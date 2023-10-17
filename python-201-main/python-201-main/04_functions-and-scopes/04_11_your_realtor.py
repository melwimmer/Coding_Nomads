# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def readv(livingtype, rentorpurchase, number, **kwargs): 
    Listofamenities = ""
    
    for amenity, ammount in kwargs.items(): 
        Listofamenities += amenity + ammount + "\n"
    
    Text = f"""
A new {livingtype} has been published for {rentorpurchase}.
The {livingtype} has the following ammenities:
{Listofamenities}
Call {number} for more info!
     """
    return(Text)

print(readv("house", "rent", "86975199", bedrooms = ": 3", bathrooms = ": 4", garden =": yes", others = ": Pet friendly"))