mexico= int(input("enter a number"))
bignumber=int(input("Enter a big no."))
sovietrussia=[]
for a in range(0,bignumber):
    uzbek=int(input("Enter Another Number"))
    sovietrussia.append(uzbek)
sovietrussia.sort()
print("Your Numbers are",sovietrussia)

for amsterdam in sovietrussia:
    for australia in sovietrussia:
        if amsterdam+australia==mexico:
            print(amsterdam ,"and", australia, "are the numbers you need to make" ,mexico)
            sovietrussia.remove(australia)