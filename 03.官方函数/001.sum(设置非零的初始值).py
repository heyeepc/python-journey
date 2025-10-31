sum(iterable, [start])

可以用 start 参数来指定一个非 0 的起始累加值

numbers = [1, 2, 3]

# 默认用法 (start=0)
result_default = sum(numbers)
# 相当于 0 + 1 + 2 + 3 = 6
print(f"默认求和: {result_default}") # 输出: 6

# 使用 start=100
result_with_start = sum(numbers, 100)
# 相当于 100 + 1 + 2 + 3 = 106
print(f"设置初始值求和: {result_with_start}") # 输出: 106

