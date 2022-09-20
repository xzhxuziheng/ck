"""
coder: xuziheng
date: 2022/9/20 9:23
"""
# 可以在多个进程之间通信（可以给多个进程来用）
from multiprocessing import Queue
import requests


def work():
    while q2.qsize() > 0:
        url = q2.get()
        requests.get(url=url)


if __name__ == '__main__':
    q2 = Queue()
    for i in range(10):
        q2.put('')

