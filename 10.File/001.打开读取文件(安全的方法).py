# 推荐的做法
with open("filename.txt", mode='r') as f:
    # 在这里进行文件读取/写入操作
    content = f.read()
    print(content)

# 当代码执行到这里时，文件 f 已经被自动关闭了，即使 f.read() 抛出了异常。
