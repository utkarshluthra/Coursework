import mysql.connector as db
import random
host=input("Enter the name of the host of your MySQL. (use 'localhost' if not sure): ")
User=input("Enter the name of the user of MySQL. (use 'root' if not sure): ")
password=input("Enter your MySQL Password: ")
conn=db.connect(host = host, user=User, passwd=password)
cursor=conn.cursor()
cursor.execute("create database if not exists classXIIproject")
cursor.execute("use classXIIproject")
cursor.execute("create table if not exists flashcards(Front varchar(50), Back varchar(50), Cardid int(3))")
cursor.execute("create table if not exists result(SNo int(3), Percent int(3), maxmarks int(3), minmarks int(3), result varchar(10))")

def deck():

    cursor.execute("SELECT Front, Back FROM flashcards ORDER BY Cardid ASC;")

    print('''WELCOME TO THE SINGLE DECK FLASHCARD PROGRAM.

    Here you can see all the flashcards in the deck arranged in increasing order of the Card Id.''')
    a=cursor.fetchall()
    count=cursor.rowcount
    print("The given deck has ", count, " flashcards \n")

    for row in (a):
        print(row)
    return

def result():
    print('''Welcome to the results file of the program \n
    Here you can see all your revious programs' scores \n''')

    cursor.execute("Select * from result")

    a=cursor.fetchall()
    for row in a:
        print(row)

    ch=input("Do you want an overwitten txt file with all your scores? (y/n) ")
    if ch=='y':
        with open("LatestScore.txt", 'w') as fh:
            for row in a:
                fh.write(str(row)+"\n")
    else:
        print("Going back to Main Menu")

def enterData():
    cursor.execute("create database if not exists classXIIproject")
    cursor.execute("use classXIIproject")
    print('''This is a program to ecreate new flashcards in this single deck flashcard program.''')

    cursor.execute("create table if not exists flashcards(Front varchar(50), Back varchar(50), Cardid int(10) primary key)")
    ch='y'
    while ch=='y':
        a=int(input("Enter the start value: "))
        b=int(input("Enter the last value you will enter"))

        for i in range(a, b+1):
            
            front = str(input("Enter the data for front of card: "))
            back = str(input("Enter the data for back of the card: "))
            
            cursor.execute("INSERT INTO flashcards VALUES ('{}','{}',{}) ".format(front, back, str(i)))
            conn.commit()

        print ("Data entered successfully.")

        ch=str(input("Do you want to continue? (y/n)"))
    
def tuptolst(tup):
        tup1=[tup]
        lst=[]
        for t1 in tup1:
            for r in t1:
                lst.append(r)
                return lst
