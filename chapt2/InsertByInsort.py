import bisect
import random

SIZE = 7
# initialize the random generator
random.seed(1729)

my_list = []
for i in range(SIZE):
    # randrange(start, stop[, step]) generate a random element between start and stop by step
    new_item = random.randrange(SIZE*2)
    # insort(seq, item) insert item into seq and keep seq up
    bisect.insort(my_list, new_item)
    print('%2d ->' % new_item, my_list)

