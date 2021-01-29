from user import UserEnter

class Privileges():
    """will peform one function for the admin, printing his privelages"""
    def __init__(self):
        self.privel_list = ['can add post', 'can block user', 'can delete post']


    def show_privelages(self):
        for p in self.privel_list:
            print("As the admin you can: \t" + p.title())



class Admin(UserEnter):
    """specila class for admin subclass """
    def __init__(self, first_name, last_name, age, height, location):

        super().__init__(first_name, last_name, age, height, location)
        self.privel = Privileges()