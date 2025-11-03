# 示例 1: 列表中包含 True
list1 = [False, False, True, False]
print(any(list1))  # 输出: True (因为有一个 True)

# 示例 2: 所有元素都为 False
list2 = [False, False, False]
print(any(list2))  # 输出: False

# 示例 3: 包含真值和假值
# 在 Python 中，非零数字、非空字符串/列表/元组等都被视为 True（真值）。
# 数字 0、空字符串 ""、空列表 []、None 等被视为 False（假值）。
list3 = [0, '', 5， None, []]
print(any(list3))  # 输出: True (因为 5 是真值)

# 示例 4: 所有元素都为假值
list4 = [0, ''， None, 0.0， ()]
print(any(list4))  # 输出: False

# 示例 5: 空的可迭代对象
list5 = []
print(any(list5))  # 输出: False
