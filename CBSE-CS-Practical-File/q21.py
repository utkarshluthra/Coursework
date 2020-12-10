import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="root",database="school")
cursor=conn.cursor()
query="delete from student where rollno=102"
cursor.execute(query)
conn.commit()
print(cursor.rowcount,"record deleted")
