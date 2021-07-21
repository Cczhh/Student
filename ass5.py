# 币安公告列表(已完成）
import re
import requests

# 第一页
url = 'https://www.binance.com/zh-CN/support/announcement/c-48'
proxy = {'http': 'http://192.168.101.20:8123'}

r = requests.get(url, proxies=proxy)
obj = re.compile(r'class="css-1ej4hfo"(?P<title>.*?)</a>')
txt = obj.finditer(r.text)
for it in txt:
    print(it.group("title"))
print("The page 1\n")

# 第n页（n>1)
for x in range(2, 51):
    url = 'https://www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query'
    params = {
        'catalogId': 48,
        'pageNo': x,
        'pageSize': 15
    }

    headers = {
        'lang': 'zh-CN'
    }

    r = requests.get(url, proxies=proxy, params=params, headers=headers)
    obj = re.compile(r'"title":"(?P<title>.*?)"')
    txt = obj.finditer(r.text)
    for it in txt:
        print(it.group("title"))
    print("The page", x, "\n")

