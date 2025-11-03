my_list = ['apple', 'banana', 'cherry', 'apple', 'date', 'apple']

# 统计 'apple' 出现的次数
count_apple = my_list.count('apple')
print(f"列表中 'apple' 出现的次数: {count_apple}")  # 输出: 3

# 统计 'grape' (不存在) 出现的次数
count_grape = my_list.count('grape')
print(f"列表中 'grape' 出现的次数: {count_grape}")  # 输出: 0
