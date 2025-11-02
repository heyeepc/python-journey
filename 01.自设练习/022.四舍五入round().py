x = 3.14159
print(round(x, 2))   # 保留 2 位小数 → 3.14
print(round(x))      # 四舍五入到整数 → 3

round() 遵循“银行家舍入法”（即“四舍六入五取偶”），当小数部分正好是 0.5 时，会取最近的偶数。

print(round(2.5))  # 输出 2
print(round(3.5))  # 输出 4

