# numpy was installed. It is not a part of STL
import numpy
# new an array from 0 to 11
a = numpy.arange(12)
print(a)
print(type(a))
# check the dimension
print(a.shape)
# change the dimension
a.shape = 3, 4
print(a)
print(a[2])
print(a[2, 1])
# select a col
print(a[:, 1])
# change row with col
print(a.transpose())

# import high precision and performance time recorder
from time import perf_counter as pc
t0 = pc()
print(121335435355345345*12312312434234123123123)
print(pc() - t0)

