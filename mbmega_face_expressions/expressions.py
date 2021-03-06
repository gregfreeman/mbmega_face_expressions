import cv2 as cv
import numpy as np
import tensorflow as tf
import logging
import pkg_resources


log = logging.getLogger(__name__)


class EmotionRecognizer:
    """
    module for face detection
    """

    def __init__(self):
        fname = pkg_resources.resource_filename('mbmega_face_expressions', '../resources/emotion_detector_model_v6_23.h5')
        print(fname)
        self.model = tf.keras.models.load_model(fname)
        self.emotion_dict = {'angry': 0, 'sad': 5, 'neutral': 4, 'disgust': 1, 'surprise': 6, 'fear': 2, 'happy': 3}
        self.label_map = dict((v, k) for k, v in self.emotion_dict.items())

    def predict(self, face_image):
        """
        input 3 color cropped face image
        output predicted label and output layer scores
        """
        face_image = cv.resize(face_image, (48, 48))
        face_image = cv.cvtColor(face_image, cv.COLOR_RGB2GRAY)
        face_image = np.reshape(face_image, [1, face_image.shape[0], face_image.shape[1], 1])
        olayer = self.model.predict(face_image)
        predicted_class = np.argmax(olayer)
        predicted_label = self.label_map[predicted_class]
        return predicted_label, olayer
