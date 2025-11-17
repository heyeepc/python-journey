# 示例
my_list = ['red', 'green', 'blue']

# 每次迭代会产生一个 (索引, 值) 的元组，然后解包给 i 和 v
# 每次循环 item 是 (0, 'red')，然后解包给 i 和 color
for i, color in enumerate(my_list):
    print(f"位置 {i+1}: 颜色 {color}")

# 输出:
# 位置 1: 颜色 red
# 位置 2: 颜色 green
# 位置 3: 颜色 blue
scores_data = [
    ["小明", 80, 90],
    ["小红", 75, 85],
    ["小刚", 95, 70]
]


for name, chinese, math in scores_data:
     print(f"{name}总成绩{chinese + math}")

goods_prices = {
    "Laptop": 5000,
    "Mouse": 150,
    "Keyboard": 300
}

for a,b in goods_prices.items():
    print(f"{a}的价格是{b*1.1}")

data_list = [10, 20, 30, 42, 50, 42, 60]
target = 42

for index, value in enumerate(data_list):
    if value == target:
        # 如果找到了，打印结果
        print(f"数字 {target} 第一次出现在索引 {index} (即第 {index + 1} 位)")

        # *** 关键步骤：使用 break 停止循环 ***
        # 因为题目要求是“第一次出现的位置”，一旦找到就应该停止查找，
        # 否则循环会继续检查后面的元素（比如第二个 42）。
        break

