from car import Car


class Battery():
    """Intialize a new class to model an electrics cars battery"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """will print statement with the current battery size"""
        print("The battery size is " + str(self.battery_size) + "-kwh.")

    def get_range(self):
        """will print average mph depending on battery size"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = ("This car can go approximatly " + str(range) + " miles per hour!")  
        print(message) 

    def upgrade_battery(self):
        """set capacity to 85"""
        self.battery_size = 85 


class Electric_car(Car):
    """Intialize a sub class for car that should inherit all the same propeteries"""
    def __init__(self, model, color, year):
        """will print the infomation about a car"""
        super().__init__(model, color, year)
        self.battery = Battery()
    
        # when an attribute is added here it will always need a default value to function properly.

    def fill_gas_tank(self):
        """will print message this car does not have a gas tank"""
        print("Silly electric cars don't have a gas tank")