count=int(input("How many students do you want to enroll: "))
fh=open("d:\marks.txt","w")
fh.write("RollNo Name Marks \n")
for i in range(count):
    print("Enter details for student ",(i+1))
    rollno=int(input("Roll No: "))
    name=input("Enter Name: ")
    marks=float(input("Enter Marks: "))
    rec=str(rollno)+","+name+","+str(marks)+"\n"
    fh.write(rec)
fh.close()
ch=input("Do you want to read file contents:(y/n)  ")
if ch=='y':
    fh=open("d:\marks.txt","r")
    while str:
        str=fh.readline()
        print(str)
    fh.close()
if ch=='n':
    print("Successfully written ,Good bye!")
    

          
