"""
coder: xuziheng
date: 2022/8/23 14:42
"""

# from collections import namedtuple
#
# stu_info = namedtuple('stu_info', ['name', 'age', 'gender'])
# tu = stu_info('张三', 18, '男')
# print(tu.name)
# print(tu.age)
# print(tu.gender)

# url = ['page{0}'.format(i) for i in range(10)]
# print(url)
# dic = {'page{0}'.format(i): 'data{0}'.format(i) for i in range(10)}
# print(dic)

cook_str = 'BIDUPSOD=GJHG34253G564_GHVjhgj;PSTM=453647653;BAIDUID=IGHJ9869OPLQX;sugstore=0;__cfduid=fghktgeak5677;BD_UPN=13453148;ispeed__lsm=2;BDORZ=BFGHJGYFHYTFGFJHH76098'
print(cook_str.split(';'))
dic1 = {i.split('=')[0]: i.split('=')[1] for i in cook_str.split(';')}
print(dic1)


# def gen():
#     for i in range(1, 5):
#         print('-------------------------------------')
#         se = yield i
#         print(se)
# g = gen()
# print(next(g))
# print(g.send(100))
# print(next(g))