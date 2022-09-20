"""
coder: xuziheng
date: 2022/8/29 11:58
"""


def num(fun):
    def func(*args, **kwargs):
        fun(*args, **kwargs)
    return func


@num
def add_num(a, b):
    print(a+b)


# add_num(2, 4)


class MyTest(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod    # 被classmethod装饰后，该方法就是一个类方法
    def add_test(cls):  # cls：代表的是类本身
        print('add_test')

    @staticmethod   # 静态方法 实例和类都可以调用
    def static():
        print('这是个静态方法')

    @property   # 用于设置只读属性
    def read_attr(self):
        print('这个装饰器装饰完了之后，该方法可以像属性一样被调用')
        return 18

    def sub(self):  # self代表的是实例本身
        print('sub中的self:', self)


t = MyTest('xzh', 20)
MyTest.add_test()
MyTest.static()
t.static()
print(t.read_attr)
