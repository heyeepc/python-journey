from datetime import timedelta

time_deltas = [timedelta(days=1), timedelta(hours=5), timedelta(minutes=30)]

# 需要使用 start=timedelta() 作为初始值
total_time = sum(time_deltas, timedelta())
print(f"总时间间隔: {total_time}") # 输出: 1 days, 5:30:00
