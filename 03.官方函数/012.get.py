my_dict = {"name": "Alice", "age": 30}
# 当指定的键不存在时，它会返回一个默认值（默认为None）
# 键存在
print(my_dict.get("name")) # 输出: Alice

# 键不存在，返回None (默认)
print(my_dict.get("city")) # 输出: None

# 键不存在，返回自定义默认值
print(my_dict.get("city", "未知")) # 输出: 未知

# 使用中括号会报错
# print(my_dict["city"]) # KeyError: 'city'

语法：dictionary.get(key, default_value)
key：要查找的键。
default_value：如果key不存在，返回这个值；如果省略，则返回None
