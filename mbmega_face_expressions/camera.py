import logging
import numpy as np
log = logging.getLogger(__name__)

try:
    from picamera import PiCamera
    has_picamera = False
except Exception:
    has_picamera = False
    log.warning('does not have picamera - simulation?')


class Camera:
    """
    module for capturing images
    """

    def __init__(self):
        self.camera = PiCamera()
        self.camera.rotation = 180
        self.camera.start_preview()

    def capture(self):
        """
        capture 3 color image
        """
        output = np.empty((480, 720, 3), dtype=np.uint8)
        self.camera.capture(output, 'rgb')
        return output
