# CBSE Computer Science Class 12th Project in Python
**Subject: Computer Science** <br>
**Language: Python** <br>
**Name of project:** English to Spanish Flashcards<br>
**AIM:** To create a project to help English speaking people in learning basic spanish words with dictionary, search and testing. Also, to display the scorecard of the previous tests taken from the database.


### Objectives
To create an application in Python3 Programming Language which uses the following:
1. Functions
2. Libraries and modules
3. File Handling
4. Database Connectivity with mysql-connector-python
5. MySQL

_The following repository folder only consists of the python part of the project and does not include the MySQL databases. Though, you can manually add data to it using a module in-built in the application._

### Project Overview

There are mainly four features in the given project:
1. To print a dictionary of words manually added by the user to test.
2. A program to add words
3. To give a test and get a score which gets saved
4. To search for words in your deck of words and phrases.

All of the above features are connected using a Main Menu program named as ```Main.py``` where the user can navigate throughout the features.
The scores and words/phrases are saved in a Database and can be accessed by selecting the respective options after running the ```Main.py``` file and choosing the option
The dictionary or deck can be accessed in the similar way.

Further, new words can be added either by using the main menu, or by going on the ```enteringData.py``` file.

The database used here is MySQL and is connected to the program using the ```mysql-connector-python``` library.

