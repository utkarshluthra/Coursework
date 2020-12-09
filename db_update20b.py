import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="school")
mycursor=mydb.cursor()
sql="update student set age=%s where rollno=%s"
val=(20,101)
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record updated")
