import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="school")
mycursor=mydb.cursor()
sql="insert into student(rollno,sname,age,city)values(%s,%s,%s,%s)"
val=(105,'sachin',15,'indore')
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted")
