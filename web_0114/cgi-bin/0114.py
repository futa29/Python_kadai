import random as ra
import codecs
import sys


sys.stdout = codecs.getwriter('utf_8')(sys.stdout.detach())

print('Content-type: text/html; charset=UTF-8')

#占いリスト
uranai_list = ["大吉","中吉","吉","凶"]


ura = ra.choice(uranai_list)
print('''
<!DOCTYPE html>
<html>
<head>
 <title>1/14課題</title>
 <meta http-equiv="content-type" charset="utf-8">
</head>
<body>
 <h2>
 ''')
print(ura)
print('''
</h2>
 


</boby> 
</html>





''')
