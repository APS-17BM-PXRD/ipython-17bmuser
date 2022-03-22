from ophyd import ADComponent
from ophyd import ImagePlugin
from ophyd import PerkinElmerDetector
from ophyd import SingleTrigger
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd.areadetector.plugins import HDF5Plugin_V34
import os

IMAGE_FILES_ROOT = "/local/data"
TEST_IMAGE_DIR = "test/"

class LocalVarexHDF5Plugin(FileStoreHDF5IterativeWrite, HDF5Plugin_V34): ...

class LocalVarexDetector(SingleTrigger, PerkinElmerDetector):
    """Perkin-Elmer detector"""

    image = ADComponent(ImagePlugin, "image1:")
    hdf1 = ADComponent(
        LocalVarexHDF5Plugin,
        "HDF1:",
        write_path_template=os.path.join(
            IMAGE_FILES_ROOT, TEST_IMAGE_DIR
        ),
    )
