n=int(input("Enter the number of entries: "))

for i in range(0, n):
    name=input("Enter your name: ")
    rollno=int(input("Enter your roll number: "))
    marks=int(input("Enter your marks: "))

    with open("q1.txt", 'a') as fh:
        fh.write(name+" "+str(rollno)+" "+str(marks)+"\n")