# 打印在同一行，模拟进度条
print("Loading", end='...')
print(" Done!")
# 输出: Loading... Done!

# 打印在同一行，不换行
for i in range(3):
    print(i, end=' ')
# 输出: 0 1 2
