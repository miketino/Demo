#!C:\Python\Python37
# _*_ coding: UTF-8 _*_
#爬虫

import requests
import json

url = "http://fanyi.baidu.com/basetrans"

data = {
    "from": "zh",
    "to": "en",
    "query": "你好，世界"
}

headers= {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

response = requests.post(url, data = data, headers = headers)
print(response)
html = response.content.decode()
dict_ret = json.loads(html)
print(dict_ret)
print(type(dict_ret))
#ret = dict_ret["trans"][0]["dst"]
#print(ret)
