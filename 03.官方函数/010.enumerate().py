enumerate(iterable, start=0)

# 查找列表中特定元素的索引
numbers = [10, 20, 30, 40]
for index, num in enumerate(numbers):
    if num == 30:
        print(f"数字30的索引是: {index}")
        break
