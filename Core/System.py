

class System:

    STATE_START = "start"

    def __init__(self):
        self.state = self.STATE_START
        pass

    def get_current_state(self):
        return self.state

    def start(self):
        pass