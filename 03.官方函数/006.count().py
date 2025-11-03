my_list = ['apple', 'banana', 'cherry', 'apple', 'date', 'apple']

# 统计 'apple' 出现的次数
count_apple = my_list.count('apple')
print(f"列表中 'apple' 出现的次数: {count_apple}")  # 输出: 3

# 统计 'grape' (不存在) 出现的次数
count_grape = my_list.count('grape')
print(f"列表中 'grape' 出现的次数: {count_grape}")  # 输出: 0


my_tuple = (1, 2, 2, 3, 4, 2, 5)

# 统计数字 2 出现的次数
count_two = my_tuple.count(2)
print(f"元组中 2 出现的次数: {count_two}")  # 输出: 3


my_string = "hello world, hello python"

# 统计子字符串 'hello' 出现的次数
count_hello = my_string.count('hello')
print(f"字符串中 'hello' 出现的次数: {count_hello}")  # 输出: 2

# 使用可选参数: 在索引 1 到 15 (不包含 15) 之间统计 'l'
count_l_partial = my_string.count('l', 1, 15)
print(f"在索引 1 到 15 之间 'l' 出现的次数: {count_l_partial}")  # 输出: 3 (在 "ello worl" 中)
