import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="school")
mycursor=mydb.cursor()
mycursor.execute("alter table student add (city varchar(10))")
