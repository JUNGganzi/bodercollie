#!python
print("content-type: text/html; charset=utf-8\n")
print()
import cgi,os
form = cgi.FieldStorage()
if 'id' in form:
    pageid = form['id'].value
    content = open('data2/'+pageid, 'r').read()
else:
    pageid='Hi'
    content=''
#open('data2/'+pageid, 'r')

#텍스트창 생성 및 버튼 생성,링크이용하여 파일쓰기및 읽기준비 세팅
print('''<!doctype html>
<html>
<head>
    <meta charset="utf-8">
<form action="sayhi2.py" method = "post">
<input type = "text" name = "title" placeholder = "Typing">
<input type = "submit">
</form>
</head>
<body>{title}
</body>
</html>'''.format(title=pageid))
