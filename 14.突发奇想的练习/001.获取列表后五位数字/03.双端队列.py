from collections import deque

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = list(deque(lst, maxlen=5))

print(result)

