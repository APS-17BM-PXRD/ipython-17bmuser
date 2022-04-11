"""
Shutter control

"""

__all__ = [
    "shutter17bmb",
]

from ..session_logs import logger
logger.info(__file__)

from apstools.devices import EpicsOnOffShutter
from ophyd import EpicsSignal
import bluesky.plan_stubs as bps


openClosePV = "17bm:XiaPfcu2:Filter2Bo.VAL"


shutter17bmb = EpicsOnOffShutter(openClosePV, name="shutter17bmb")
shutter17bmb.close_value = 1  # Insert
shutter17bmb.open_value = 0 # Retract
