from GBot.GBot import GBot


class System:
    # A top level abstraction for the project

    def __init__(self):
        self.gbot = GBot()

    def run(self):
        self.gbot.main_loop()


if __name__ == '__main__':
    system = System()
    system.run()
