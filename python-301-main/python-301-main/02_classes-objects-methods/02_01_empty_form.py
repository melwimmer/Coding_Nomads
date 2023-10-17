# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class Medicine:
    '''models medication instructions for a doctor'''

    def __init__(self, name, strength, days, times):
        self.name = name
        self.strength = strength
        self.days = days
        self.times = times
    
    def __str__(self):
        return f"{self.name} strength {self.strength}, take for {self.days} days, {self.times} times a day"

ib = Medicine("Ibuprofeno", 400, 5, 3)
ty = Medicine("Tylenol", 500, 7, 4)
ins= Medicine("Insulina", 7, 30, 3)

print(ib)




