import pickle
stu={}
fh=open("d:\student.dat","ab")
ans='y'
while ans=='y':
    rno=int(input("Enter Roll Number: "))
    name=input("Enter Name: ")
    marks=float(input("Enter marks: "))
    stu['RollNo']=rno
    stu['Name']=name
    stu['Marks']=marks
    pickle.dump(stu,fh)
    ans=input("Do you want to append more records ? (y/n) ")
print("Now displaying contents of updated file...")
fh=open("d:\student.dat","rb")
try:
    while True:
        stu=pickle.load(fh)
        print(stu)
except EOFError:
    fh.close()
          
    
