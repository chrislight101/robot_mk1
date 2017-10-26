try:
    import RPi.GPIO as GPIO
except (RuntimeError, ImportError):
    import Components.MockGPIO as GPIO

class L298N:
    # A class to define the LM298 motor controller module
    #TODO: Can this be changed to not depend on RPi hardware

    MOTOR_A_ENABLE_PIN = 11
    MOTOR_B_ENABLE_PIN = 12

    MOTOR_A_DIR_PINS = 13, 15
    MOTOR_B_DIR_PINS = 16, 18

    PWM_FREQUENCY = 50

    BRAKE = 0
    FORWARD = 1
    REVERSE = 2

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        # motor 1 pins
        GPIO.setup(self.MOTOR_A_ENABLE_PIN, GPIO.OUT)  # A PWM
        GPIO.setup(self.MOTOR_A_DIR_PINS[0], GPIO.OUT)
        GPIO.setup(self.MOTOR_A_DIR_PINS[1], GPIO.OUT)
        self.motor_a_pwm = GPIO.PWM(self.MOTOR_A_ENABLE_PIN, self.PWM_FREQUENCY)
        # motor 2 pins
        GPIO.setup(self.MOTOR_B_ENABLE_PIN, GPIO.OUT)  # B PWM
        GPIO.setup(self.MOTOR_B_DIR_PINS[0], GPIO.OUT)
        GPIO.setup(self.MOTOR_B_DIR_PINS[1], GPIO.OUT)
        self.motor_b_pwm = GPIO.PWM(self.MOTOR_B_ENABLE_PIN, self.PWM_FREQUENCY)

        self.motor_a_pwm.start(0)
        self.motor_b_pwm.start(0)


    def set_motor_A_pwm(self, pwm):
        self.motor_a_pwm.ChangeDutyCycle(pwm)

    def set_motor_B_pwm(self, pwm):
        self.motor_b_pwm.ChangeDutyCycle(pwm)

    def set_motor_A_dir(self, dir):
        if dir == self.FORWARD:
            GPIO.output(self.MOTOR_A_DIR_PINS[0], 0)
            GPIO.output(self.MOTOR_A_DIR_PINS[1], 1)
        elif dir == self.REVERSE:
            GPIO.output(self.MOTOR_A_DIR_PINS[0], 1)
            GPIO.output(self.MOTOR_A_DIR_PINS[1], 0)
        elif dir == self.BRAKE:
            GPIO.output(self.MOTOR_A_DIR_PINS[0], 1)
            GPIO.output(self.MOTOR_A_DIR_PINS[1], 1)

    def set_motor_B_dir(self, dir):
        if dir == self.FORWARD:
            GPIO.output(self.MOTOR_B_DIR_PINS[0], 0)
            GPIO.output(self.MOTOR_B_DIR_PINS[1], 1)
        elif dir == self.REVERSE:
            GPIO.output(self.MOTOR_B_DIR_PINS[0], 1)
            GPIO.output(self.MOTOR_B_DIR_PINS[1], 0)
        elif dir == self.BRAKE:
            GPIO.output(self.MOTOR_B_DIR_PINS[0], 1)
            GPIO.output(self.MOTOR_B_DIR_PINS[1], 1)