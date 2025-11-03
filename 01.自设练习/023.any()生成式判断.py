numbers_a = [1, 3, 5, 7, 9]
numbers_b = [2, 4, 1, 3]

# 修正：判断 z 是否是偶数 (z % 2 == 0)
result_a = any(z % 2 == 0 for z in numbers_a)
print(f"numbers_a 结果 (应为 False): {result_a}")

# 修正：判断 z 是否是偶数
result_b = any(z % 2 == 0 for z in numbers_b)
print(f"numbers_b 结果 (应为 True): {result_b}")
