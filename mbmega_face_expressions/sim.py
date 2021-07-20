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
        self.idx = 0

    def capture(self):
        """
        capture 3 color image
        """
        log.info('Image: %d' % self.idx)
        img = cv.imread(self.files[self.idx])
        self.idx = (self.idx + 1) % len(self.files)

        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        return img


def dummy(*args):
    pass


class FakeBot:
    """
    Simulated Mega Bot Robot
    """

    def DCMotor(self, *args):
        DC = namedtuple('DC', ['run'])
        return DC(run=dummy)

    def RGBLed(self, *args):
        RGB = namedtuple('RGB', ['set_color'])
        return RGB(set_color=dummy)
