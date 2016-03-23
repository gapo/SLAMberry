#!/usr/bin/python
import RPi.GPIO as GPIO

pin = 16
#pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

# Frequency
ontime = 1.5
offtime = 20
freq = 1000/(ontime+offtime)
dc=100*ontime/(ontime+offtime)

print("Freq =")
print(freq)
print("DC =")
print(dc)
p = GPIO.PWM(pin,freq)
p.start(1)
p.ChangeDutyCycle(dc)
raw_input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()
