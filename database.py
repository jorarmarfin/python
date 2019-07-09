import pymysql
v_host = 'localhost'
v_user = 'root'
v_db = 'emanuel'
v_pass = 'P@ssw0rd'
db = pymysql.connect(host=v_host, user=v_user,passwd=v_pass, db=v_db)
cursor = db.cursor()
#Variable
recs=cursor.execute("SELECT * FROM movimiento limit 1")
# for x in range(recs):
#    print(cursor.fetchone())
#Indirectamente
for row in cursor:
   print(row[0])