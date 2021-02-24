import json
import yaml

import requests
import base64
"""
·需要二次封装requests，对请求j进行定制化
·将请求结构体url从一个写死ip替换成动态域名
·使用env配置文件，存放环境配置信息
·将请求结构中的url替换未env配置文件中的url
·将env配置文件使用yaml进行管理
"""
class Api:
    data = {
        "method":"get",
        "url":"http://testing-studio:9999/demo1.json",
        "headers":None,
        "json":None,
        "encoding":"base64"
    }
    with open('./common/env.yaml','r')as f:
        env = yaml.safe_load(f)
    def send(self,data:dict):
        data['url'] = str(data['url']).replace('test',self.env['test_studio'][self.env['defult']])
        res = requests.request(method=data['method'],url=data['url'],headers=data['headers'],json=data['json'])
        return res
