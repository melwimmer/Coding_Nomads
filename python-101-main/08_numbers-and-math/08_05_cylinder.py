# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.
#volume = pi r^2 h
#surface area = 2 pi r h + 2 pi r^2
radius = 3.14
height = 5
pi = 3.14
volume = pi*(radius ** 2)*height
surface_area = (2*pi*radius*height) + (2*pi*(radius**2))
print(volume)
print(surface_area)
