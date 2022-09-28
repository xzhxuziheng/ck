"""
coder: xuziheng
date: 2022/9/28 17:42
"""

import socket
import time


class TcpClient:

    def __init__(self, address, port, data):
        self.address = address
        self.port = port
        self.data = data

    def tcp_client(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((self.address, self.port))
        tcp_data = bytes.fromhex(self.data)
        client.send(tcp_data)
        info = client.recv(1024)
        print(info.hex().upper())
        client.close()
        return info.hex().upper()


if __name__ == '__main__':
    address = '110.191.179.145'
    port = 10101
    data = 'AA 55 23 c7 00 23 00 1E 09 04 64 38 36 36 32 31 35 30 35 30 31 30 34 39 34 39 34 36 30 30 38 31 39 35 36 38 30 35 38 38 38'
    # data = 'aa 55 29 6f 00 1b 00 30 1f 00 00 00 f0 5c 4a a7 16 94 db e4 42 23 06 f4 41 00 00 00 29 5c af 3f 05'
    tcp = TcpClient(address, port, data)
    tcp_info = tcp.tcp_client()
    msg = tcp_info[12:]
    print(msg)
    msg_int = int(msg, 16)
    print(msg_int)
    timeArray = time.localtime(msg_int)
    t = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(t)

