"""
coder: xuziheng
date: 2022/9/14 15:25
"""
from queue import Queue
import threading
import time


q = Queue()


class ProductThread(threading.Thread):
    def run(self):
        count = 0
        while True:
            if q.qsize() < 50:
                for i in range(200):
                    count += 1
                    goods = '--生产第{}个商品'.format(count)
                    q.put_nowait(goods)
                    print('product:', goods)
            time.sleep(1)


class UseProductThead(threading.Thread):
    def run(self):
        count = 0
        while True:
            if q.qsize() > 10:
                for i in range(3):
                    count += 1
                    use = '--消费第{}个商品'.format(count)
                    q.get_nowait()
                    print('use:', use)
            else:
                time.sleep(2)


p = ProductThread()
p.start()
for i in range(10):
    u = UseProductThead()
    u.start()
