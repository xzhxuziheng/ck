"""
coder: xuziheng
date: 2022/9/20 9:18
"""
import queue
import time
import requests
import threading

# 线程的队列（只能在一个进程中使用）
q = queue.Queue()
for i in range(10):
    q.put('https://test.bike.ledear.cn/api/user/refund-apply/list?page=1&pageSize=10')


def work():
    while q.qsize() > 0:
        url = q.get()
        header = {
            'content-type': 'application/json',
            'area_id': '7',
            'source_type': '3',
            'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb3VyY2VfdHlwZSI6Mywic291cmNlX2lkIjoxMjE4fQ.APKg0vDbJvVqJEiwFBmB73dV_eEOfZX7p87z9HXoIp4'
        }
        requests.get(url=url, headers=header)


def main():
    st = time.time()

    t1 = threading.Thread(target=work)
    t2 = threading.Thread(target=work)
    t3 = threading.Thread(target=work)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    et = time.time()
    print('耗时：{}'.format(et-st))


if __name__ == '__main__':
    main()
