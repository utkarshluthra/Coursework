ch='y'
while ch=='y':
    print("Welcome To English to Spanish Translation Tutorial \n")
    print("Enter the your choice below")
    print('''1. Access English to Spanish Dictionary
    2. Take a Test
    3. See previous results
    4. Add words to dictionary \n''')
    mainChoice=int(input("Enter your Choice here: "))
    print("\n")
    if mainChoice==1:
        import dictionary

    elif mainChoice==2:
        import test

    elif mainChoice==3:
        import result

    elif mainChoice==4:
        import enteringData

    else:
        print("Invalid Choice!!")

    ch=str(input("Do you want to go back to the main menu? (y/n) "))
