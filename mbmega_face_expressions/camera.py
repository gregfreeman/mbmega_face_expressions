import cv2 as cv
import logging
import numpy as np
log = logging.getLogger(__name__)

try:
    from picamera import PiCamera
    has_picamera = False
except Exception:
    has_picamera = False
    print('does not have picamera - simulation?')


class Camera:
    """
    module for face detection
    """

    def __init__(self):
        self.camera = PiCamera()

    def capture(self):
        """
        capture 3 color image
        """
        return self.camera
