# 生成 0, 1, 2, 3, 4
for i in range(5):
    print(i, end=' ')
# 打印结果：0 1 2 3 4


# 生成 3, 4, 5, 6
for i in range(3, 7):
    print(i, end=' ')
# 打印结果：3 4 5 6

range(start, stop, step)

# 目标序列：10, 9, 8, 7, 6
# start=10 (包含 10)
# stop=5 (不包含 5，即停止在 6)
# step=-1 (每次减 1)
print("--- 简单的倒数 (10 到 6) ---")
for i in range(10, 5, -1):
    print(i, end=' ')
# 打印结果：10 9 8 7 6

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 生成的索引序列：8, 7, 6, 5, 4, 3, 2, 1, 0
print("\n\n--- range() 生成倒序索引 ---")
for i in range(len(a) - 1, -1, -1):
    print(f"索引 {i} 对应的值是 {a[i]}")
# 打印结果：
# 索引 8 对应的值是 9
# 索引 7 对应的值是 8
# ...
# 索引 0 对应的值是 1
start	len(a) - 1 (即 8)	从最后一个索引开始。
stop	-1	必须停止在 0，所以 stop 要设置为 -1。
step	-1	每次索引减 1。
