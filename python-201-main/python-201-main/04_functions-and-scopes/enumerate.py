locations = ["cr", "spain", "france", "brazil"]

# for index, country in enumerate(locations, start=1):
#     print(f'*{index}: {country}')


# counter = 0

def my_enumerate(countrylist):
    counter = 0
    tuples=""
    for i in countrylist:
        tuples += (f'*{counter}: {i}') 
        counter += 1
    return(tuples)
    
print(my_enumerate(locations))



