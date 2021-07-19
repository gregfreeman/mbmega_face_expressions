from time import sleep
from random import random
import math
from makeblock import MegaPi,SerialPort


###USAGE###
# pip3 install makeblock --upgrade
###########
from time import sleep
from random import random
import math
from makeblock import MegaPi,SerialPort
A6 = 60
A7 = 61
A8 = 62
A9 = 63
A10= 64
A11= 65
A12= 66
A13= 67
A14= 68
A15= 69

A6 = 60  # ir detector
A7 = 61
A8 = 62  
A9 = 63 # line following
A10= 64 
A11= 65 # switches
A12= 66 
A13= 67 # LED
A14= 68
A15= 69 # open


megapi = MegaPi.connect() # or 
megapi = MegaPi.connect(SerialPort.connect("/dev/ttyUSB1"))
megapi = MegaPi.connect(SerialPort.connect("/dev/ttyUSB0"))
led = megapi.RGBLed()
j = 0
f = 0
k = 0
pixels = [0]*12
for i in range(100):
  for t in range(0,4):
    pixels[t*3] = int(16 * (1 + math.sin(t / 2.0 + j / 4.0)))
    pixels[t*3+1] = int(16 * (1 + math.sin(t / 1.0 + f / 9.0 + 2.1)))
    pixels[t*3+2] = int(16 * (1 + math.sin(t / 3.0 + k / 14.0 + 4.2)))
  led.set_colors(pixels,A13)
  j += random()
  f += random()
  k += random()
  sleep(0.01)


led = megapi.RGBLed()
pixels = [0]*12
for t in range(0,4):
    pixels[t*3] = 255
    pixels[t*3+1] = 0
    pixels[t*3+2] = 0
led.set_colors(pixels,A13)
led.set_colors(pixels,A14)


led = megapi.RGBLed()
led.set_colors(1,0xff,0xff,0xff,A13)
led.set_colors(1,0xff,0xff,0xff,A14)


led = megapi.RGBLed()
led.set_color(2,0xff,0xff,0xff,A13)
led.set_color(2,0xff,0xff,0xff,A14)


led = megapi.RGBLed()
led.set_color(3,0xff,0,0,A13)
led.set_color(3,0xff,0,0,A14)

led.set_color(4,0xff,0,0,A13)
led.set_color(4,0xff,0,0,A14)



pin = megapi.Pin()
for i in range(20):
   print(pin.digital_read(A6),pin.digital_read(A7),pin.digital_read(A8))
   sleep(0.2)


motor1 = megapi.DCMotor(1,1)  # RF forward
motor2 = megapi.DCMotor(1,2)  # RR forward
motor3 = megapi.DCMotor(2,1)  # LR reverse
motor4 = megapi.DCMotor(2,2)  # LF reverse



R_motor = np.array([[+1 +1 -1 -1],   # X
                    [+1 -1 +1 -1],   # Y
                    [+1 +1 +1 +1]]   # w (z rotation)


motor1.run(50)
motor2.run(50)
motor3.run(50)
motor4.run(50)
sleep(1)
motor1.run(0)
motor2.run(0)
motor3.run(0)
motor4.run(0) 


motor = motor4
motor.run(50)
sleep(1)
motor.run(0)




ls /dev/ttyU*



  R_motor = np.array([[+1 + 1 - 1 - 1],   # X
                      [+1 - 1 + 1 - 1],   # Y
                      [+1 + 1 + 1 + 1]]   # w (z rotation)

