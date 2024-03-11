from collections import namedtuple
# two parameters: one for typename, another for field_names
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)
# you can get by field_name or place
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

# properties and methods
# a tuple contains all field names
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# _make accepts an iterable object to generate an instance for it
# similar to City(*delhi_data)
delhi = City._make(delhi_data)
# _asdict returns a namedtuple in the form of collections.OrdereDict
print(delhi._asdict())
for key, value in delhi._asdict().items():
    print(key + ":",value)
