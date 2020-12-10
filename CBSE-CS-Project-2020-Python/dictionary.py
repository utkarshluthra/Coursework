import mysql.connector as db

conn=db.connect(host = "localhost", user="root", database='classxiiproject', passwd='u1524')
cursor=conn.cursor()

cursor.execute("SELECT English_word, Spanish_word FROM estrans ORDER BY English_Word ASC;")

print('''WELCOME TO THE ENGLISH SPANISH DICTIONARY

Here you can access all the words that can be asked in the questions''')
a=cursor.fetchall()
count=cursor.rowcount
print("The given dictionary has ", count, " entries \n")
print("Hope you enjoy it \n")
for row in (a):
    print(row)

