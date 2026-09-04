lst = [64, 34, 25, 12, 22, 11, 90, 88, 120, 130]

for i in range(10):
    swapped = False
    for j in range(0,10 - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            swapped = True
    if not swapped:
        break

print(lst)