def test():
    cursor.execute("CREATE DATABASE IF NOT EXISTS classXIIproject;")
    cursor.execute("USE classXIIproject;")
    cursor.execute("create table if not exists result(SNo int(3), Percent int(3), maxmarks int(3), minmarks int(3), result varchar(10))")
    cursor.execute("create table if not exists flashcards(Front varchar(50), Back varchar(50), Cardid int(10) primary key)")

    
            
    print('''Welcome to the Flashcard test.\n
    Here, you can test yourself on any of the words given in the dictionary''')

    print("\n")
    print("General Instructions")
    print('''1. The given test is case sensitive.
    2. Leaving question blank accounts for a wrong answer
    3. One point will be awarded to each correct answer and the same will be deducted in case of a wrong answer
    4. There is no time limit or limit to the questions''')

    #To obtain upperlimit of randint() function
    #Fetching maximum value of cardid


    cursor.execute("select max(Cardid) from flashcards;")
    s=cursor.fetchall()
    for row in s:
        h=(row)
        
    lst1=tuptolst(h)
    upperlimit=lst1[0]
    try:
        count=0
        ch='y'
        while ch=='y':#1
            num=int(input("Enter the number of questions to ask: "))
            for i in range(0, num):#3
                rand=random.randint(1, upperlimit)
                rep=rand
                cursor.execute("Select Front from flashcards where cardid={}".format(rand))
                a=cursor.fetchall()
                for row in a:#3
                    print(row)
                    
                cursor.execute("Select Back from flashcards where cardid={}".format(rep))
                b=cursor.fetchall()
                for row in b:#4
                    x=str(row)
            
                ans=input("What should be in the back of the card?")
                bi="('"+ans+"',)"
                if x==bi:
                    count+=1
                    print("Correct Answer!!! \n")
                else:
                    count=count-1
                    print("Wrong Answer!!!")
                    print("The correct answer is ",x, "\n")
                
                i+=1
            
            print("You have recieved ", count, " points. \n")

            #To assign S_no field in database
            #Fetching previous maximum value of S_no

            cursor.execute("select MAX(SNo) from result")
            g=cursor.fetchall()
            for row in g:
                z=(row)

                lst2=tuptolst(z)
                if lst2[0]==None:
                    cursor.execute("insert into result values(0, 0, 0, 0, '')")
                    lst2[0]=0
            sno= int(lst2[0])+1

            #For percentage field in database
            percentage=0
            if count<0:
                percentage=0
            else:
                percentage=(count/num)*100

            MM=num
            MO=count
            #For Pass/Fail
            if percentage>33:
                result="pass"
                print("Congratulations!!! You have scored", percentage,"% in the test. YOU HAVE PASSED")
            else:
                result="fail"
                print("Sorry... but you have failed in the test. Try again...")
            #To add to database
            cursor.execute("INSERT INTO result values ({},{},{},{},'{}')".format(sno, percentage, MM, MO, result))
            conn.commit()
            ch=input("Do you want to continue(y/n)")#Exiting loop 1
    except TypeError:
        print("No Flashcards Created. First create flashcards using the Main Menu")

def searchbyFront(Front):
    argument="\""+str(Front)+"\""
    cursor.execute("Select Front, Back from flashcards where front={}".format(argument))
    x=cursor.fetchall()
    for row in x:
        print(row)
def searchbyBack(Back):
    argument="\""+str(Back)+"\""
    cursor.execute("Select Front, Back from flashcards where back={}".format(argument))
    x=cursor.fetchall()
    for row in x:
        print(row)

def searchByID(id):
    cursor.execute("Select Front, Back from flashcards where cardid={}".format(id))
    x=cursor.fetchall()
    for row in x:
        print(row)

if __name__=='__main__':
    ch='y'
    while ch=='y':

        print('''Welcome To SINGLE DECK FLASHCARD PROGRAM's Main Menu.
        
        Each flashcard has tow faces, front and back. The front being the question/prompt and the back being the answer/hint all of which is designed by you, the user, as per the menu below.''')
        print('''Enter your choice below
        1. To see all your flashcards in one place.
        2. Take a Test based on random flashcards
        3. See previous results on the tests
        4. Add flashcards to the dictionary.
        5. Search a card by its Card-id
        6. Search a card by its Front
        7. Search a card by its Back
        8. Exit Program
        ''')
        mainChoice=int(input("Enter your Choice here: "))
        print("\n")
        if mainChoice==1:
            deck()

        elif mainChoice==2:
            test()

        elif mainChoice==3:
            result()

        elif mainChoice==4:
            enterData()
        elif mainChoice==5:
            i=int(input("Enter the id you want to search: "))
            searchByID(i)
        elif mainChoice==6:
            try:
                front=input("Enter the text in the front to search: ")
                searchbyFront(front)
            except Exception:
                print("invalid entry")
            
        elif mainChoice==7:
            try:
                back=input("Enter the text in the front to search: ")
                searchbyBack(back)
            except Exception:
                print("invalid entry")
        elif mainChoice==8:
            break
        else:
            print("Invalid Choice!!")

        ch=str(input("Do you want to go back to the main menu? (y/n) "))

    conn.close()
    if conn:
        conn.close()
        print("Connection is Closed Permanently.")
