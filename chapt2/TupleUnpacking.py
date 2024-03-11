print(divmod(20, 8))
t = (20, 8)
# * can unpack an iterable object as a parameter for a function
print(divmod(*t))

# os.path.split() returns a tuple of path and last_part
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)
print(os.path.split('/home/luciano/.ssh/idrsa.pub'))

# use * to process rest elements
a, b, *rest = range(5)
print(a, b, rest)
# * can only decorate an element and can appear anywhere
a, *body, b, c = range(5)
print(a, body, b, c)
