import mysql.connector as db

conn=db.connect(host="localhost", user="root", password="u1524", database="classxiiproject")
cursor=conn.cursor()
print('''Welcome to the results file of the program \n
Here you can see all your revious programs' scores \n''')
cursor.execute("Select * from result")

a=cursor.fetchall()
for row in a:
    print(row)
