import pickle
print("Now reading contents of the file...")
fh = open("q3.dat","rb")
try:
    while True:
        stu=pickle.load(fh)
        print(stu)
except EOFError:
    fh.close()