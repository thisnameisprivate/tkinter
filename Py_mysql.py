import pymysql as db
connection = db.connect(host = 'localhost', port = 3306, user = 'root', passwd = '', db = 'visit', charset='utf8')
cur = connection.cursor()
sql = "select * from alldiseases"
cur.execute(sql)
rows = cur.fetchall()
for dr in rows:
    print(dr)