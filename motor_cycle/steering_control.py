# steering_control.py

from machine import Pin, PWM
import time

class SteeringServo:
    def __init__(self, pwm_pin_number):
        # Servos typically run at a 50Hz frequency
        self.pwm = PWM(Pin(pwm_pin_number))
        self.pwm.freq(50)
        print("Steering servo initialized.")

    def set_angle(self, angle):
        # This function maps an angle (-90 to 90) to a PWM duty cycle.
        # These values (1000 to 9000) are common but may need calibration
        # for your specific servo.
        min_duty = 1000  # Corresponds to -90 degrees (full left)
        max_duty = 9000  # Corresponds to +90 degrees (full right)
        
        # Calculate the duty cycle based on the angle
        duty_range = max_duty - min_duty
        duty_cycle = min_duty + (duty_range * (angle + 90) / 180)
        
        self.pwm.duty_u16(int(duty_cycle))

    def center(self):
        # Helper function to easily center the steering
        self.set_angle(0)