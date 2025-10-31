list_of_lists = [[1, 2], [3, 4], [5, 6]]

# 错误用法: 默认 start=0 会报错
# sum(list_of_lists) # TypeError: unsupported operand type(s) for +: 'int' and 'list'

# 正确用法: 使用 start=[] 作为初始值
flattened_list = sum(list_of_lists, [])
# 相当于 [] + [1, 2] + [3, 4] + [5, 6]
print(f"扁平化列表: {flattened_list}") # 输出: [1, 2, 3, 4, 5, 6]
