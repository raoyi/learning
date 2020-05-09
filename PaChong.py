import requests
from bs4 import BeautifulSoup
url="https://www.kanunu8.com/tuili/9506/"
r=requests.get(url)
r.encoding='gb2312'
demo=r.text
#将r.text赋给demo
soup=BeautifulSoup(demo,"html.parser")
#用 html.parser解析器解析demo(即 r.text),赋给soup
print(soup.prettify())
#输出解析后的结果

print(soup.title)
#输出html的 <title>与</title>之中的内容

tag=soup.a
print(tag)
#获取(第一个)a标签（链接），并输出

print(soup.a.name)
#获取a标签的名字，并输出

print(soup.a.parent.name)
#获取a标签的父标签的名字，并输出
tag=soup.a
#获取a标签

print(tag.attrs)
#输出a标签的属性

print(tag.attrs['class'])
#输出a标签的属性中class属性的值

print(tag.attrs['href'])
#输出a标签的属性中href属性的值

print(type(tag.attrs))
#a.attrs(a的属性的类型)  结果为<class 'dict'>  (dict:字典)

print(type(tag))

print(soup.a)
#输出a标签的内容

print(soup.a.string)
#获取a标签中未用<>包含的部分

print(soup.head)
#获取从<head>开头 到</head>结尾的内容,并输出

print(soup.head.contents)
#soup.head.contents 获取的内容比soup.head获取的内容少了最前面的<head>和最后面的</head>
#其余内容放在[]中,(即类型为列表)

'''
.parent  节点的父亲标签
.parents 节点的先辈标签的迭代类型，用于循环遍历先辈节点
.contents 子节点的列表，将<tag>（标签）所有的儿子节点存入列表
.children 子节点的迭代类型,与.contents类似,用于循环遍历子节点
.descendants 子孙节点的迭代类型，包含所有子孙节点，用于循环遍历
'''
print(soup.title.parent)
#获取title标签的父节点,并输出

print(soup.html.parent)
#获取html标签的父节点,html已是最高层（根结点）
#它没有父节点,返回它本身

print(soup.parent)
#soup没有父节点,返回None

for parent in soup.a.parents:
    if parent is None:#soup没有父节点,返回None，这时
        print(parent)
    else:
        print(parent.name)
#循环遍历a标签的父节点，并打印
#返回结果不为None时,打印这个父节点的名字
#若返回结果为None时,打印这个父节点(soup)打印出[document]
'''
标签树的平行遍历:
.next_sibling 返回按照html文本顺序的下一个平行节点标签
.previous_sibling 返回按照htmml文本顺序的上一个平行节点标签
.next_siblings 迭代类型，返回按照html文本顺序的后续所有平行节点标签
.previous_siblings 迭代类型,返回按照html文本顺序的前续所有平行节点标签
必须是同一个父节点下的平行节点
'''

print(soup.a.next_sibling)
#获取a标签的下一个平行标签,并输出

print(soup.a.previous_sibling)
#获取a标签的上一个平行节点标签

for sibling in soup.a.next_siblings:
    print(sibling)
#循环遍历a节点标签的所有后续节点标签,并输出

for sibling in soup.a.previous_siblings:
    print(sibling)
#循环遍历a节点标签的所有前续节点标签,并输出
