# Create two classes that model a rectangle and a circle.
# The rectangle class should be constructed by length and width
# while the circle class should be constructed by radius.
#
# Write methods in the appropriate class so that you can calculate
# the area of both the rectangle and the circle, the perimeter
# of the rectangle, and the circumference of the circle.


class Triangle():
    def __init__(self, base, altura, hipotenusa, side2):
        self.base = base
        self.altura = altura
        self.hipotenusa = hipotenusa
        self.side2 = side2

    def perimeter(self):
        perimeter = self.base + self.hipotenusa + self.side2 
        print(f'The perimeter of your triangle is {perimeter}')

    def area(self):
        area = self.base * self.altura
        print(f'The area of your triangle is {area}')

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def perimeterc(self):
        perimeterc = 2*3.14*self.radius
        print(f'The perimeter of your circle is {perimeterc}')

    def areac(self):
        areac = 3.14*(self.radius**2)
        print(f'The a area of your circle is {areac}')


    
