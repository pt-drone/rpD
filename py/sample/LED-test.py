import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
for x in xrange(5):
    GPIO.output(2,True)
    time.sleep(0.5)
    GPIO.output(2,False)
    time.sleep(0.5)
GPIO.cleanup()