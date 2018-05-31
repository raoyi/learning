#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#create txt file
f = open("yinyangguiyi.txt",'w')

#set start url
url = 'http://m.shumil.com/yinyangguiyi/6026995.html'

while True:
    r = urllib2.urlopen(url)
    time.sleep(5)
    for line in r:
        
        #get title
        if line.find('<div id="headline">') >= 0 and line.find('</div>') >= line.find('<div id="headline">'):
            title = line[line.find('<div id="headline">')+19:line.find('</div>')].strip()
            if title.find('.第') >= 0:
                title = title[title.find('.第')+1:]
            f.write('\n' + title + '\n')
            print title + ' is saving...'

        #get conntent
        if line.find('&nbsp;') >= 0 or line.find('<br />') >= 0:
            out = line.replace('<div id="content">','')
            out = out.replace('<br />','')
            out = out.replace('&nbsp;','')
            out = out.replace('</div>','')
            #print out
            f.write(out)

        #get next url
        if line.find('">下一章</a></td>') >= 0:
            index = line[line.find('<td><a href="')+13:line.find('">下一章</a></td>')].strip()
            if index == '/yinyangguiyi/':
                print 'stoped...'
                raw_input()
            url = 'http://m.shumil.com' + index

f.close()
