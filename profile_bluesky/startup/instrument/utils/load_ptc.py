'''
	PTC10 Controller with capability of adding control loops.  
	If multiple loops needed, create multiple instances:
	
	ptcA = load_ptc10(loop = {'set':'5A', 'read':'2A'})
	ptcB = load_ptc10(loop = {'set':'3A', 'read':'5C'})
	
	Otherwise if no loops are needed:
	ptcC = load_ptc10(loop = None)

'''

from ..devices.ptc10_controller import BM17_PTC10_Base 
from ..framework import sd
from ..session_logs import logger
logger.info(__file__)

__all__ = """
    load_ptc10
""".split()


def load_ptc10(prefix = "17bmb:tc1:", loop = {'set':'5A', 'read':'2A'}, 
               name = 'ptc10'):
	
	'''
	prefix	:	defaults to 17bmb:tc1:
	
	loop	:	dictionary for control loop. Defaults to AIO channel 5A
				as the output and temperature channel 2A as readback. For 17BM,
				can use 5A, .... as controls and 2A, .... as readbacks
	name	:	defaults to ptc10, 
	
	'''
	
	print('Basic PTC10 controller setup as: {}'.format(name)) 
	ptc10 = BM17_PTC10("17bmb:tc1:", name=name)
	
	if loop is not None:
		# Basic PVPositioner setup
		
		#TODO: Need to add conditional to handle RTD as set
		set_sig = loop['set']+':setPoint'
		#TODO: Need to add conditional to handle AIO as readback
		read_sig = loop['read']+':temperature'
		
		ptc10.setpoint = Component(EpicsSignalWithRBV, set_sig, kind="hinted")
		ptc10.readback = Component(EpicsSignalRO, read_sig, kind="hinted")

		#TODO: Need to accoutn for RTD -- is there a ramprate?
		# For 17BM add a simpler path to ramp rate
		if loop['set'] == '5A':
			ptc10.ramp = ptc10.pidA.ramprate
		elif loop['set'] == '5B':
			ptc10.ramp = ptc10.pidB.ramprate
		elif loop['set'] == '5C':
			ptc10.ramp = ptc10.pidC.ramprate
		elif loop['set'] == '5D':
			ptc10.ramp = ptc10.pidD.ramprate
		else:
			print('Using RTD for setpoint in control loop - ')
			print('ramp shortcut not used.')	
			
		ptc10.report_dmov_changes.put(True)  # a diagnostic
		ptc10.tolerance.put(1.0)  # done when |readback-setpoint|<=tolerance
	
	return ptc10
