import mysql.connector as sql
conn = sql.connect(host="localhost",user="root",passwd="root",database="school")
cursor=conn.cursor()
cursor.execute("select * from student where age>12")
res=cursor.fetchall()
for x in res:
    print(x)
conn.close()