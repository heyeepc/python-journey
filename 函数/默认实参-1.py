def greet(name="小明"):   # 有默认值的参数，要放在没有默认值参数的后面。
    print(f"你好，{name}！")

greet()          # 不传参数，默认用“小明”
greet("小红")    # 传了参数，就用“小红”

