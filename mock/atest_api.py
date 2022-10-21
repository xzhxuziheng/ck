"""
coder: xuziheng
date: 2022/10/10 10:01
"""


def atest_api():
    pass


def atest_api_statues():
    result = atest_api()
    try:
        if result["result"] == "success":
            return "支付成功"
        elif result["result"] == "fail":
            return "支付失败"
        else:
            return "未知错误异常"
    except:
        return "Error, 服务端返回异常!"


if __name__ == '__main__':
    r = atest_api()
    re = 'success'
    print(atest_api_statues())