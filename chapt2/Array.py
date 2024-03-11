from array import array
from random import random

floats = array('d', (random() for i in range(10**7)))
print(floats[-1])

# write the array to a file
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()

# read data from a file
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
print(floats2[-1])
print(floats2 == floats)

nums = array('d', (1, 3, 2, 5, 4, 2))
print(nums)
# to sort an array
nums = array(nums.typecode, sorted(nums))
print(nums)
