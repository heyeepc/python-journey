from itertools import accumulate

data = [1, 2, 3, 4]
result = list(accumulate(data))  #list是累加
print(result)  # 输出: [1， 3, 6, 10]
