"""
coder: xuziheng
date: 2022/8/30 10:34
"""


class MyTest(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
            return cls.instance
        else:
            return cls.instance

    def __str__(self):
        print('----str----触发了')
        return self.instance

    def __repr__(self):
        print('----repr----被触发了')
        return '<MyClass.object-{}>'.format(self.instance)

    def __call__(self, *args, **kwargs):
        # 对象像函数一样调用的时候触发
        print('---call---')


# t1 = MyTest()
# t2 = MyTest()
# t3 = MyTest()
#
# t1.instance = 'xzh'
# t2.instance = 'hhh'
# t3.name = 'tttttt'
# print(t2.instance)
# print(t1.instance)
# t1.__str__()
# print(t3.name)


class ThisIsCall(object):

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('这是装饰器功能1')
        self.func(*args, **kwargs)
        print('----这是装饰器功能2----')


@ThisIsCall
def test_call():
    print('这是原函数的功能')


test_call()
