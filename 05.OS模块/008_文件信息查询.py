import os

def file_info(path):
    if not os.path.exists(path):
        print(f"'{path}' 不存在")
        return

    print(f"'{path}' 存在")

    if os.path.isfile(path):
        print("类型：文件")
        print(f"大小：{os.path.getsize(path)} 字节")

        _, ext = os.path.splitext(path)
        print(f"扩展名：{ext}")

        dir_path = os.path.dirname(path)
        if dir_path == "":
            dir_path = os.getcwd()
        print(f"所在目录：{dir_path}")
    else:
        print("不是一个文件（可能是目录）")

file_info("date.txt")
