k = 0.1
T = 100
Ta = 25

while abs(T - Ta) > 0.01:
    T = T - k * (T - Ta)   # 更新温度
    print(T)
