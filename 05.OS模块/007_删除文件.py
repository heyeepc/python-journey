import os

def delete_file(path):
    if os.path.isfile(path):
        try:
            os.remove(path)
            print("删除成功")
        except Exception as e:
            print("删除时发生错误：", e)
    else:
        print("文件不存在")

# 示例调用
delete_file("test.txt")
