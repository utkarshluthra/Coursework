# file handling
# file operations: 1. Read 2. Write 3. Append(edit) and their combinations
# type of files : 1. binary and 2. non binary(Text file)
# A file is a bunch of data which is stored in the memory.
# Writing in a file replaces out the old data while append writes new data at the end data
# End of line characters : '\n' '\r\n' 
file1=open('C:\\Users\\Prade\\Desktop\\years.csv',"r") 
#syntax: 
# <name of file handler>=[open/close](<file location and name>, <file mode>)
#new file is created in w,a,w+,a+ writing modes in case of unavailable file
f= file1.read()
print(f)
file1.close()