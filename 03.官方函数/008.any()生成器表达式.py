numbers = [1, 5, 12, 8, 3]

# 生成器表达式：(x > 10 for x in numbers) 会产生 (False, False, True, False, False)
result = any(x > 10 for x in numbers)
print(result)  # 输出: True
