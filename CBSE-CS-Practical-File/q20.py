import mysql.connector as sql
conn=sql.connect(host="localhost",user="root",passwd="root",database="school")
cursor=conn.cursor()
query="update student set age=%s where rollno=%s"
val=(20,101)
cursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record updated")
