"""
coder: xuziheng
date: 2022/8/29 11:30
"""


def login(func):
    def fun():
        username = 'test'
        password = '123456'
        user = input('请输入用户名：')
        pw = input('请输入密码：')
        if username == user and password == pw:
            func()
        else:
            print('账号或密码错误')
    return fun


# @login  # @login：语法糖 --> index = login(index)
def index():
    print('---------欢迎进入首页---------')


index = login(index)
index()
