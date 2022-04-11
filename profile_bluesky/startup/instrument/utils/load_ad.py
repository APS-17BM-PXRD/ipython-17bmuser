""" Loading AD devices """

from ..devices.ad_varex import VarexSingleTrigDet, VarexMultiTrigDet 
from ..devices.ad_lightfield import LocalLightfieldDetector
from ..devices.shutters import *
from ..framework import sd
from ..session_logs import logger
logger.info(__file__)

__all__ = """
    load_varex
    junk_phase_template
    dark_phase_template
    light_phase_template
    load_lightfield
""".split()

#Default cycle takes 2 junk, 10 dark, 30 data
#To change at run_time: varex.trigger_cycle = new_cycle

#shutter17bmb: 1 -- inserted; 0 -- retracted
junk_phase_template = [('junk', {shutter17bmb.signal:1})]                                                                      
dark_phase_template = [('dark', {shutter17bmb.signal:1})]                                                                      
light_phase_template = [('light', {shutter17bmb.signal:0})

default_n_junk = 2      
default_n_dark = 10
default_n_light = 10
 
default_cycle = [junk_phase_template*default_n_junk + 
                 dark_phase_template*default_n_dark +
                 light_phase_template*default_n_light]

def reset_dark_light_cycle(n_junk, n_dark, n_light, num_images_sig,
                           shutter_sig = shutter17bmb.signal, openVal = 1, closedVal = 0):

    junk_phase_template = [('junk', {shutter_sig:closedVal, num_images_sig:n_junk})]                                                                      
    dark_phase_template = [('dark', {shutter_sig:closedVal, num_images_sig:n_dark})]                                                                      
    light_phase_template = [('light', {shutter_sig:openVal, num_images_sig:n_light})]
    
    trig_cycle = [junk_phase_template + dark_phase_template + light_phase_template]
    
    return trig_cycle

def load_varex(pv="17bmXRD:", trigger_cycle = default_cycle, multi = False):



    if not multi:
        print("-- Loading Varex detector with Single Trigger --")
        varex = VarexSingleTrigDet(pv, name="varex1")
    else:
        print("-- Loading Varex detector with Multiple Trigger --")
        varex = VarexMultiTrigDet(pv, name="varexN", trigger_cycle = trigger_cycle)
    
    varex.wait_for_connection(timeout=5)
    
    varex.cam.stage_sigs["num_images"] = 1
        
    if multi:
        varex.cam.stage_sigs["image_mode"] = "Multiple"
        if trigger_cycle == default_cycle:
            varex.trigger_cycle = reset_dark_light_cycle(default_n_junk, default_n_dark,
                                                         default_n_light, varex.cam.num_images, 
                                                         shutter_sig = shutter17bmb.signal)
    else:
        varex.cam.stage_sigs["image_mode"] = "Single"

    print("Done!")
    print("All done!")
    
    return varex
    
def load_lightfield(pv="17bmLF1:"):
#   Need to investigate this more: 
    
#   https://github.com/bluesky/ophyd/blob/7937cd46e92e9ec2f7eec321dd5b1b1b71115e20/ophyd/areadetector/docs.py#L1167

#   Link outlines differences in lightfield, unclear if these are implemented or are just warnings.

    print("-- Loading Lightfield detector --")
    lightfield = LocalLightfieldDetector(pv, name="lightfield")
#   det_pe = LocalLightfieldDetector("LF1:", name="det_pe")
    sd.baseline.append(lightfield)

    lightfield.wait_for_connection(timeout=10)
    # This is needed otherwise .get may fail!!!
 
#    lightfield.hdf1.create_directory.put(-5)
    lightfield.cam.stage_sigs["image_mode"] = "Normal"
    lightfield.cam.stage_sigs["num_images"] = 1
    lightfield.cam.stage_sigs["acquire_time"] = 0.1
    lightfield.cam.stage_sigs["acquire_period"] = 0.105
 #   lightfield.hdf1.stage_sigs["lazy_open"] = 1
 #   lightfield.hdf1.stage_sigs["compression"] = "LZ4"
#    lightfield.hdf1.stage_sigs["file_template"] = "%s%s_%3.3d.h5"
#    del lightfield.hdf1.stage_sigs["capture"]
#    lightfield.hdf1.stage_sigs["capture"] = 1

    print("Done!")
    print("All done!")
    return lightfield    
