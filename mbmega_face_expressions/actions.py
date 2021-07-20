import logging
import numpy as np
import asyncio as aio
from time import sleep
from random import random
import math
from makeblock import MegaPi, SerialPort


log = logging.getLogger(__name__)


A6 = 60
A7 = 61
A8 = 62
A9 = 63
A10 = 64
A11 = 65
A12 = 66
A13 = 67
A14 = 68
A15 = 69

COLORS = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'magenta': (255, 0, 255),
}


def set_rgb(bot, r, g, b):
    """
    set 2x4 rgb leds to the same color
    """
    led = bot.RGBLed()
    for idx in range(1, 5):
        led.set_color(idx, r, g, b, A13)
        led.set_color(idx, r, g, b, A14)


async def move_xyw(bot, x, y, w, t):
    """
    move robot in x, y, w space for t seconds
    x = forward
    y = left
    w = rotate about z  (x cross y)

    robot has mecanum wheels
    """
    motor1 = bot.DCMotor(1, 1)  # RF forward
    motor2 = bot.DCMotor(1, 2)  # RR forward
    motor3 = bot.DCMotor(2, 1)  # LR reverse
    motor4 = bot.DCMotor(2, 2)  # LF reverse

    # motor mapping
    R_motor = np.array([[+1, +1, -1, -1],   # X
                        [+1, -1, -1, +1],   # Y
                        [+1, +1, +1, +1]])   # w (z rotation)

    xyw = np.array([x, y, w])
    motor_cmd = xyw @ R_motor
    motor1.run(motor_cmd[0])
    motor2.run(motor_cmd[1])
    motor3.run(motor_cmd[2])
    motor4.run(motor_cmd[3])
    await aio.sleep(t)
    motor1.run(0)
    motor2.run(0)
    motor3.run(0)
    motor4.run(0)


async def happy_action(bot):
    log.info('happy action')
    set_rgb(bot, *COLORS['green'])
    await move_xyw(bot, 0, 0, 50, 0.3)
    await aio.sleep(0.2)
    await move_xyw(bot, 0, 0, -50, 0.3)


async def angry_action(bot):
    log.info('angry action')
    set_rgb(bot, *COLORS['red'])
    await move_xyw(bot, 0, 50, 0, 0.3)
    await aio.sleep(0.2)
    await move_xyw(bot, 0, -50, 0, 0.3)


async def show_blue(bot):
    log.info('show_blue')
    set_rgb(bot, *COLORS['blue'])


async def surprised_action(bot):
    log.info('surprised_action')
    set_rgb(bot, *COLORS['yellow'])
    await move_xyw(bot, 100, 0, 0, 0.3)
    await aio.sleep(0.2)
    await move_xyw(bot, -100, 0, 0, 0.3)


async def show_magenta(bot):
    log.info('show_magenta')
    set_rgb(bot, *COLORS['magenta'])


async def led_off(bot):
    log.info('led_off')
    set_rgb(bot, *COLORS['black'])
