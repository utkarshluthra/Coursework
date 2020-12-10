import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="root",database="school")
cursor=conn.cursor()
cursor.execute("alter table student add (city varchar(10))")
conn.commit()
conn.close()