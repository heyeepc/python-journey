numbers = [1, 5, 12, 8, 3]

# 生成器表达式：(x > 10 for x in numbers) 会产生 (False, False, True, False, False)
result = any(x > 10 for x in numbers)
print(result)  # 输出: True


s = "helloWorld"
# 检查每个字符是否为大写，然后 any() 检查结果
result = any(char.isupper() for char in s)
print(result)  # 输出: True (因为 'W' 是大写)
