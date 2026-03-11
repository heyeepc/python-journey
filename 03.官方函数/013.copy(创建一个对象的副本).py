items = [1, 2, 3, 4, 5]
for item in items.copy():
    if item < 3:
        items.remove(item)
print(items)
