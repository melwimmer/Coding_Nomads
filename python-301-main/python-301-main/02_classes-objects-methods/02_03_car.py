# The classic OOP example: Write a class to model a car. The class should:
#
# 1. Set the attributes model, year, and max_speed in the `__init__()` method.
# 2. Have a method that increases the `max_speed` of the car by 5 when called.
# 3. Have a method that prints the details of the car.
#
# Create at least two different objects of this `Car()` class and demonstrate
# changing the objects' attributes.

class Car():
    def __init__(self,make, model, year, max_speed):
            self.make = make
            self.model = model
            self.year = year
            self.max_speed = max_speed   
    
    def speed_change(self):
            """Increases the max speed by 5."""
            print(f"Max speed has been increased by 5")
            self.max_speed += 5

    def __str__(self):
           return(f'This is a {self.year} {self.make}, model {self.model}, with a max speed of {self.max_speed}')
    

honda = Car("Honda", "AAA", 2007, 130)
bmw = Car("BMW", "X5", 2019, 300)

print(honda)

bmw.speed_change()

print(bmw)
           
    

