import  mysql.connector as db
conn=db.connect (host="localhost", user="root", passwd="u1524", database="classxiiproject")
cursor= conn.cursor()
print('''This is a program to enter any new word in the English Spanish dictionary

It is important to note that the words should exist.''')
ch='y'
while ch=='y':
    a=int(input("Enter the start value: "))
    b=int(input("Enter the last value you will enter"))

    for i in range(a, b+1):
        
        eng = str(input("Enter English Word: "))
        sp = str(input("Enter Spanish Word: "))
        
        cursor.execute("INSERT INTO estrans VALUES ('{}','{}',{}) ".format(eng, sp, str(i)))
        conn.commit ()

    print ( 'Data entered successfully.' )

    ch=str(input("Do you want to continue? (y/n)"))
conn . close ()

if (conn):
    conn.close()
    print("The mysql connection is closed.")
