#Write a program to read the text files line by line and display each word separated by a "#"
a=""
with open('source.txt', 'r') as fh:
    for line in fh:
        words = line.split()
        for i in words:
            a = a +"#"+ i
print(a)
