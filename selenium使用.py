from selenium import webdriver
import time

bro = webdriver.Chrome()
url = 'https://baidu.com/'
bro.get(url)
time.sleep(3)
bro.quit()
