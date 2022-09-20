"""
coder: xuziheng
date: 2022/9/13 10:31
"""

import threading
import time

count = 0


def func1():
    global count
    for i in range(10000000):
        # print('------func1 running------')
        # mate.acquire()
        count += 1
        # mate.release()
    # print('func1:', count)


def func2():
    global count
    for i in range(10000000):
        # print('--------func2 running------')
        # mate.acquire()
        count += 1
        # mate.release()
    # print('func2:', count)


# mate = threading.Lock()
# th1 = threading.Thread(target=func1, name='Threading func1')
# th2 = threading.Thread(target=func2, name='Threading func2')
# s_time = time.time()
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# e_time = time.time()
# print('threading run time:', e_time-s_time)
# print(count)
s_time = time.time()
func1()
func2()
e_time = time.time()
print('threading run time:', e_time-s_time)
print(count)
