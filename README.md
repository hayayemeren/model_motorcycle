# Project: Self-Balancing Model Motorcycle

A multi-phase plan to build a self-balancing, and eventually autonomous, model motorcycle.

---

## Phase 1: Parts & Materials

### Initial Build Components

- [x]  **Microcontroller:** Raspberry Pi Pico W
- [x]  **Main Battery:** Makita 18V
- [x]  **Voltage Regulator:** 5V BEC (Battery Eliminator Circuit) or Buck Converter

### Components to Upgrade the System

- [ ]  **Upgraded Battery:** 6S (22.2V) LiPo Battery
- [ ]  **Balance Sensor:** MPU-6050 Inertial Measurement Unit (IMU)
- [ ]  **Control System:** RC Transmitter & Receiver (For reliable, low-latency control)
- [ ]  **Advanced Sensors:** LiDAR, Camera Module (For autonomy)
- [ ]  **Advanced CPU:** Raspberry Pi 4/5 (For autonomous navigation processing)
- [ ]  **Controller:** Physical Joystick (For a tactile PC-based controller)

---

## Phase 2: Initial Build & Control (Non-Balancing)

The goal of this phase is to create a functional, remote-controlled vehicle without the complexity of self-balancing.

- [ ]  **Assemble Core Components:** Mount the Pico W, Makita 18V, BEC, and motors onto the chassis.
- [x]  **Develop Wi-Fi Communication:**
    - [x]  Set up a socket server on the Pico W to listen for commands.
- [x]  **Write Modular Code:**
    - [x]  Create a `MotorControl` module for acceleration and braking.
    - [x]  Create a `SteeringControl` module for the servo.
    - [x]  Create a `Communication` module to handle receiving and parsing Wi-Fi commands.
- [ ]  **Implement "Training Wheels":** Design and attach small, servo-actuated "feet" that can be deployed to keep the bike standing still and retracted when it moves.

---

## Phase 3: Upgrades & Self-Balancing

This is the most challenging phase, focusing on implementing the self-balancing logic.

- [ ]  **Integrate the IMU:** Connect the MPU-6050 to the Pico W and write code to get a stable tilt-angle reading.
- [ ]  **Upgrade the Power System:** Swap to the 6S LiPo battery to provide the necessary power and torque for rapid motor adjustments.
- [ ]  **Implement PID Controller:**
    - [ ]  Write a PID (Proportional-Integral-Derivative) control loop.
    - [ ]  The controller's input will be the tilt angle from the IMU.
    - [ ]  The controller's output will adjust the drive motor's speed to counteract falling.
- [ ]  **(Optional) Design a Custom PCB:** Move the finalized circuit from a breadboard to a custom-designed PCB for a clean, robust, and permanent installation.

---

## Phase 4: Full Autonomy

The long-term goal is to make the motorcycle navigate its environment independently.

- [ ]  **Integrate Advanced Hardware:** Add a Raspberry Pi 4/5 and advanced sensors like LiDAR and a camera.
- [ ]  **Develop Perception:** Write code for the Raspberry Pi to process sensor data to detect obstacles and understand its surroundings (SLAM).
- [ ]  **Develop Path Planning:** Create algorithms for the motorcycle to navigate from one point to another while avoiding obstacles. The Raspberry Pi will send high-level commands (e.g., "turn left," "go forward") to the Pico W.

---

## Extras & Future Ideas

- [ ]  **ROS Integration:** Adapt the software to be compatible with the Robot Operating System (ROS).
- [ ]  **Mechanical Drive System:** Replace the direct drive with a belt or chain system to optimize the gear ratio for better torque or speed.
- [ ]  **Self-Parking Stand:** Evolve the initial "feet" into a fully automated kickstand that deploys when the bike comes to a stop.
