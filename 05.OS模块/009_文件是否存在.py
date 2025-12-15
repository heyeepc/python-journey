import os

file_path = "example.txt"
if os.path.exists(file_path):
    print(f"文件或目录 '{file_path}' 存在。")
else:
    print(f"文件或目录 '{file_path}' 不存在。")
