import pickle
stu={}
found=False
fin=open("q3.dat","rb")
x=int(input("Enter Roll number to be searched for : "))
searchkeys=[x]
try:
    while True:
        stu=pickle.load(fin)
        if stu['RollNo'] in searchkeys:
            print(stu)
            found=True
except EOFError:
    if found==False:
        print("Not Found")
    else:
        print("Search Successful.")
    fin.close()