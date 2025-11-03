from itertools import accumulate

data = [1, 2, 3, 4]
result = list(accumulate(data))  #list是列表
print(result)  # 输出: [1， 3, 6, 10]

# itertools.accumulate(iterable, func=operator.add, *, initial=None)
# iterable: 需要处理的可迭代对象，如列表、元组等
# func: 一个接收两个参数的函数，用于定义累积操作。默认为加法(operator.add)
# initial: 可选的初始值。如果提供，累积计算将从这个值开始。

data1 = [1, 2, 3, 4]
squared_sum = accumulate(data1, lambda x, y: x + y**2)
# 输出: [1, 5, 14, 30]
