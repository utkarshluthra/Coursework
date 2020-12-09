import csv
fh=open("d:\student.csv","w")
wobj=csv.writer(fh)
wobj.writerow(['RollNo','Name','Marks'])
for i in range(5):
    rollno=int(input("Enter Rollno: "))
    name=input("Enter Name: ")
    marks=float(input("Enter Marks: "))
    rec=[rollno,name,marks]
    wobj.writerow(rec)
fh.close()
