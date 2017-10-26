#from Components.Camera import Camera
from Components.L298N import L298N
from time import sleep

class GBot:
    # This is a 2 DC motor differential drive with RPi3, webcam, and LM298 motor control

    def __init__(self):
        #self.camera = Camera()
        self.motor_drive = L298N()

    def drive_in_circle_x_seconds(self, seconds):
        self.motor_drive.set_motor_A_dir(L298N.FORWARD)
        self.motor_drive.set_motor_B_dir(L298N.FORWARD)
        self.motor_drive.set_motor_A_pwm(50)
        self.motor_drive.set_motor_B_pwm(25)
        print("DRIVE IN CIRCLE")
        sleep(seconds)

    def listen_for_commands(self):
        while 1:
            command = input("Enter Command: ")
            if command == "d":
                self.drive_in_circle_x_seconds(5)
            if command == "q":
                break

