"""
coder: xuziheng
date: 2022/10/13 11:24
"""
import requests
import pytest
from electric.common.excel_data import ExcelData
import os

path = os.path.dirname(__file__).split('hardwareData')[0] + 'common\\告警数据依赖.xlsx'
excel_data = ExcelData(path, 'Sheet1').read_excel()


class TestHardwareDta:
    @pytest.mark.parametrize('param', [data for data in excel_data])
    def test_warm_data(self, param):
        point_index = param['point_index']
        point_name = param['point_name']
        mark = param['mark']
        re_data = {
            "uid": "c2430c131bd4d33e2d12d32434071d6c",
            "productId": "524e51c772d04f34bdbfd4b094f735a8",
            "deviceId": "37485d5b203a46a69bc5981a30b3e286",
            "mac": "1c1704d0789700200000840000000000",
            "commandList": [
                {
                    "pointMap": {
                        "msg_alarmFlag": {
                            "t": 1,
                            "v": 1,
                            "i": 8408,
                            "id": "d01c599c2aa9470bbb7f7279fefffd11",
                            "n": "msg_alarmFlag"
                        },
                        "msg_msgType": {
                            "t": 4,
                            "v": 420,
                            "i": 8400,
                            "id": "41aa76770701402fb7e20567bb2cb05d",
                            "n": "msg_msgType"
                        },
                        "msg_alarmTime": {
                            "t": 5,
                            "v": 1665644456,
                            "i": 8404,
                            "id": "9cc3343583be49fabeb82c6c7f31bcb8",
                            "n": "msg_alarmTime"
                        },
                        "msg_devId": {
                            "t": 0,
                            "v": "CHZD08TBLD220621001",
                            "i": 8403,
                            "id": "8117c282957643ff80e05463367dc143",
                            "n": "msg_devId"
                        },
                        point_name: {
                            "t": 1,
                            "v": 1,
                            "i": point_index,
                            "id": "f47cdbb4bd74425ca7dfaa19ac20ccaa",
                            "n": point_name
                        },
                        "msg_txnNo": {
                            "t": 5,
                            "v": 1665501450,
                            "i": 8401,
                            "id": "90627d2048a14dd1a59b9b4fd8084a61",
                            "n": "msg_txnNo"
                        }
                    },
                    "cmd": 98
                }
            ]
        }
        url = 'https://batterytest.ledear.cn/smart-radio-web/ark/data'
        res = requests.post(url=url, json=re_data)
        print(res.json())


if __name__ == '__main__':
    pytest.main()
