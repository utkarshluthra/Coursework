import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="school")
mycursor=mydb.cursor()
sql="update student set age=10 where rollno=104"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount,"record updated")
