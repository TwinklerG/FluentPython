colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tShirts = [(color, size) for color in colors for size in sizes]
print(tShirts)
tShirts = [(color, size) for size in sizes for color in colors]
print(tShirts)
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt, end="|")