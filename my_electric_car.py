from car import Car
from electric_car import Electric_car


my_tesla = Electric_car('tesla', 'red', 2012)
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()

my_chev = Car('chev', 'brown', 2000)
my_chev.get_descriptive_name()
my_chev.increament_odometer(60)
my_chev.read_odemeter()