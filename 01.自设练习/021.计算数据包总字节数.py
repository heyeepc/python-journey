# 模拟网络会话中的数据包列表
# 每个元组代表一个数据包：(数据包ID, 字节大小, 协议类型)
packets = [
    (1, 1500, "TCP"),
    (2, 64, "ARP"),
    (3, 1500, "TCP"),
    (4, 500, "UDP"),
    (5, 64, "ICMP"),
    (6, 1500, "TCP")
]

# 假设我们只关心 TCP 协议的数据包的总字节数

# 直接在 sum() 中使用生成器表达式
# 语法特点：生成器表达式外层不需要额外的圆括号 (因为 sum() 已经提供了圆括号)
total_tcp_bytes_generator = sum(
    size
    for id, size, proto in packets
    if proto == "TCP" # 过滤条件：只计算 TCP 协议的
)

print("-" * 20)
print(f"总字节数 (生成器表达式): {total_tcp_bytes_generator}")
# 结果: 4500
