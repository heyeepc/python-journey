enumerate(iterable, start=0)

# 查找列表中特定元素的索引
numbers = [10, 20, 30, 40]
for index, num in enumerate(numbers):
    if num == 30:
        print(f"数字30的索引是: {index}")
        break

my_list = ['A', 'B', 'C']
for index, item in my_list:  # 直接解包获取索引和值
    print(f"索引 {index}: 元素 {item}")

# 输出：
# 索引 0: 元素 A
# 索引 1: 元素 B
# 索引 2: 元素 C
