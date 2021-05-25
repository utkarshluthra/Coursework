import mysql.connector as sql
import csv
conn = sql.connect(host="localhost", password="root", user="root", database="Guests")
cursor = conn.cursor()
cursor.execute("select S_no, Name, Address, city, email, mobile from apr2020 where mobile!=\"Null\" group by mobile;")
a=cursor.fetchall()
count=0
def remove(string):
    return string.replace(" ", "")
def comma_remove(string):
    return string.replace(",", "")

for i in a:
    sno=str(i[0])
    name=i[1]
    address=i[2]
    Address=comma_remove(address)
    city=i[3]
    City=comma_remove(city)
    email=i[4]
    mobile=i[5]
    mobile_pure=remove(mobile)
    mobile_10 = mobile_pure[-10:]
    
    query=sno+", "+name+", "+Address+", "+City+", "+email+", "+mobile_10+"\n"

    with open("Apr2020_corrected.csv", "a") as fh:
        fh.write(query)

