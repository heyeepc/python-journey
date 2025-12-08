a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1.倒序切片法
print(a[::-1])

# 2.列表推导式
b = [x for x in reversed(a)]
print(b)

# 3.循环
for z in range(len(a)-1, -1, -1):
    print(z)

