import logging
import numpy as np
import pkg_resources
import cv2 as cv
import glob
from collections import namedtuple


log = logging.getLogger(__name__)


class FakeCamera:
    """
    simulated camera
    """

    def __init__(self):
        pattern = pkg_resources.resource_filename('mbmega_face_expressions', '../data/*')
        self.files = glob.glob(pattern)

    def capture(self):
        """
        capture 3 color image
        """
        img = cv.imread(self.files[-5])
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return img
        #return np.zeros((1600, 2000, 3), dtype='uint8')


def dummy(*args):
    pass


class FakeBot:
    """
    Simulated Mega Bot Robot
    """

    def DCMotor(self):
        DC = namedtuple('DC', ['run'])
        return DC(run=dummy)

    def RGBLed(self):
        RGB = namedtuple('RGB', ['set_color'])
        return RGB(set_color=dummy)
