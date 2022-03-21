"""
PTC10 Programmable Temperature Controller
"""

__all__ = [
    "cs800",
]

from ..session_logs import logger
logger.info(__file__)

from apstools.devices import PTC10AioChannel
from apstools.devices import PTC10PositionerMixin
from apstools.devices import PTC10RtdChannel
from apstools.devices import PTC10TcChannel
from ophyd import Component
from ophyd import EpicsSignalRO
from ophyd import EpicsSignalWithRBV
from ophyd import PVPositioner

class OXFORD_CS800(PVPositioner):
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



cs800 = oxford_cs800("17bmCryo:BM:", name="cs800")
cs800.report_dmov_changes.put(True)  # a diagnostic
cs800.tolerance.put(1.0)  # done when |readback-setpoint|<=tolerance

