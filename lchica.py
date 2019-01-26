#!/usr/bin/env python
#

import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(17, RPi.GPIO.OUT)

i = 0

print('start')
while i <= 60:
        RPi.GPIO.output(17, RPi.GPIO.HIGH)
        time.sleep(0.2)
        RPi.GPIO.output(17, RPi.GPIO.LOW)
        time.sleep(0.8)
        i += 1
print('end')

RPi.GPIO.cleanup()