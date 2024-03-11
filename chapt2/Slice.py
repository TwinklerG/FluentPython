# s[a: b: c] to slice between a and b with the interval of c
s = "bicycle"
print(s[::3])

# slice assignment
l = list(range(10))
print(l)
l[2:5] = [20, 30]
print(l)
del l[5:7]
print(l)
l[3::2] = [11, 22]
print(l)
# l[2:5] = 100 is not allowed
l[2:5] = [100]
print(l)

# use + and * to list. Never change the original one. Create a new one instead
l = [1, 2, 3]
print(l * 5)
print(l + l)
