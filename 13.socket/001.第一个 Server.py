import socket

# 1. 创建 Socket (买手机)
# AF_INET = 使用 IPv4 网络
# SOCK_STREAM = 使用 TCP 协议
server_ptr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. 绑定地址 (办卡)
# '127.0.0.1' 是回环地址，代表你自己的电脑
# 8888 是端口号，就像房间号
server_ptr.bind(('127.0.0.1', 8888))

# 3. 开始监听 (手机开机)
# 5 代表允许排队的最大人数
server_ptr.listen(5)
print("--- 服务器已启动，正在 8888 端口等待连接 ---")

# 4. 阻塞式等待 (盯着手机看，等它响)
# 程序运行到这里会“停住”，直到有人连接进来
conn, addr = server_ptr.accept()

print(f"--- 报告！有人连进来了，对方地址是: {addr} ---")

# ⚠️ 暂时不写聊天代码，先测试连接
conn.close()
server_ptr.close()

运行程序： 在 PyCharm 中点击绿色三角形运行 server.py。你会发现控制台显示“正在等待连接...”，并且程序没有结束（那个小红方块一直亮着）。

打开 CMD： 按下 Win + R，输入 cmd 并回车。

模拟拨号： 在黑窗口中输入以下命令并回车：

telnet 127.0.0.1 8888
