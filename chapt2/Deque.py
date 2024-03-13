from collections import deque
# maxlen is an optional parameter, once selected can't be changed
dq = deque(range(10), maxlen=10)
print(dq)
# rotate elements from back to front
dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
# append to head
dq.appendleft(-1)
print(dq)
# extend the deque using a list
dq.extend([11, 22, 33])
print(dq)
# if exceeding the maxlen, the elements in the front will be deserted
dq.extend([10, 20, 30, 40])
print(dq)

# deque has other methods such as append and popleft
