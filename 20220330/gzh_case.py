import unittest

import jsonpath as jsonpath
import requests as requests
from ddt import file_data, ddt


@ddt
class GzhCase(unittest.TestCase):

    @file_data('test.yaml')
    def test_01_get_token(self, **kwargs):
        print(kwargs['name'])
        print(kwargs['request']['method'])
        print(kwargs['request']['url'])
        print(kwargs['request']['data'])
        print(kwargs['validate'])

        if 'name' in kwargs.keys() and 'request' in kwargs.keys():
            if jsonpath.jsonpath(kwargs, '$..url') and jsonpath.jsonpath(kwargs, '$..method'):
                res = requests.get(url=kwargs['request']['url'], params=kwargs['request']['data'])
                print(res.json(), type(res.json()))
                # 进行断言，通过循环判断条件是否成功
                for assert_type in kwargs['validate']:
                    for key, value in dict(assert_type).items():
                        # 查看使用的断言参数
                        # print(key, value)
                        if key == 'equals':
                            pass
                        elif key == "contains":
                            if value in res.text:
                                print("断言通过")
                            else:
                                print("断言失败")
            else:
                print("request目录下必须有url和method")
        else:
            print("一级关键字必须要有name，request")


if __name__ == '__main__':
    unittest.main()
