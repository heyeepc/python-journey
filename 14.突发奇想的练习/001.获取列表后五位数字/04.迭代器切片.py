from itertools import islice

lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

result = list(islice(lst, 5, None))

print(result)
