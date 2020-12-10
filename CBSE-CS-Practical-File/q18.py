import mysql.connector as sql
conn = sql.connect(host="localhost",user="root",passwd="root",database="school")
cursor=conn.cursor()
query="insert into student(rollno,sname,age,city)values(%s,%s,%s,%s)"
val=(105,'sachin',15,'indore')
cursor.execute(query,val)
conn.commit()
print(cursor.rowcount,"record inserted")
conn.close()
