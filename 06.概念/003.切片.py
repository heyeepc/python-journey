[start:stop:step]

A. start (起始索引)
作用： 切片开始的位置。切片包含这个索引位置的元素。
默认值： 如果省略，默认从序列的开头（索引 0）开始。负数索引： 
负数表示从末尾开始计数。-1 是最后一个元素，-2 是倒数第二个，依此类推。

B. stop (结束索引)
作用： 切片结束的位置。切片不包含这个索引位置的元素（开区间）。
默认值： 如果省略，默认到序列的末尾结束。
重要原则： 切片操作是左闭右开，即 [start, stop)。

C. step (步长)
作用： 指定在切片过程中，每隔多少个元素取一个。
默认值： 如果省略，默认步长是 1（即连续取下一个元素）。
step = 2：取奇数/偶数位置的元素。
step = -1：反转序列

data = [10, 20, 30, 40, 50, 60, 70, 80]
result_1 = data[2:6]
print(result_1)
result_2 = data[:5]
print(result_2 )
result_3 = data[:-3]
print(result_3)
result_4 = data[::3]
print(result_4)
result_5 = data[::-1]
print(result_5)
result_6 = data[6:1:-2]
print(result_6)
# 从索引 6 (70) 开始，向后每隔 2 个元素取一个，直到索引 1 (20) 之前停止
