fruits = ['grapes', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
# reversed method
print(sorted(fruits, reverse=True))
# sort by the len(if same, place as the original)
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(fruits)
fruits.sort()
print(fruits)
