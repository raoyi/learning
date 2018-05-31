#coding=utf-8
import xml.dom.minidom

#在内存中创建一个空的文档
doc = xml.dom.minidom.Document() 
#创建一个根节点Managers对象
root = doc.createElement('DLurl') 

#将根节点添加到文档对象中
doc.appendChild(root) 

UrlList = [{'title' : 'A',  'url' : 1},
               {'title' : 'B', 'url' : 2}
]

for i in UrlList :
  nodeTable = doc.createElement('table')
  
  nodeTitle = doc.createElement('title')
  nodeTitle.appendChild(doc.createTextNode(str(i['title'])))

  nodeUrl = doc.createElement("url")
  nodeUrl.appendChild(doc.createTextNode(str(i["url"])))

  #将各叶子节点添加到父节点Manager中，
  #最后将Manager添加到根节点Managers中
  nodeTable.appendChild(nodeTitle)
  nodeTable.appendChild(nodeUrl)
  root.appendChild(nodeTable)
  
#开始写xml文档
fp = open('demo.xml', 'w')
doc.writexml(fp, indent='\t', addindent='\t', newl='\n', encoding="utf-8")
raw_input()
