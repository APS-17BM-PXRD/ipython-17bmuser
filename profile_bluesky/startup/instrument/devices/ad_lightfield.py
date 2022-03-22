from ophyd import ADComponent
from ophyd import ImagePlugin
from ophyd import LightFieldDetector
from ophyd import SingleTrigger
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd.areadetector.plugins import HDF5Plugin_V34
import os

IMAGE_FILES_ROOT = "/local/data"
TEST_IMAGE_DIR = "test/"

class LocalLfHDF5Plugin(FileStoreHDF5IterativeWrite, HDF5Plugin_V34): ...

class LocalLightfieldDetector(SingleTrigger, LightFieldDetector):
	'''
	LightField detector

	Need to investigate this more: 
	
	https://github.com/bluesky/ophyd/blob/7937cd46e92e9ec2f7eec321dd5b1b1b71115e20/ophyd/areadetector/docs.py#L1167

	Link outlines differences in lightfield, unclear if these are implemented or are just warnings.
	
	'''
    image = ADComponent(ImagePlugin, "image1:")
    hdf1 = ADComponent(
        LocalLfHDF5Plugin,
        "HDF1:",
        write_path_template=os.path.join(
            IMAGE_FILES_ROOT, TEST_IMAGE_DIR
        ),
    )

