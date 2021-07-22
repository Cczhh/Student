# 币安的公告（单页）
import re
import requests

url = 'https://www.binance.com/zh-CN/support/announcement/c-48'
proxies = {'https': 'https://192.168.101.20:8123'}
dat = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 "
                  "Safari/537.36 ",
    "Content-Type": "text/plain"
}

# proxy_support = urllib.request.ProxyHandler(proxies)  # 写入代理IP（协议名称映射为URL的字典对象)
# opener = urllib.request.build_opener(proxy_support)  # 以给定顺序把处理函数串联在一起
# opener.addheaders = [dat]  # 输入请求头（不能多也不能少，忽略内含网址）
# urllib.request.install_opener(opener)  # 全局打开代理
# resp = urllib.request.urlopen(url)  # 进入要请求的网站
# html = resp.read().decode('utf-8')  # 将网站源代码赋予'html'，utf-8！！！


r = requests.get(url, proxies=proxies)
# 提取公告中心的币币交易目录
# 数据解析

obj = re.compile(r'"css-1ej4hfo">(?P<title>.*?)</a>', re.S)
result = obj.finditer(r.text)  # 迭代器的使用
print("公告中心————币币交易：\n")
for it in result:
    print(it.group("title"))


# """公告中心————币安最新公告"""
# url = 'https://www.binance.com/zh-CN/support/announcement/c-49?navId=49'
# proxy_support = urllib.request.ProxyHandler(proxies)  # 写入代理IP（协议名称映射为URL的字典对象)
# opener = urllib.request.build_opener(proxy_support)  # 以给定顺序把处理函数串联在一起
# opener.addheaders = [dat]  # 输入请求头（不能多也不能少，忽略内含网址）
# urllib.request.install_opener(opener)  # 全局打开代理
# resp = urllib.request.urlopen(url)  # 进入要请求的网站
# html = resp.read().decode('utf-8')  # 将网站源代码赋予'html'，utf-8！！！


obj = re.compile(r'"css-1ej4hfo">(?P<title>.*?)</a>', re.S)
result = obj.finditer(r.text)
print("\n\n\n\n公告中心————币安最新公告\n")
for it in result:
    print(it.group("title"))











