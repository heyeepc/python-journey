class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, "w")  # 打开并保存文件对象

    def write(self, text):
        self.file.write(text)

    def close(self):
        self.file.close()
        print("文件已关闭")


f = FileManager("test.txt")
f.write("hello")
f.close()
