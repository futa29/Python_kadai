import MySQLdb
 
def db_sample():
    """ 接続サンプル """
 
    # 接続する 
    con = MySQLdb.connect(
            user='root',
            passwd='root',
            port=3308,
            host='localhost',
            db='r3b',
            charset="sjis")
 
    # カーソルを取得する
    cur= con.cursor()
     
    # クエリを実行する
    sql = "select * from hoge"
    cur.execute(sql)
 
    # 実行結果をすべて取得する
    rows = cur.fetchall()
     
    # 一行ずつ表示する
    for row in rows:
        print(row)
 
    cur.close()
    con.close()
 
db_sample()