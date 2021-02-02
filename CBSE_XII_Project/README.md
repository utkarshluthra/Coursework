# Class XII CBSE Project
## Single Deck Flashcard Program

---

**Subject:** Computer Science
**Language:** Python
**Name of project:** English to Spanish Flashcards
**AIM:** To create a project to help English speaking people in learning basic spanish words with dictionary, search and testing. Also, to display the scorecard of the previous tests taken from the database.

### Objectives
To create an application in Python3 Programming Language which uses the following:

1. Functions
2. Libraries and modules
3. File Handling
4. Database Connectivity with mysql-connector-python
5. MySQL


**The above file is a stand-alone file which can be run on any operating system and can be run immediately.**

### Pre-requisites
To run this program, the following is required:
1. [Python-3 interpretter](https://www.python.org)
2. [MySQL Server should be installed on system](https://www.mysql.com)
3. MySQL-Python-Connector should be installed via pip or other sources. (for pip install type, ```pip install mysql-connector-python```) in the terminal or powershell.


The following repository folder only consists of the python part of the project and does not include the MySQL databases. Though, you can manually add data to it using a module in-built in the application.

### Project Overview
There are mainly four features in the given project:

1. To create flashcards for with two faces, "Front" and "Back", along with a Card-id for each card.
2. To display the entire deck of flashcards created by the user.
3. To give a test from the flashcards created by the user for memorization.
4. To search for specific flashcards for reference purpose of the used by Text on front, back or by the card-id.
5. To obtain the result of all the previous tests given by the user stored in the database.
6. To export the result of the user from database to a printable textfile.
7. To automatically create all the necessary databases and tables.


All of the above features are connected using a Main Menu where the user can navigate throughout the features. The scores and faces of the cards are saved in a Database and can be accessed by selecting the respective options after running program and choosing the option deck can be accessed in the similar way.


The database used here is MySQL and is connected to the program using the mysql-connector-python library.
