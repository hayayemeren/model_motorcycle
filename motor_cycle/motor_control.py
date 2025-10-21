# motor_control.py

from machine import Pin, PWM

class DriveMotor:
    def __init__(self, pwm_pin_number):
        # Setup PWM on the specified pin
        self.pwm_pin = PWM(Pin(pwm_pin_number))
        self.pwm_pin.freq(10000) # Set a suitable PWM frequency
        print("Motor controller initialized.")

    def set_speed(self, percent):
        # A value of 0 is stop, 100 is max forward
        # This function will contain the logic to map a percentage
        # to the specific duty cycle required by the motor.
        # For example:
        if percent == 0:
            duty_cycle = 0 # motor off
        else:
            # Map a 0-100% value to the motor's operational range
            # This needs careful calculation based on the manual
            duty_cycle = int(10000 + (percent * 55000 / 100)) # Example values
        
        self.pwm_pin.duty_u16(duty_cycle)

    def stop(self):
        self.set_speed(0)