# from urllib.request import urlopen
#
#
# url = "http://www.baidu.com"
# r = urlopen(url)
# with open("myfirst.html", mode='w', encoding='utf-8') as f:
#     f.write(r.read().decode('utf-8'))
# print('!!')


'''
#原始响应内容
import requests
r = requests.get("http://www.baidu.com",stream=True)
print(r.raw.read(10))

'''

'''
#响应状态码
import requests
r = requests.get('http://www.baidu.com')
print(r.status_code==requests.codes.ok)
if r.status_code==requests.codes.ok :
    print(r.status_code)
else :
    print("False!")
'''

'''
#定制请求头
import requests
headers={'user-agent':'my-app/0.0.1'}
url='http://www.baidu.com'
r = requests.get(url,headers=headers)
print(r.url)
'''

'''
# 传递表单形式的数据
import requests
pl={'key1':'value1','key2':'value2'}
# pl=(('key1','value1'),('key2','value2')) # 多元素同一key
url='http://www.baidu.com'
r = requests.post(url,data=pl)
print(r.url)
'''

'''
# 上传编码文件
import requests
url = 'http://www.baidu.com'
files = {'file' :open('report.xls','rb')}

r = requests.put(url,files=files)
r.text
'''

'''
# 访问响应头
import requests
url = 'http://www.baidu.com'
r = requests.get(url)
print(r.headers['connect'])
'''

'''
# 发送自己的cookies到服务器
import requests
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url,cookies=cookies)
print(r.text)
'''

'''
#用allow_redirects来禁止重定向
import requests
r = requests.get('http://github.com')
print(r.status_code)
r = requests.get('http://github.com',allow_redirects=False)
print(r.status_code)
'''

'''
# 会话跨对象
import requests
s = requests.session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)
'''

"""
import requests
s = requests.Session()
'''
s.auth = ('user','pass')
s.headers.update({'x-text':'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)
'''

r = s.get('http://httpbin.org/cookies',cookies={'from-my':'brower'}) # 发送一个cookies
print(r.text)
r = s.get('http://httpbin.org/cookies',cookies={'from-my':None}) # 移除一个值
print(r.text)
"""
# 任务4
import requests
import json
import pprint

url = 'https://api.cosmostation.io/v1/status'
r = requests.get(url).text
r = json.loads(r)
print(type(r))  # 字典
pprint.pprint(r['total_circulating_tokens'], indent=2)

# x = re.findall('total_circulating_tokens.*}]}', r)
# print(r)


# import requests
#
# url = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABIAQMAAABvIyEEAAAABlBMVEUAAABTU1OoaSf/AAAAAXRSTlMAQObYZgAAAENJREFUeF7tzbEJACEQRNGBLeAasBCza2lLEGx0CxFGG9hBMDDxRy/72O9FMnIFapGylsu1fgoBdkXfUHLrQgdfrlJN1BdYBjQQm3UAAAAASUVORK5CYII='
#
# r = requests.get(url)
# print(r.text)

