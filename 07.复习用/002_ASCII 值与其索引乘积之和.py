# 计算字符串 'PYTHON' 中所有字符的 ASCII 值与其 索引 的乘积之和
s = 'PYTHON'
total = 0
for index, char in enumerate(s):
    total += ord(char) * index
print("乘积之和:", total)  # 输出: 1179
