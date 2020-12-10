import mysql.connector as db
import random

conn=db.connect(host="localhost", user="root", password="u1524", database="classxiiproject")
cursor=conn.cursor()

def tuptolst(tup):
    tup1=[tup]
    lst=[]
    for t1 in tup1:
        for r in t1:
            lst.append(r)
            return lst
        
print('''Welcome to the English to Spanish test.\n
Here, you can test yourself on any of the words given in the dictionary''')

print("\n")
print("General Instructions")
print('''1. The given test is case sensitive.
2. The first letter of the word may or may be capital as per the word to translate. If the english word is capitalized, the the spanish word must also be capitalized
3. In case of use of words with 'la' or 'el', do not capitalize words
4. Leaving question blank accounts for a wrong answer
5. One point will be awarded to each correct answer and the same will be deducted in case of a wrong answer
6. There is no time limit or limit to the questions \n''')

#To obtain upperlimit of randint() function
#Fetching maximum value of uid
cursor.execute("select max(uid) from estrans")
s=cursor.fetchall()
for row in s:
    h=(row)
    
lst1=tuptolst(h)
upperlimit=lst1[0]

count=0
ch='y'
while ch=='y':#1
    q=num=int(input("Enter the number of questions to ask: "))
    while q==num:#2
        for i in range(num):#3
            rand=random.randint(1, upperlimit)
            rep=rand
            m=cursor.execute("Select English_word from estrans where uid={}".format(rand))
            a=cursor.fetchall()
            for row in a:#3
                print(row)
                
            n=cursor.execute("Select Spanish_word from estrans where uid={}".format(rep))
            b=cursor.fetchall()
            for row in b:#4
                x=str(row)
        
            ans=input("Enter the Spanish word")
            bi="('"+ans+"',)"
            if x==bi:
                count+=1
                print("Correct Answer!!! \n")
            else:
                count=count-1
                print("Wrong Answer!!!")
                print("The correct answer is ",x, "\n")
            q='n'#Exiting loop 2
    ch=input("Do you want to continue(y/n)")#Exiting loop 1
print(count)

#To assign S_no field in database
#Fetching previous maximum value of S_no
w=cursor.execute("select MAX(S_no) from result")
g=cursor.fetchall()
for row in g:
    z=(row)
    
lst2=tuptolst(z)
sno= lst2[0]+1

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

if (conn):
    conn.close()
    print("Thank You")
