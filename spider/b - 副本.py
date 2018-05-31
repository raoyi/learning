#!/usr/bin/env python
import urllib2

index = open('b.txt')
f = open("yinyangguiyi.txt",'w')
for line in index:
    url = line.split('>')[0].strip()
    title = line.split('>')[1].strip()

    r = urllib2.urlopen(url)
    f.write('\n'+title+'\n')
    for line in r:
        if line.find('<br />') >= 0:
            out = line.replace('<div id="content">','')
            out = out.replace('<br />','')
            out = out.replace('&nbsp;','')
            #print out
            f.write(out)
f.close()
index.close()
