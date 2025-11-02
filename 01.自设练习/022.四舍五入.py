import math
def round_half_up(n):
    return math.floor(n + 0.5)

print(round_half_up(2.4))  # 2
print(round_half_up(3.5))  # 4
