import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="school")
mycursor=mydb.cursor()
mycursor.execute("select * from student where age>12")
myres=mycursor.fetchall()
for x in myres:
    print(x)
