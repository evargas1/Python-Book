from car import Car


my_new_car = Car('honda', 'red', 2001)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(50)
my_new_car.read_odemeter()