import csv
fh=open("employee.csv","w",newline="")
wobj=csv.writer(fh)
ans='y'
emprec=[['empno','empname','empsalary']]
print("Enter Employee details: ")
while ans=='y':
    eno=int(input("Enter employee number: "))
    ename=input("Enter employee name: ")
    esal=float(input("Enter employee salary: "))
    emprec.append([eno,ename,esal])
    ans=input("Do you want to enter more records ?(y/n): ")
else:
    wobj.writerows(emprec)
    print("Records written successfully.")
fh.close()

with open("employee.csv","r") as fh:
    robj=csv.reader(fh)
    for x in robj:
        print(x)
