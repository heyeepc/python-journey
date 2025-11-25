current_user = None  # 模拟未登录状态

def login_required(func):
    def wrapper(*args, **kwargs):
        if not current_user:
            return "请先登录"
        return func(*args, **kwargs)
    return wrapper

@login_required
def dashboard():
    return "欢迎来到管理后台"

print(dashboard())  # 模拟未登录
