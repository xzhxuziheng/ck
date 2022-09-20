"""
coder: xuziheng
date: 2022/8/26 10:54
"""
from functools import partial

# def fibo_fun(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fibo_fun(n-2)+fibo_fun(n-1)


# li = []
# n = int(input('请输入：'))
# for i in range(1, n+1):
#     li.append(fibo_fun(i))
# print(li)

# n = int(input('请输入：'))
# a = 0
# for i in range(1, n+1):
#     a += fibo_fun(i)
# print(a)

# 内置函数 filter
# def fun(n):
#     return n < 10
#
#
# li = [12, 445, 543, 3, 43, 5, 32, 32, 7, 3, 9]
# data = filter(lambda x: x < 10, li)
# print(list(data))
#
# li1 = [lambda i: i for i in range(100) if i % 5 == 0]
# print(li1)
# print(len(li1))

# li1 = [12, 445, 543, 3, 43, 5, 32, 32, 7, 3, 9]
# li2 = [12, 445, 543, 3, 43, 5, 32, 32, 7, 3, 9]
# li3 = [12, 445, 543, 3, 43, 5, 32, 32, 7, 3, 9]
# li4 = [12, 445, 543, 3, 43, 5, 32, 32, 7, 3, 9]
# li5 = [12, 445, 543, 3, 43, 5, 32, 32, 7, 3, 9]
# li6 = [12, 445, 543, 3, 43, 5, 32, 32, 7, 3, 9]
# # , li2, li3, li4, li5, li6
# filter1 = partial(filter, lambda x: x > 5)
# res = filter1(li1)
# print(list(res))


# def fun(mon):
#     if mon == 1 or mon == 2:
#         return 2
#     else:
#         return fun(mon-2)+fun(mon-1)
# print(fun(6))

money = 100
book = 100
con = 0
for a in range(money//5+1):
    for b in range(money//3+1):
        for c in range(101):
            if a*5 + b*3 + c*0.5 <= money and a + b + c == book:
                print(a, b, c)
                con += 1
print(con)
 