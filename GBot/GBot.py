from Components.Camera import Camera
from Components.LM298 import LM298

class GBot:
    # This is a 2 DC motor differential drive with RPi3, webcam, and LM298 motor control

    def __init__(self):
        self.camera = Camera()
        self.motor_drive = LM298()

    def drive_in_circle(self):
        self.motor_drive.set_motor_A_dir(LM298.FORWARD)
        self.motor_drive.set_motor_B_dir(LM298.FORWARD)

        self.motor_drive.set_motor_A_pwm(10)
        self.motor_drive.set_motor_B_pwm(5)
        pass


