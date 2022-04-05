"""
Shutter control

For 17bm:XiaPfcu2:Filter2Bo, 17bm:rShtrB:Open sequence is run before 
opening in this sequence

1 --> 17bm:9440:1:bo_2.VAL PP; no delay
0 --> 17bm:9440:1:bo_2.VAL PP; delay 2 seconds before sending value ("0")

"""

__all__ = [
    "shutter17bmb",
]

from ..session_logs import logger
logger.info(__file__)

from apstools.devices import EpicsOnOffShutter
from ophyd import EpicsSignal
import bluesky.plan_stubs as bps

preOpenPV = "17bm:rShtrB:Open.PROC"
openClosePV = "17bm:XiaPfcu2:Filter2Bo.VAL"



class Shutter17BM(EpicsOnOffShutter):
	'''
	17BM's shutter also PROCs the following PV 17bm:rShtrB:Open when opening
	but not when closing 
	
	EXAMPLE::
        bit_shutter = Shutter17BM("2bma:bit1", name="bit_shutter")
        bit_shutter.close_value = 0      # default
        bit_shutter.open_value = 1       # default
        bit_shutter.open()
        bit_shutter.close()
        # or, when used in a plan
        def planA():
            yield from mv(bit_shutter, "open")
            yield from mv(bit_shutter, "close")
	'''
	
	preOpenSeq = EpicsSignal(preOpenPV)
		
	# Extending open to include pre-opening sequence
	def open(self):
		self.preOpenSeq.put(1)
		super().open()
	
	

shutter17bmb = EpicsOnOffShutter(openClosePV, name="shutter17bmb")
# 17BM's shutter doesn't follow default values
shutter17bmb.close_value = 1  # Insert
shutter17bmb.open_value = 0 # Retract
