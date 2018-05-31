#!/usr/bin/env python
import urllib2

index = open('b.txt')
for line in index:
    url = line.split('>')[0].strip()
    title = line.split('>')[1].strip()

    f = open(title+".txt",'w')
    r = urllib2.urlopen(url)
    for line in r:
        if line.find('<br />') >= 0:
            out = line.replace('<div id="content">','')
            out = out.replace('<br />','')
            out = out.replace('&nbsp;','')
            print out
            f.write(out)
    f.close()
index.close()
