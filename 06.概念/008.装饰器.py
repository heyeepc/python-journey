def my_decorator(func):
    def wrapper():
        print("函数执行前")
        func()
        print("函数执行后")
    return wrapper

@my_decorator
def hello():
    print("Hello")

hello()

def decorator(func):
    def wrapper(*args, **kwargs):
        # 可以加任何逻辑
        return func(*args, **kwargs)
    return wrapper
