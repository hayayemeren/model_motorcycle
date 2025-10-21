# main.py

import time
from motor_control import DriveMotor
from steering_control import SteeringServo # <-- IMPORT THE NEW MODULE
from communication import WifiServer

# --- Configuration ---
WIFI_SSID = "ROMER_MESH"
WIFI_PASSWORD = "K0van1231"
MOTOR_PIN = 15  # GPIO pin for the drive motor
SERVO_PIN = 16  # GPIO pin for the steering servo

# --- Initialization ---
motor = DriveMotor(MOTOR_PIN)
servo = SteeringServo(SERVO_PIN) # <-- INITIALIZE THE SERVO
server = WifiServer(WIFI_SSID, WIFI_PASSWORD)
server.start_server()

print("Application started. Waiting for commands...")

target_speed = 0
current_speed = 0
ACCELERATION_RATE = 5

# --- Main Loop ---
while True:
    command = server.get_latest_command()

    # Update target speed based on command
    if command == "UP":
        target_speed = 100 # Target 100% speed
    elif command == "DOWN":
        target_speed = -100
    else: # STOP, CENTER, etc.
        target_speed = 0

    # --- Acceleration Ramping Logic ---
    if current_speed < target_speed:
        current_speed += ACCELERATION_RATE
        if current_speed > target_speed:
            current_speed = target_speed # Don't overshoot
    elif current_speed > target_speed:
        current_speed -= ACCELERATION_RATE
        if current_speed < target_speed:
            current_speed = target_speed # Don't overshoot

    motor.set_speed(current_speed)
    
    # ... handle steering ...
    time.sleep(0.02)

    # Steering Servo Control
    if command == "LEFT":
        servo.set_angle(-45) # Steer 45 degrees left
    elif command == "RIGHT":
        servo.set_angle(45)  # Steer 45 degrees right
    elif command == "CENTER":
        servo.center() # Straighten the wheel

    time.sleep(0.05) # Loop runs 20 times per second