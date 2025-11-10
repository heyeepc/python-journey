
# 用 Leibniz 级数逼近 pi/4：
# pi/4 = 1 - 1/3 + 1/5 - 1/7 + ...

threshold = 1e-6     # 停止条件：两次累加结果的变化小于这个值
s = 0.0              # 当前累加和（代表逼近的 pi/4）
prev_s = 0.0         # 上一次的累加和（用于比较）
n = 0                # 项索引（从 0 开始）
iterations = 0       # 统计实际用了多少项

while True:
    term = (-1) ** n / (2 * n + 1)  # 当前项
    s += term
    iterations += 1

    # 比较这次累加后的和与上一次的和的差
    if abs(s - prev_s) < threshold:
        break

    prev_s = s       # 保存当前和，供下一次比较
    n += 1

pi_approx = 4 * s
print("逼近的 pi 值：", pi_approx)
print("用的项数：", iterations)
print("误差（与 math.pi 比较）：", abs(pi_approx - __import__("math").pi))
