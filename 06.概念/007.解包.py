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

# 示例
student_scores = {'Alice': 95, 'Bob': 88, 'Charlie': 92}

# 字典的 .items() 方法会返回一个由 (键, 值) 元组组成的序列。
# 每次循环 item 是 ('Alice', 95)，然后解包给 name 和 score
for name, score in student_scores.items():
    print(f"{name} 的分数是 {score} 分")

# 输出:
# Alice 的分数是 95 分
# Bob 的分数是 88 分
# Charlie 的分数是 92 分

# 示例：一个包含 (姓名, 年龄, 职位) 信息的列表
employees = [
    ('John', 30, 'Manager'),
    ('Sara', 24, 'Engineer'),
    ('Mike', 45, 'Director')
]

# 每次循环 item 是 ('John', 30, 'Manager')，然后解包给 name, age, title
for name, age, title in employees:
    # 注意这里使用了 f-string 格式化输出
    print(f"{name} ({age}岁) 的职位是 {title}")

# 输出:
# John (30岁) 的职位是 Manager
# Sara (24岁) 的职位是 Engineer
# Mike (45岁) 的职位是 Director
