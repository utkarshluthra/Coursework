import requests
import calendar
import json
import os

print('''

===============================================================================================
***********************************************************************************************


                                Welcome to API Project


***********************************************************************************************
===============================================================================================

''')

name=input("Enter your Name:")

ch='y'
while ch!='n':
  try:
    a=int(input(""" 
Hi {}
Choose one of the following:
1. Weather
2. Dictionary
3. Calendar
4. Calculator
5. Snake Game
    """.format(name)))
    if a==1:
      print('''
============================================================================================================

                                          Calendar

============================================================================================================
      ''')
      city=input("Enter name of City, {} ".format(name))
      url="https://wttr.in/{}".format(city)
      weatherReport = requests.get(url)
      weatherReportText = weatherReport.text
      print(weatherReportText)

    elif a==2:
      print('''
============================================================================================================

                                          Dictionary

============================================================================================================
      ''')
      word=input("Enter word, {}: ".format(name))
      url="https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(word)
      worddict = requests.get(url)
      worddictText = worddict.text
      with open("Dictionary.json", 'w') as dfh:
          dfh.write(worddictText)
      with open("Dictionary.json", 'r') as dfh:
          a=dfh.read()
          b=json.loads(a)
          print("The word, {}, means: ".format(word), end="")
          print(b[0]["meanings"][0]["definitions"][0]["definition"])

    elif a==3:
      calChoice=int(input('''
Which of the following calendar do you want to display, {}:
1. Year Calendar
2. Month Calendar
      '''.format(name)))
      if calChoice==1:
        year=int(input("Enter year: "))
        print(calendar.calendar(year))

      elif calChoice==2:
        year=int(input("Enter year: "))
        month=int(input("ENter month number: "))
        print(calendar.month(year, month))
      else:
        print("invalid")
    elif a==4:
      print("""
====================================================================================

Welcome to our Calculator, {}

====================================================================================
      """.format(name))
      a=int(input("Enter number 1:"))
      contd='y'
      while contd!='n':
        operator = input(
          '''
Choose among:
[+]
[-]
[x]
[/]

          '''
        )
        if operator=='+':
          b=int(input("Enter Second number:"))
          a=a+b
          print(a)
        elif operator=='-':
          b=int(input("Enter Second number:"))
          a=a-b
          print(a)
        elif operator=='x':
          b=int(input("Enter Second number:"))
          a=a*b
          print(a)
        elif operator=='/':
          b=int(input("Enter Second number:"))
          if b==0:
            print("Dividing by 0 is not possible")
          else:
            a=a/b
            print(a)
        contd=input("Continue? ")
    elif a==5:
      os.system("python3 snakegame.py")
    else:
      print("invalid choice")
    
    ch=input("Do you want to continue: (y/n)")
    if ch=='n':
      print("""
Thanks for visiting!

Credits:
    Utkarsh Luthra
    Mohd. Arslaan
    Poornima Ganguly
    Swati
      """)
  except:
    print("Oops, there was some problem...")