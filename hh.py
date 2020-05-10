import requests
from bs4 import BeautifulSoup
import re

# 定义章节目录url
indexUrl = "https://www.kanunu8.com/tuili/9506/"

# 定义headers，模拟浏览器访问
headers = {
    #"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    #"accept-encoding":"gzip, deflate, br",
    #"accept-language":"zh-CN,zh;q=0.9",
    #"Connection":"keep-alive",
    #"upgrade-insecure-requests":"1",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}

# 获取html
r = requests.get(indexUrl, timeout = 10, headers = headers)

# 打印状态码
#print(r.status_code)

# 转码
r.encoding = 'gb2312'
html = r.text
soup = BeautifulSoup(html,"html.parser")

# 获取标题
title = soup.h1.string
print(title)

"""
file = open(title+'.txt', 'w')
file.write(title+'\n')
"""

# 生成各章节url列表
contentUrlList = []
for a in soup.find_all('a', href = True):
    contentUrlList = contentUrlList + re.findall("\d{6}.html", a['href'])

for index in range(len(contentUrlList)):
    url = indexUrl+contentUrlList[index]
    #print(url)
    r = requests.get(url, timeout = 10, headers = headers)
    #print(r.status_code)
    r.encoding = 'gb2312'
    html = r.text
    soup = BeautifulSoup(html,"html.parser")
    
    # 获取章节标题
    print(soup.title.string.split('_')[0]+"\n\n")
    
    # 获取正文内容
    print(soup.p.text+"\n\n")

"""
file.close()
"""
