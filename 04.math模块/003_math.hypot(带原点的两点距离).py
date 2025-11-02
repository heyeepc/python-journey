import math

x1 = input("x1: ")
if x1 == "":
    print("未输入任何点。")
    exit()

y1 = input("y1: ")
if y1 == "":
    print("未输入任何点。")
    exit()

x = float(x1)
y = float(y1)

z = math.hypot(x,y)

print(z)
