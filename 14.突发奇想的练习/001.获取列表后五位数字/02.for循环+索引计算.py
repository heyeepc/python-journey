lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

a = len(lst) - 5
b = [lst[i] for i in range(a,len(lst))]

print(b)
