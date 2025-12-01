import os

# 1. 创建文件对象
a = open("date.txt", mode='r')

# 2. 读取文件**所有内容**到一个新的变量
file_content = a.read()

# 3. 打印文件内容
print(file_content)

# 4. 关闭文件 (非常重要!)
a.close()

# 推荐使用 with 语句，它会自动处理文件的关闭
# with open("date.txt", mode='r') as a:
#     file_content = a.read()
#     print(file_content)
