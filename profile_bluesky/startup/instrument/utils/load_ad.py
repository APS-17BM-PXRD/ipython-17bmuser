""" Loads a new eiger device """

from ..devices.ad_varex import LocalVarexDetector
from ..devices.ad_lightfield import LocalLightfieldDetector
from ..framework import sd
from ..session_logs import logger
logger.info(__file__)

__all__ = """
    load_varex
    load_lighfield
""".split()


def load_varex(pv="17bmXRD:"):

    print("-- Loading Varex detector --")
    varex = LocalVarexDetector(pv, name="varex")
#   det_pe = LocalVarexDetector("XRD1:", name="det_pe")
    sd.baseline.append(varex)

    varex.wait_for_connection(timeout=10)
    # This is needed otherwise .get may fail!!!

    varex.hdf1.create_directory.put(-5)
    varex.cam.stage_sigs["image_mode"] = "Single"
    varex.cam.stage_sigs["num_images"] = 1
    varex.cam.stage_sigs["acquire_time"] = 0.1
    varex.cam.stage_sigs["acquire_period"] = 0.105
    varex.hdf1.stage_sigs["lazy_open"] = 1
    varex.hdf1.stage_sigs["compression"] = "LZ4"
    varex.hdf1.stage_sigs["file_template"] = "%s%s_%3.3d.h5"
    del varex.hdf1.stage_sigs["capture"]
    varex.hdf1.stage_sigs["capture"] = 1

    print("Done!")
    print("All done!")

    return varex
    
    
def load_lightfield(pv="17bmLF1:")
	'''
	Need to investigate this more: 
	
	https://github.com/bluesky/ophyd/blob/7937cd46e92e9ec2f7eec321dd5b1b1b71115e20/ophyd/areadetector/docs.py#L1167

	Link outlines differences in lightfield, unclear if these are implemented or are just warnings.
	
	'''


    print("-- Loading Lightfield detector --")
    lightfield = LocalLightfieldDetector(pv, name="lightfield")
#   det_pe = LocalLightfieldDetector("LF1:", name="det_pe")
    sd.baseline.append(lightfield)

    lightfield.wait_for_connection(timeout=10)
    # This is needed otherwise .get may fail!!!
 
    lightfield.hdf1.create_directory.put(-5)
    lightfield.cam.stage_sigs["image_mode"] = "Normal"
    lightfield.cam.stage_sigs["num_images"] = 1
    lightfield.cam.stage_sigs["acquire_time"] = 0.1
    lightfield.cam.stage_sigs["acquire_period"] = 0.105
    lightfield.hdf1.stage_sigs["lazy_open"] = 1
    lightfield.hdf1.stage_sigs["compression"] = "LZ4"
    lightfield.hdf1.stage_sigs["file_template"] = "%s%s_%3.3d.h5"
    del lightfield.hdf1.stage_sigs["capture"]
    lightfield.hdf1.stage_sigs["capture"] = 1

    print("Done!")
    print("All done!")
    return lightfield    
