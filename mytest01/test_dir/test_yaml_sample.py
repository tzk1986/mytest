# -*- coding:utf-8 -*-
"""
@Author:tang
@File:test_yaml_sample.py
@Time:2022/5/25 17:28
说明：
"""
import seldom
from seldom import file_data


class YamlTest(seldom.TestCase):

    @file_data(file="data.yaml", key="bing")
    def test_yaml_driver(self, keyword):
        """ data driver case """
        self.open("https://cn.bing.com")
        self.type(id_="sb_form_q", text=keyword, enter=True)
        self.assertInTitle(keyword)
        # print(un)
        # print(pd)


if __name__ == '__main__':
    seldom.main(debug=True)
