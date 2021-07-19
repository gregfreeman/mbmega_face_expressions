import face_recognition
from mbmega_face_expressions.expressions import EmotionRecognizer
from mbmega_face_expressions.actions import happy_action, angry_action, show_blue, show_yellow, show_magenta, led_off
from mbmega_face_expressions.camera import Camera
from mbmega_face_expressions.sim import FakeCamera, FakeBot
import logging
import asyncio as aio
import traceback
from makeblock import MegaPi,SerialPort



log = logging.getLogger(__name__)


class Controller:
    """
    Main controller for robot
    """
    def __init__(self, sim=False):

        self.action_dict = dict(
            happy=happy_action,
            angry=angry_action,
            sad=show_blue,
            scared=show_magenta,
            surprised=show_yellow,
            default=led_off)

        self.model_emotion = EmotionRecognizer()
        if sim:
            self.bot = FakeBot()
            self.cam = FakeCamera()
        else:
            self.bot = MegaPi.connect(SerialPort.connect("/dev/ttyUSB0"))
            self.cam = Camera()
        self.sig_stop = False
        self.step_count = 0
        self.state = 'Initialized'
        aio.ensure_future(self.start())

    async def initialize(self):
        pass

    async def start(self):
        await self.initialize()
        self.state = 'Running'
        await aio.sleep(1)
        while(not self.sig_stop):
            try:
                await self.step()
            except Exception:
                log.error(traceback.format_exc())
                self.state = 'Fault'
                return
            self.step_count += 1
        print(stopped)
        self.state = 'Stopped'

    async def stop(self):
        self.sig_stop = True

    async def step(self):
        """
        controller step

        capture image
        detect faces
        recognize expressions
        perform action based on expression
        """

        img = self.cam.capture()
        faces = face_recognition.face_locations(img)
        if len(faces) > 1:
            log.warning('Multiple faces detected. Only using one face')
        if len(faces) > 0:
            # predict emotion
            top, right, bottom, left = faces[0]
            face_image = img[top:bottom, left:right]
            emotion, olayer = self.model_emotion.predict(face_image)
            # perform ation based on emotion
            default_action = led_off
            func = self.action_dict.get(emotion, default_action)
            if func is not None:
                await func(self.bot)

        await aio.sleep(1)
