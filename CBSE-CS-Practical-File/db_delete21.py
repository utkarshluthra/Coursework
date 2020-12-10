import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="school")
mycursor=mydb.cursor()
sql="delete from student where rollno=102"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record deleted")
