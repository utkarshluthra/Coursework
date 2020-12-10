import csv
fh=open("student.csv","w")
wobj=csv.writer(fh)
wobj.writerow(['RollNo','Name','Marks'])
while ch=='y':
    rollno=int(input("Enter Rollno: "))
    name=input("Enter Name: ")
    marks=float(input("Enter Marks: "))
    rec=[rollno,name,marks]
    wobj.writerow(rec)
    ch=input("Do you want to continue? (y/n)")
fh.close()