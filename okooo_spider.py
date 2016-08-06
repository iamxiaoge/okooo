# -*- coding: utf-8 -*-
import re
import urllib2,urllib
if __name__ == '__main__':
    f=open('2014.txt','w')
    for num in range(34):
        game_no=str(num+1)
        f.write(game_no)
        f.write('\n')
        url = 'http://www.okooo.com/soccer/league/196/schedule/11749/1-82-'+game_no+'/'
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        content = res.read()
        r1=re.compile(r'<td align="left">(?P<away>.+)</td>')
        m1=r1.findall(content)
        r2=re.compile(r'<td align="right">(?P<away>.+)</td>')
        m2=r2.findall(content)
        r3=re.compile(r'<strong class="font_red">(?P<score>.+)</strong>')
        m3=r3.findall(content)
        r4=re.compile(r'<td class="ctrl_3">(?P<gamble_3>.+)</td>')
        m4=r4.findall(content)
        r5=re.compile(r'<td class="ctrl_1">(?P<gamble_1>.+)</td>')
        m5=r5.findall(content)      
        r6=re.compile(r'<td class="ctrl_0">(?P<gamble_0>.+)</td>')
        m6=r6.findall(content)             
        for i in range(len(m3)):
            f.write(m1[i])
            f.write('!')
            f.write(m2[i])
            f.write('!')
            f.write(m3[i][0])
            f.write('!')
            f.write(m3[i][2])
            f.write('!')
            f.write(m4[i])
            f.write('!')
            f.write(m5[i])
            f.write('!')
            f.write(m6[i])
            f.write('!')
        f.write('\n')
    print "close"
    f.close()