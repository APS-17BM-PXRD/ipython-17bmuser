from ophyd import ADComponent
from ophyd import ImagePlugin
from ophyd import PerkinElmerDetector
from ophyd import SingleTrigger, MultiTrigger
from ophyd.areadetector.filestore_mixins import FileStoreHDF5IterativeWrite
from ophyd.areadetector.plugins import HDF5Plugin_V34
import os

IMAGE_FILES_ROOT = "/local/data"
TEST_IMAGE_DIR = "test/"

class LocalVarexHDF5Plugin(FileStoreHDF5IterativeWrite, HDF5Plugin_V34): ...

class VarexSingleTrigDet(SingleTrigger, PerkinElmerDetector):
#    Perkin-Elmer detector with Single Trigger

    image = ADComponent(ImagePlugin, "image1:")

    def stage(self):
        # Make sure that detector is not armed.
    #   set_and_wait(self.cam.acquire, 0)
        super().stage()
        # The trigger button does not track that the detector is done, so
        # the image_count is used. Not clear it's the best choice.
    #   self._image_count.subscribe(self._acquire_changed)
    #    set_and_wait(self.cam.acquire, 1)
        print('Varex staged.')
            
    def unstage(self):
        super().unstage()
   #     self._image_count.clear_sub(self._acquire_changed)
   #     set_and_wait(self.cam.acquire, 0)
        print('Varex un- staged.')
        
#    hdf1 = ADComponent(LocalVarexHDF5Plugin, "HDF1:", write_path_template=os.path.join(IMAGE_FILES_ROOT, TEST_IMAGE_DIR))


class VarexMultiTrigDet(MultiTrigger, PerkinElmerDetector):
#    Perkin-Elmer detector with Multiple Triggers

    image = ADComponent(ImagePlugin, "image1:")

    def stage(self):
        # Make sure that detector is not armed.
    #   set_and_wait(self.cam.acquire, 0)
        super().stage()
        # The trigger button does not track that the detector is done, so
        # the image_count is used. Not clear it's the best choice.
    #   self._image_count.subscribe(self._acquire_changed)
    #    set_and_wait(self.cam.acquire, 1)
        print('Varex staged.')
            
    def unstage(self):
        super().unstage()
   #     self._image_count.clear_sub(self._acquire_changed)
   #     set_and_wait(self.cam.acquire, 0)
        print('Varex un- staged.')

#    hdf1 = ADComponent(LocalVarexHDF5Plugin, "HDF1:", write_path_template=os.path.join(IMAGE_FILES_ROOT, TEST_IMAGE_DIR))
