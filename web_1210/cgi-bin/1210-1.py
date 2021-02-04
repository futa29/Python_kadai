import cgi
import codecs
import sys

sys.stdout = codecs.getwriter('utf_8')(sys.stdout.detach())

print('Content-type: text/html; charset=UTF-8')


form = cgi.FieldStorage()

#第2引数で値を受け取らなかった場合の処理ができる
text = form.getfirst('text','未入力')



print('''
<!DOCTYPE html>
<html>
<head>
 <title>Webの勉強　谷　風汰</title>
 <meta http-equiv="content-type" charset="utf-8">
</head>
<body>
 <h2>こんにちは「
 ''')
print(text)
print('''
 」さん</h2>
 


</boby> 
</html>





''')
