symbols = "$%$##@!"
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# another way using list comprehension(listcomps)
symbols = "$%$##@!"
codes = [ord(symbol) for symbol in symbols]
print(codes)

# another way using filter and map
symbols = "$%$##@!"
codes = list(filter(lambda c: c > 35, map(ord, symbols)))
print(codes)
