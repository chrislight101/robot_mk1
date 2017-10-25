from Components.Camera import Camera
from Components.L298N import L298N

class GBot:
    # This is a 2 DC motor differential drive with RPi3, webcam, and LM298 motor control

    def __init__(self):
        self.camera = Camera()
        self.motor_drive = L298N()

    def drive_in_circle(self):
        self.motor_drive.set_motor_A_dir(L298N.FORWARD)
        self.motor_drive.set_motor_B_dir(L298N.FORWARD)

        self.motor_drive.set_motor_A_pwm(10)
        self.motor_drive.set_motor_B_pwm(5)
        pass


