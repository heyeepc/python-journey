class Demo:
    def __init__(self, name):
        self.name = name
        print("初始化:", self.name)

    def __del__(self):
        print("销毁:", self.name)

d = Demo("test")
del d
