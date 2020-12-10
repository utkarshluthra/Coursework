# scope of variables 
#global variables can be used everywhere
#local variables are defined at a specific part of code and can be used there only.
def anything():
    a= 71 #local variable 1
    return a 
def something():
    a= "devansh" #local variable 2
    return a 
if __name__ == "__main__":
    a=17  #global variable
    print(a)
    print(anything())
    print((something()))

# namespaces
# all function                                                                                                                                                      s have a specific lifetime in a program. global: during complete program. local: during the specific function
# LEGB Rule
# Local (For Functions)> Enclosing (For Loops) > Global (For Program)> Builtin (Builtin Functions in Python)
