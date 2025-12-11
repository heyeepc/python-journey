import os

def create_folder(name):
    try:
        os.mkdir(name)
        print(f"已创建目录：{name}")
    except FileExistsError:
        print(f"目录已存在：{name}")

