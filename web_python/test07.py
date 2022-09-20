"""
coder: xuziheng
date: 2022/9/8 16:44
"""


# 单例模式
class SingleInstance:
    __instance = None
    print('这是instance属性：', __instance)

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            print('新属性的new方法：{}'.format(cls.__instance))
        return cls.__instance


a = SingleInstance()
a.instance = 100
a.age = 10
a.name = 'aaa'
b = SingleInstance()
# b.instance = 'qqq'
# b.age = 9999
# b.name = 'bbb'
print(a.instance)
print(a.age)
print(a.name)
print(b.name)
print(b.age)
print(b.instance)