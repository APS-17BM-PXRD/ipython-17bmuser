"""
Oxford Cryostream 800
"""

__all__ = [
    "cs800",
]

from ..session_logs import logger
logger.info(__file__)

from ophyd import Component, Device, Signal
from ophyd import EpicsSignalRO
from ophyd import EpicsSignalWithRBV
from ophyd import PVPositioner

#Cryostream may not work as simply as PTC10; may need to utilize "programming"
#PVs as SETPOINT, TARGETTEMP, and TEMP appear to be read-only
#
#Looking at Programming UI:
#
# Cooldown: CTEMP (K) + COOL.PROC
# Ramp up: RRATE (K/h) + RTEMP (K) + RAMP.PROC
# plateau: PTIME (min)

class OxfordPositionerMixin(Device):
    """
    Mixin so Oxford CryoStream can be used as a (temperature) positioner.
    .. autosummary::
       ~cb_readback
       ~cb_setpoint
       ~inposition
       ~stop
    """

    done = Component(Signal, value=True, kind="omitted")
    done_value = True

    # for computation of soft `done` signal
    # default +/- 1 degree for "at temperature"
    tolerance = Component(Signal, value=1, kind="config")

    # For logging when temperature is reached after a move.
    report_dmov_changes = Component(Signal, value=True, kind="omitted")

    def cb_readback(self, *args, **kwargs):
        """
        Called when readback changes (EPICS CA monitor event).
        """
        diff = self.readback.get() - self.setpoint.get()
        dmov = abs(diff) <= self.tolerance.get()
        if self.report_dmov_changes.get() and dmov != self.done.get():
            logger.debug(f"{self.name} reached: {dmov}")
        self.done.put(dmov)

    def cb_setpoint(self, *args, **kwargs):
        """
        Called when setpoint changes (EPICS CA monitor event).
        When the setpoint is changed, force ``done=False``.  For any move,
        ``done`` MUST change to ``!= done_value``, then change back to
        ``done_value (True)``.  Without this response, a small move
        (within tolerance) will not return.  Next update of readback
        will compute ``self.done``.
        """
        self.done.put(not self.done_value)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.readback.name = self.name

        # to compute the soft `done` signal
        self.readback.subscribe(self.cb_readback)
        self.setpoint.subscribe(self.cb_setpoint)

    @property
    def inposition(self):
        """
        Report (boolean) if positioner is done.
        """
        return self.done.get() == self.done_value

    def stop(self, *, success=False):
        """
        Hold the current readback when the stop() method is called and not done.
        """
        if not self.done.get():
            self.setpoint.put(self.position)

class OXFORD_CS800(OxfordPositionerMixin, PVPositioner):
    """
    Oxford CryoStream 800 
    USAGE
    * Change the temperature and wait to get there: ``yield from bps.mv(ptc10, 75)``
    * Change the temperature and not wait: ``yield from bps.mv(ptc10.setpoint, 75)``
    * Change other parameter: ``yield from bps.mv(ptc10.tolerance, 0.1)``
    * To get temperature: ``ptc10.position``  (because it is a **positioner**)
    * Is it at temperature?:  ``ptc10.done.get()``
    """

    # PVPositioner interface
    readback = Component(EpicsSignalRO, "TEMP", kind="hinted")
    setpoint = Component(EpicsSignalWithRBV, "SETPOINT", kind="hinted")

    # PTC10 base
    enable = Component(EpicsSignalWithRBV, "outputEnable", kind="config", string=True)


