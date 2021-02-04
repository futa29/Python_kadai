import cgi
import codecs
import sys


sys.stdout = codecs.getwriter('utf_8')(sys.stdout.detach())

print('Content-type: text/html; charset=UTF-8')


form = cgi.FieldStorage()
calc1 = form.getfirst('calc1')
calc2 = form.getfirst('calc2')


try:
    sum  = int(calc1) + int(calc2)
except :
    sum = '不明です'


print('''
<!DOCTYPE html>
<html>
<head>
 <title>Webの勉強 谷　風汰</title>
 <meta http-equiv="content-type" charset="utf-8">
</head>
<body>
計算結果は
 <h2>
 ''')
print(sum)
print('''
</h2>
 


</boby> 
</html>





''')
