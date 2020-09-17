#!python

import cgi,os
form = cgi.FieldStorage()
title =form['title'].value
#파일 쓰기
opened_file = open('data2/'+title, 'w')
opened_file.write(title)
opened_file.close()
#새로운 링크가 열리지 않고 바로 출력값 나오기
print('Location: sayhi.py?id='+title)
print()
