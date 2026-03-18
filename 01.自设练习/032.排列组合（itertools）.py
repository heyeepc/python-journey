from itertools import permutations

# 从 [1, 2, 3, 4] 中任选 3 个数字进行全排列
for p in permutations([1, 2, 3, 4], 3):
    print(f"{p[0]}{p[1]}{p[2]}")
