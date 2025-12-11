import os

def create_folder(name):
    os.makedirs(name, exist_ok=True)
    print(f"已创建或已存在：{name}")
