km = int(float(input("what is the distance in Km")))
usage = int(float(input("Usage of the car in L/Km")))
price = int(float(input("what is the price per liter of fuel")))

print(f'the price of the trip is {km * usage * price}')
