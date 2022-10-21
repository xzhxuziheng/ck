"""
coder: xuziheng
date: 2022/10/10 10:00
"""
import unittest
from unittest import mock
from mock import atest_api


class TestApiStatues(unittest.TestCase):
    """单元测试用例"""
    def test_01(self):
        r = atest_api.test_api().mock.Mock(return_value={
            "result": "fail",
            "msg": "余额不足"
        })
        print(r)

    # def test_02(self):
    #     """测试支付失败场景"""
    #     # mock一个支付失败的数据
    #     pay.zhifu = mock.Mock(return_value={"result": "fail", "msg": "余额不足"})
    #     # 根据支付结果测试页面跳转
    #     statues = pay.zhifu_statues()
    #     print(statues)
    #     # self.assertEqual(statues, "支付失败")


if __name__ == "__main__":
    unittest.main()
