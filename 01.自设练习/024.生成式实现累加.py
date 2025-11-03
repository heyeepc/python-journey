a = list(range(0,10))
print(a)
b = sum(z for z in a)
print(b)


a = list(range(0, 10))
print(a) # 输出: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 使用 for 循环的一般结构
b = 0 # 初始化一个变量用于累加
for z in a:
    b += z # 将列表 a 中的每个元素 z 累加到变量 b 上
print(b) # 输出: 45
