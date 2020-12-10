import pickle
stu={}
found=False
fin=open("q3.dat","rb+")
try:
    while True:
        rpos=fin.tell()
        stu=pickle.load(fin)
        if stu['Marks']>81:
            stu['Marks']+=2
            fin.seek(rpos)
            pickle.dump(stu,fin)
            found=True
            print("Updated contents are : ")
            print(stu)
except EOFError:
    if found==False:
        print("Not Found")
    else:
        print("Record(s) Successfully Updated.")
    fin.close()
