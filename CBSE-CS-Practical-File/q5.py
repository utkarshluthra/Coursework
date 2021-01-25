#Write a program to count the number of lines in a text file which is starting with the alphabets "A" or "a"
with open("q5.txt", "r") as fh:
    s=fh.readlines()
    linecount=len(s)
    count=0
    for i in range(0, linecount):
        a=s[i]
        if a[0]=='a':
            count+=1

        elif a[0]=='A':
            count+=1
        i+=1
    print(count)
    fh.close()
