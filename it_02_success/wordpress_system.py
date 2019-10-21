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

    def select_type_of_site(self, type):
        types = ["Blog", "Professional", "Business", "Online Store"]
        if type in types:
            return True
        
        return False

    def select_name_of_site(self, name):
        if len(name) > 3:
            return True
        
        return False