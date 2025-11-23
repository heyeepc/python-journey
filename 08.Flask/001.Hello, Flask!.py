from flask import Flask

# 1. 创建应用实例
app = Flask(__name__)

# 2. 定义路由和视图函数
@app.route('/')
def index():
    return 'Hello, Flask!'

# 3. 启动开发服务器
if __name__ == '__main__':
    app.run()
