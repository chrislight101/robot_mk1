# Dummy GPIO when not running on Pi

BOARD = 'board'
BCM = 'broadcom'
OUT = 'output'
IN = 'input'

def cleanup():
    pass

def setmode(mode):
    mode = mode

def setup(pin_num, pin_mode):
    pin_num = pin_num
    pin_mode = pin_mode

def output(pin_num, direction):
    pass

def input(pin_num):
    return True

class PWM:
    def __init__(self,pin, frequency):
        self.pin = pin
        self.frequency = frequency

    def start(self, duty_cycle):
        self.duty_cycle = duty_cycle

    def stop(self):
        pass

    def ChangeFrequency(self, new_frequency):
        self.frequency = new_frequency

    def ChangeDutyCycle(self, new_duty_cycle):
        self.duty_cycle = new_duty_cycle