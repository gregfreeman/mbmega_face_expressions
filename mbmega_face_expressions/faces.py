import cv2 as cv
import logging


log = logging.getLogger(__name__)


class FaceDetector:
    """
    module for face detection
    """

    def __init__(self):
        self.detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

    def detect_faces(self, img):
        """
        import 3 color image
        output list of faces as tuples (x,y,w,h)
        """
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = self.detector.detectMultiScale(gray, 1.1, 4)
        return faces
