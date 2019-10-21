class bootstrapper():
    def create():
        return System(True)

class System():
    def __init__(self, is_available):
        self.is_available = is_available

    def register_user(self, name, password):
        if len(password) < 5:
            return False

        return True