# 示例
my_list = ['red', 'green', 'blue']

# 每次迭代会产生一个 (索引, 值) 的元组，然后解包给 i 和 v
# 每次循环 item 是 (0, 'red')，然后解包给 i 和 color
for i, color in enumerate(my_list):
    print(f"位置 {i+1}: 颜色 {color}")

# 输出:
# 位置 1: 颜色 red
# 位置 2: 颜色 green
# 位置 3: 颜色 blue
