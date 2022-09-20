"""
coder: xuziheng
date: 2022/9/8 10:55
"""


# 字符串描述器
class CharFiled:
    def __init__(self, max_len=20):
        self.max_len = max_len

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, str):
            if len(value) <= self.max_len:
                self.value = value
            else:
                raise ValueError('字段长度不允许超过{}'.format(self.max_len))
        else:
            raise TypeError('字段只能为字符串')

    def __delete__(self, instance):
        self.value = None


# 模型类
class Model:
    name = CharFiled(max_len=2)


m = Model()
m.name = 111
print(m.name)