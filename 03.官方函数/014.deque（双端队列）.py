from collections import deque

# 创建一个最多只能存 3 个元素的 deque
history = deque(maxlen=3)

history.append("页面 A")
history.append("页面 B")
history.append("页面 C")
print(history)  # deque(['页面 A', '页面 B', '页面 C'], maxlen=3)

# 再加一个，“页面 A” 会被自动挤掉！
history.append("页面 D")
print(history)  # deque(['页面 B', '页面 C', '页面 D'], maxlen=3)
