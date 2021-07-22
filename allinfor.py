# 公告内信息(已完成）
import requests
from lxml import etree

url = 'https://www.binance.com/zh-CN/support/announcement/aec178a59f824162ab77a17a5d0838a5'
proxy = {'http': 'http://192.168.101.20:8123'}

r = requests.get(url, proxies=proxy).text
r = etree.HTML(r)
content = r.xpath('//div[@class="css-vkw2w1"]/h1/text()')
print(content[0])
content = r.xpath('//article/div/strong/text()')
content1 = r.xpath('//article/div[@class="css-mm1dbi"]/text()')
content2 = r.xpath('//article/div[@class="css-mm1dbi"]/a[@class="css-li4l4s"]/text()')
content3 = r.xpath('//article/div[@class="css-3fpgoh"]/text()')
print(content[0])
print(content1[0]+content2[0]+content1[1])
print(content1[2])
for x in range(0, 3):
    print(content3[x])

