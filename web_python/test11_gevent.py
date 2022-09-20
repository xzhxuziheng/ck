"""
coder: xuziheng
date: 2022/9/20 11:02
"""
import time
import gevent
from gevent import monkey
import queue
import requests

monkey.patch_all()


def work1():
    for i in range(50):
        print('---执行work1---第{}次'.format(i+1))
        # gevent.sleep()
        time.sleep(0.001)


def work2():
    for i in range(50):
        print('---执行work2---第{}次'.format(i+1))
        # gevent.sleep()
        time.sleep(0.001)


q = queue.Queue()
for i in range(100):
    q.put('http://httpbin.org/get')


def work3():
    while q.qsize() > 0:
        url = q.get()
        requests.get(url)


st = time.time()
# g1 = gevent.spawn(work1)
# g2 = gevent.spawn(work2)
g3 = gevent.spawn(work3)
g4 = gevent.spawn(work3)
g5 = gevent.spawn(work3)
g6 = gevent.spawn(work3)
g7 = gevent.spawn(work3)
g8 = gevent.spawn(work3)
g9 = gevent.spawn(work3)
g10 = gevent.spawn(work3)
g11 = gevent.spawn(work3)
g12 = gevent.spawn(work3)
g13 = gevent.spawn(work3)
g14 = gevent.spawn(work3)
g15 = gevent.spawn(work3)
g16 = gevent.spawn(work3)
g17 = gevent.spawn(work3)
# g1.join()
# g2.join()
g3.join()
g4.join()
g5.join()
g6.join()
g7.join()
g8.join()
g9.join()
g10.join()
g11.join()
g12.join()
g13.join()
g14.join()
g15.join()
g16.join()
g17.join()
# work1()
# work2()
et = time.time()

print('耗时：{}'.format(et-st))
