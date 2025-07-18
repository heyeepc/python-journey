#在寒冷的天气里有风时，空气感觉比实际更冷，因为空气的流动增加了温暖物体（比如人）的冷却速度，这种效应称为风寒。
#2001年，加拿大、英国和美国采用了如下公式来计算风寒指数。式中Ta为气温，单位为摄氏度：V为风速，单位为千米/小时。类似的公式可以用不同的恒定值来表示华氏温度和风速（英里/小时）。
T = float(input("温度"))
V = float(input("风速"))
wcl = 13.12 + 0.6215 * T - 11.3 * (V**0.16) + 0.3965 * T * (V**0.16)
print(f"风寒指数{wcl:.2f}")
