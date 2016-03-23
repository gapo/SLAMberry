#!/usr/bin/python2.7
# Robot Control
#
# ------------------------------
# Robot Control 
# Gautham Ponnu , Jacob George
# ECE MEng Project
# Cornell University
#
# ------------------------------

import RPi.GPIO as GPIO
import time

# Channel Define
rmotor = 26
lmotor = 16

# Declarations
GPIO.setmode(GPIO.BCM)
GPIO.setup(rmotor, GPIO.OUT)
GPIO.setup(lmotor, GPIO.OUT)

# Global Declaration
global offtime,r_on,l_on

# Frequency Parameters
offtime = 20

# Frequency Function
def freq(ontime):
    freq = 1000/(ontime+offtime)
    return freq

# Dutycycle Function
def dc(ontime):
    dc = 100*ontime/(ontime+offtime)
    return dc

# Default Start Conditions
# These are global that will contain on times
r_on = 1.5
l_on = 1.5

# PWM Starts
r_pwm=GPIO.PWM(rmotor,freq(r_on))
l_pwm=GPIO.PWM(lmotor,freq(l_on))
r_pwm.start(0)
l_pwm.start(0)

# Define Speed Control
# Speed Control increments speed between speed_lower to speed_upper 
# def speed_control(speed):
#   global motor_a
#   global motor_b

#   if (speed == "up" and motor_a > speed_upper and motor_b < speed_upper):
#     motor_a = motor_a + 10
#     motor_b = motor_b - 0.1

#   if (speed == "down" and motor_a >7.5 and motor_b < 7.5):
#     motor_a = motor_a - 0.1
#     motor_b = motor_b + 0.1
  
def motor_control(direction):
  print direction
 
  if (direction == "fwd"):
    r_on = 1.8
    l_on = 1.3
    r_pwm.ChangeFrequency(freq(r_on))
    l_pwm.ChangeFrequency(freq(l_on))
    r_pwm.ChangeDutyCycle(dc(r_on))
    l_pwm.ChangeDutyCycle(dc(l_on))
 
  if (direction == "bwd"):
    r_on = 1.8
    l_on = 1.3
    r_pwm.ChangeFrequency(freq(r_on))
    l_pwm.ChangeFrequency(freq(l_on))
    r_pwm.ChangeDutyCycle(dc(r_on))
    l_pwm.ChangeDutyCycle(dc(l_on))
 
  if (direction == "left"):     
    r_on = 1.8
    l_on = 0
    r_pwm.ChangeFrequency(freq(r_on))
    l_pwm.ChangeFrequency(freq(l_on))
    r_pwm.ChangeDutyCycle(dc(r_on))
    l_pwm.ChangeDutyCycle(dc(l_on))  
 
  if (direction == "right"):
    r_on = 0
    l_on = 1.8
    r_pwm.ChangeFrequency(freq(r_on))
    l_pwm.ChangeFrequency(freq(l_on))
    r_pwm.ChangeDutyCycle(dc(r_on))
    l_pwm.ChangeDutyCycle(dc(l_on))
  
  if (direction == "stop"):
    r_pwm.ChangeDutyCycle(0)
    l_pwm.ChangeDutyCycle(0) 

def _main_():
    # This will be my main loop
    print ("f - fwd \n b - bwd \n r - right \n l - left \n u - speed up \n d - speed down")
    while True:
      motor_control('stop')
      choice = raw_input("> ")
      if choice == 'f' :
        motor_control('fwd')
      elif choice == 'b' :
        motor_control('bwd')
      elif choice == 'r' :
        motor_control('right')
      elif choice == 'l' :
        motor_control('left')
      # elif choice == 'u' :
      #   speed_control('up')
      # elif choice == 'd' :
      #   speed_control('down')
      elif choice == 'q' :
        break
      time.sleep(1)

_main_()
