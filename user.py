class UserEnter():
    """will be the infomation for a user portfilo."""
    def __init__(self, first_name, last_name, age, height, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.location = location
        self.login_attempts = 0

    def attempts(self):
        """will print the number of attempts """

        print("Great so the number of attempts right now is " + str(self.login_attempts))


    def increament_login_attempts(self):
        """will add one to every new login attemot"""
        self.login_attempts += 1
        

    def reset_login_attempts(self):
        """will reset the value of attempts to 0 be sure to call attempts()"""
        self.login_attempts = 0
        
    def describe_user(self):
        """Prints all the general infomation"""
        print("Your first name: \t " + self.first_name.title())
        print("Your last name: \t" + self.last_name.title())
        print("You are " + str(self.age) + " years old cool!")
        print("Wow you are " + str(self.height) + " cm tall.")
        print("Loacted: \t" + self.location.title())


    def welcome_mess(self):
        """welcome message to all new users"""
        print("Hey welcome to the home page once again! " + self.first_name.title())





