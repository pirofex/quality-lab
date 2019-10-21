class bootstrapper():
    def create():
        return System(True)

class System():
    def __init__(self, is_available):
        self.is_available = is_available

    def register_user(self, name, password):
        if len(password) >= 5:
            return True

        return False

    def select_type_of_site(self, type):
        types = ["Blog", "Professional", "Business", "Online Store"]

        if type in types:
            return True
        else:
            return False

    def select_name_of_site(self, name):
        if len(name) <= 3:
            return False
        
        return True

    def get_user_page(self):
        return 1

    def create_page(self):
        return True

    def delete_page(self, page):
        pages = [1, 2, 3]

        if page in pages:
            pages.remove(page)
            return True
        
        return False