mexico= int(input("enter a number"))
bignumber=int(input("Enter a big no."))
sovietrussia=[]
for a in range(0,bignumber):
    uzbek=int(input("Enter Another Number"))
    sovietrussia.append(uzbek)
sovietrussia.sort()
print("Your Numbers are",sovietrussia)
countyes=0
countnot=0
for amsterdam in sovietrussia:
    for australia in sovietrussia:
        if amsterdam+australia==mexico:
            print(amsterdam ,"and", australia, "are the numbers you need to make" ,mexico)
            sovietrussia.remove(australia)
            countyes+=1
        else:
            countnot+=1
print(countnot+" Combinations are not giving the sum as "+mexico)
print(countyes+" combinations are giving the sum as "+mexico)
