"""
coder: xuziheng
date: 2022/9/6 15:21
"""


class Test:

    def __init__(self):
        self.age = 20
        self.name = 'hahaha'

    def __setattr__(self, key, value):
        if key == 'age':
            # 禁止修改属性值
            super().__setattr__(key, 20)
        elif key == 'name':
            super().__setattr__(key, 'hahaha')
        else:
            super().__setattr__(key, value)


t = Test()
t.age = 30
t.name = 'hahaha'
print(t.name)
print(t.age)
