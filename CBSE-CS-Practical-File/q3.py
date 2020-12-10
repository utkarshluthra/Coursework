import pickle
stu={}
fh=open("q3.dat","wb")
ans='y'
while ans=='y':
    rno=int(input("Enter Roll Number: "))
    name=input("Enter Name: ")
    marks=float(input("Enter marks: "))
    stu['RollNo']=rno
    stu['Name']=name
    stu['Marks']=marks
    pickle.dump(stu,fh)
    ans=input("Do you want to write more records ? (y/n) ")

          