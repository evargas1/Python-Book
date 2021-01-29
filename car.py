class Car():
    """This will include infomation about a car"""
    def __init__(self, model, color, year):
        """choosing my main attributes for this function"""
        self.model = model
        self.color = color
        self.year = year
        self.read_od = 0

    def get_descriptive_name(self):
        """Will print a clean line of all the info collected"""
        print("Hey your car is a " +
            self.model.title() + 
            " and its " +
            self.color.title() + 
            ". Relatively new its a " + 
            str(self.year) + 
            " model.")

    def read_odemeter(self):
        """Will print current miles on odometer"""
        print("Your car currently has " + str(self.read_od) + " miles on it.")

    def update_odometer(self, milage):
        """update the milage if its more than current miles"""
        if milage >= self.read_od:
            self.read_od = milage
        else:
            print("You can't roll back an odomter silly")
    
    def increament_odometer(self, miles):
        """will add on any new miles that may be needed. Still need to call read_odemter"""
        # the second variable can be named anything because it depends on the input
        self.read_od += miles





tesla = Car('tesla', 'blue', '2001')
tesla.get_descriptive_name()
tesla.update_odometer(30)
tesla.read_odemeter()
