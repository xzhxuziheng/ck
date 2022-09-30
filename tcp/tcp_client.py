"""
coder: xuziheng
date: 2022/9/28 17:42
"""
from tcp import es_tcp
import socket
import time
from func_timeout import func_set_timeout


class TcpClient:

    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.address, self.port))

    def tcp_client(self):
        # client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # client.connect((self.address, self.port))
        # tcp_data = bytes.fromhex(self.data)
        # client.send(tcp_data)
        # info = client.recv(1024)
        # print(info.hex().upper())
        # client.close()
        # return info.hex().upper()
        pass

    def tcp_login(self, _data):
        tcp_data = bytes.fromhex(_data)
        self.client.send(tcp_data)
        re_info = self.client.recv(1024).hex().upper()[12:]
        msg = int(re_info, 16)
        time_array = time.localtime(msg)
        login_time = time.strftime("%Y-%m-%d %H:%M:%S", time_array)
        return login_time

    @func_set_timeout(10)
    def tcp_cmd(self):
        tcp_cmd_data = es_tcp.EsTcp('1C').es_tcp_alarm()
        print(tcp_cmd_data)
        _data = bytes.fromhex(tcp_cmd_data)
        self.client.send(_data)
        re_info = self.client.recv(1024).hex().upper()
        if re_info[:-3] == tcp_cmd_data[:-5]:
            return '中控响应成功，上报服务器数据：{}'.format(re_info)
        else:
            return '中控响应失败'


if __name__ == '__main__':
    address = '110.191.179.145'
    port = 10101
    data = 'AA 55 23 07 00 23 00 1E 09 04 64 38 36 36 32 31 35 30 35 30 31 30 34 39 34 39 34 36 30 30 38 31 39 35 36 38 30 35 38 38 38'
    # data = 'aa55051b000101'
    # tcp = TcpClient(address, port, data)
    # tcp_info = tcp.tcp_client()
    # msg = tcp_info[12:]
    # print(msg)
    # msg_int = int(msg, 16)
    # print(msg_int)
    # timeArray1 = time.localtime(msg_int)
    # t = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    # print(t)
    tcp = TcpClient(address, port)
    print(tcp.tcp_login(data))
    print(tcp.tcp_cmd())


