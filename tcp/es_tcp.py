"""
coder: xuziheng
date: 2022/9/29 20:10
"""
import random


class EsTcp:

    def __init__(self, data):
        self.data = data

    def es_tcp_alarm(self):
        head = 'AA55'
        _cmd = '05'
        num = str(hex(random.randint(1, 255)))[2:].upper()
        _len = '0001'
        cmd_type = self.data
        cmd_alarm = head + _cmd + num + _len + cmd_type
        return cmd_alarm


# print(EsTcp('01').es_tcp_alarm())
