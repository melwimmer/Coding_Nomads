#know the population in 3 years
#current popukation 380,123,456
#one person born every 6 seconds
#one person dies every 12 seconds
#one person immigrates every 40 seconds
year = 3
days = year*360
hours = days*24
minutes = hours*60
seconds = minutes*60


born_3yrs = ((3*360*24*60*60)/6)
dead_3yrs = ((3*360*24*60*60)/12)
immigration = ((3*360*24*60*60)/40)
population = 380123456
population3yrs = (population + born_3yrs + immigration - dead_3yrs)
print(population3yrs) 