print("HELLO".isupper())         # 输出: True
print("Hello".isupper())         # 输出: False (因为存在小写字母 'e', 'l', 'l', 'o')
print("123ABC".isupper())        # 输出: True (数字不影响，只要字母部分全大写)
print("123!@#".isupper())        # 输出: False (字符串中没有可区分大小写的字母字符)

#如果一个字符串中至少包含一个可区分大小写的字符（例如字母），并且所有这类字符都是大写，那么 .isupper()就会返回 True；否则返回 False
