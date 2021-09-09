"""
slits
"""

__all__ = """
	slitUpH
	slitUpV
	slitDnH
	slitDnV
    """.split()



from ..session_logs import logger
logger.info(__file__)

from bluesky import plan_stubs as bps
from ophyd import Component, EpicsSignal, MotorBundle

# from ..framework import sd
# from .general_terms import terms
# from .usaxs_motor_devices import UsaxsMotor
# from ..utils import move_motors

class SlitDevice(MotorBundle):

    """
    17BM slits
    * center of slit: (center)
    * aperture: (size)
    """

    size	= Component(EpicsSignal, '', labels=("slit",))
    center	= Component(EpicsSignal, '', labels=("slit",))





slitUpH = SlitDevice(pv='17bmb:SlitUpH')
slitUpV = SlitDevice(pv='17bmb:SlitUpV')
slitDnH = SlitDevice(pv='17bmb:SlitDnH')
slitDnV = SlitDevice(pv='17bmb:SlitDnV')
