""" Loads a new eiger device """

from ..devices.ad_varex import VarexSingleTrigDet, VarexMultiTrigDet 
from ..devices.ad_lightfield import LocalLightfieldDetector
from ..devices.shutters import *
from ..framework import sd
from ..session_logs import logger
logger.info(__file__)

__all__ = """
    load_varex_single
    load_varex_multi
    junk_phase_template
    dark_phase_template
    light_phase_template
    load_lightfield
""".split()


def load_varex_single(pv="17bmXRD:"):

    print("-- Loading Varex detector with Single Trigger --")
    varex1 = VarexSingleTrigDet(pv, name="varex1")
#   det_pe = LocalVarexDetector("XRD1:", name="det_pe")
#    sd.baseline.append(varex1)

    varex1.wait_for_connection(timeout=10)
    # This is needed otherwise .get may fail!!!

#    varex1.hdf1.create_directory.put(-5)
    varex1.cam.stage_sigs["image_mode"] = "Single"
    varex1.cam.stage_sigs["num_images"] = 1
    varex1.cam.stage_sigs["acquire_time"] = 0.05
    varex1.cam.stage_sigs["acquire_period"] = 0.105
#    varex1.hdf1.stage_sigs["lazy_open"] = 1
#    varex1.hdf1.stage_sigs["compression"] = "LZ4"
#    varex1.hdf1.stage_sigs["file_template"] = "%s%s_%3.3d.h5"
#    del varex1.hdf1.stage_sigs["capture"]
#    varex1.hdf1.stage_sigs["capture"] = 1

    print("Done!")
    print("All done!")

    return varex1


#Default cycle takes 2 junk, 10 dark, 30 data
#To change at run_time: varex.trigger_cycle = new_cycle
    
#junk_phase_template = [('junk', {'shutter17bmb':'closed'})]                                                                      
#dark_phase_template = [('dark', {'shutter17bmb':'closed'})]                                                                      
#light_phase_template = [('light', {'shutter17bmb':'open'})]

#Shutter may have to be integrated into AD setup; for the time being
#using acquire_time to test multiple frames - MW 2022.04.04
junk_phase_template = [('junk', {'acquire_time':0.5})]                                                                      
dark_phase_template = [('dark', {'acquire_time':0.1})]                                                                      
light_phase_template = [('light', {'acquire_time':1.0})]


default_n_junk = 2      
default_n_dark = 10
default_n_light = 10
 
default_cycle = [junk_phase_template*default_n_junk + 
                 dark_phase_template*default_n_dark +
                 light_phase_template*default_n_light]
    
def load_varex_multi(pv="17bmXRD:", trigger_cycle = default_cycle):

    print("-- Loading Varex detector with Multiple Trigger --")
    varexN = VarexMultiTrigDet(pv, name="varexN", trigger_cycle = trigger_cycle)
#   Commented out next line as having it as a baseline reading was killing plans
#   it wasn't a detector for
#    sd.baseline.append(varexN) 

    #reseting trigger cycle
    junk_phase_template = [('junk', {varexN.cam.acquire_time:0.5})]                                                                      
    dark_phase_template = [('dark', {varexN.cam.acquire_time:0.1})]                                                                      
    light_phase_template = [('light', {varexN.cam.acquire_time:1.0})]

    default_cycle = [junk_phase_template*default_n_junk + 
                     dark_phase_template*default_n_dark +
                     light_phase_template*default_n_light]
    

    varexN.wait_for_connection(timeout=10)
    # This is needed otherwise .get may fail!!!

#    varexN.hdf1.create_directory.put(-5)
    varexN.cam.stage_sigs["image_mode"] = "Multiple"
    varexN.cam.stage_sigs["num_images"] = 1
    varexN.cam.stage_sigs["acquire_time"] = 0.05
    varexN.cam.stage_sigs["acquire_period"] = 0.105
#    varexN.hdf1.stage_sigs["lazy_open"] = 1
#    varexN.hdf1.stage_sigs["compression"] = "LZ4"
#    varexN.hdf1.stage_sigs["file_template"] = "%s%s_%3.3d.h5"
#    del varexN.hdf1.stage_sigs["capture"]
#    varexN.hdf1.stage_sigs["capture"] = 1
    
#    varexN.trigger_cycle(default_cycle)
    varexN.trigger_cycle = default_cycle

    print("Done!")
    print("All done!")

    return varexN    
    
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
