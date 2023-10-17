from collections import namedtuple

Geolocation = namedtuple("Geolocation", "name lat lon")

null_island = Geolocation(name="Null Island", lat=0, lon=0)

# Using zero-based indexing
print(null_island[0])  # "Null Island"

# Using dot notation
print(null_island.name)  # "Null Island"

maccu_piccu = Geolocation(name="Maccu Piccu", lat=-13.163108055193145, lon=-72.54496539348477)

maccu_piccu = Geolocation(name="Maccu Piccu", lat=-13.163108055193145, lon=-72.54496539348477)
maccu_piccu_tuple = ("Maccu Piccu", -13.163108055193145, 72.54496539348477)

# Get the latitude from the plain tuple
maccu_piccu_tuple[1]  # -13.163108055193145 - Wait... or was it at index 0? Or index 2? Arrgh!

# Get the latitude from the namedtuple
maccu_piccu.lat  # -13.163108055193145 - Yay!

null_island_dict = null_island._asdict()
null_island_dict["name"] = "Null Island is not an island"

modified_null_island = Geolocation(**null_island_dict)
print(modified_null_island)  # Geolocation(name='Null Island is not an island', lat=0, lon=0)

#Finally, namedtuple has several other useful attributes and methods, 
# such as ._make(), which allows you to create a new namedtuple from an iterable, 
# and ._fields, which returns a tuple containing the field names of the namedtuple.