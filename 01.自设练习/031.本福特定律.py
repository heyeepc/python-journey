def leading_digit(n):
    """返回一个正数的首位数字"""
    n = abs(n)
    while n >= 10:
        n //= 10
    return int(n)

def benford_count(data):
    """统计数据的首位数字分布"""
    count = {i: 0 for i in range(1, 10)}
    for num in data:
        if num == 0:
            continue
        d = leading_digit(num)
        count[d] += 1
    return count

# 示例数据
data = [123, 456, 789, 1024, 512, 2048, 999, 321, 345, 678, 111, 100, 200]

result = benford_count(data)
print(result)
