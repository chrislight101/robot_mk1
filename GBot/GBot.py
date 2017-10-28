from Components.L298N import L298N
from time import sleep
import curses


class GBot:
    # This is a 2 DC motor differential drive with RPi3, webcam, and L298n motor control

    DEFAULT_PWM = 50

    def __init__(self):
        self.stdscr = curses.initscr()

        self.motor_drive = L298N()

    def drive_in_circle_x_seconds(self, seconds):
        self.motor_drive.set_motor_a_dir(L298N.FORWARD)
        self.motor_drive.set_motor_b_dir(L298N.FORWARD)
        self.motor_drive.set_motor_a_pwm(self.DEFAULT_PWM)
        self.motor_drive.set_motor_b_pwm(int(self.DEFAULT_PWM / 2))
        print("DRIVE IN CIRCLE")
        sleep(seconds)

    def drive_forward(self, pwm):
        self.motor_drive.set_motor_a_dir(L298N.FORWARD)
        self.motor_drive.set_motor_b_dir(L298N.FORWARD)
        self.motor_drive.set_motor_a_pwm(pwm)
        self.motor_drive.set_motor_b_pwm(pwm)

    def drive_reverse(self, pwm):
        self.motor_drive.set_motor_a_dir(L298N.REVERSE)
        self.motor_drive.set_motor_b_dir(L298N.REVERSE)
        self.motor_drive.set_motor_a_pwm(pwm)
        self.motor_drive.set_motor_b_pwm(pwm)

    def turn_left(self):
        self.motor_drive.set_motor_a_dir(L298N.REVERSE)
        self.motor_drive.set_motor_b_dir(L298N.FORWARD)
        self.motor_drive.set_motor_a_pwm(self.DEFAULT_PWM)
        self.motor_drive.set_motor_b_pwm(self.DEFAULT_PWM)

    def turn_right(self):
        self.motor_drive.set_motor_a_dir(L298N.FORWARD)
        self.motor_drive.set_motor_b_dir(L298N.REVERSE)
        self.motor_drive.set_motor_a_pwm(self.DEFAULT_PWM)
        self.motor_drive.set_motor_b_pwm(self.DEFAULT_PWM)

    def stop(self):
        self.motor_drive.set_motor_a_pwm(0)
        self.motor_drive.set_motor_b_pwm(0)

    def curses_init(self):
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        self.stdscr.nodelay(True)

    def curses_cleanup(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def parse_command(self,cmd):
        # movement
        if cmd == ord('w'):
            self.drive_forward(self.DEFAULT_PWM)
        elif cmd == ord('a'):
            self.turn_left()
        elif cmd == ord('d'):
            self.turn_right()
        elif cmd == ord('s'):
            self.drive_reverse(self.DEFAULT_PWM)
        elif cmd == ord('r'):
            # start recording images
            pass
        elif cmd == ord('e'):
            # stop recording images
            pass
        elif cmd == ord('q'):
            # shutdown
            return False
        else:
            self.stop()
        sleep(0.05)
        return True

    def main_loop(self):
        self.curses_init()
        c = self.stdscr.getch()
        while self.parse_command(c):
            c = self.stdscr.getch()


        self.curses_cleanup()

if __name__ == '__main__':
    gbot = GBot()
    GBot.main_loop()
