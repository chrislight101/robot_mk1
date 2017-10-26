from GBot.GBot import GBot

class System:
    # A top level abstraction for the project

    def __init__(self):
        self.robot = GBot()

    def run(self):
        self.robot.listen_for_commands()
