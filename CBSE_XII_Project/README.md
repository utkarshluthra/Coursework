# Class XII CBSE Project
## Single Deck Flashcard Program

---

**Subject:** Computer Science <br>
**Language:** Python <br>
**Name of project:** Single Deck Flashcard Program
**AIM:** To create a program simulating the flashcard experience for better memorization and reference purpose capable of testing, searching and creating flashcards with complete connectivity to MySQL Database and including File Handling.

### Objectives
To create an application in Python3 Programming Language which uses the following:

1. Functions
2. Libraries and modules
3. File Handling
4. Database Connectivity with mysql-connector-python
5. MySQL


**The above file is a stand-alone file which can be run on any operating system and can be run immediately.**

### Introduction
A _flashcard_ is a piece of paper which has two sides which can be used in many different ways and are used as a tool for memorization and easy reference. The two sides of the card, Front and back, can be used in several ways, For E.g., Front can be for Question and Back for Answer. Or, it can be used as front for a certain word and the back for its meaning.

The wide applications of flashcards can be in:
1. Examination preparation
2. Learning new words of a language
3. Poetry and its meaning
... and many more places.

This project aims to create a program which can simulate the experience of flashcard making and testing on a computer using Python language. The user can create as many flashcards as necessary and test themselves on the basis of the cards created.

### Pre-requisites
To run this program, the following is required:
1. [Python-3 interpretter](https://www.python.org)
2. [MySQL Server should be installed on system](https://www.mysql.com)
3. MySQL-Python-Connector should be installed via pip or other sources. (for pip install type, ```pip install mysql-connector-python```) in the terminal or powershell.


The following repository folder only consists of the python part of the project and does not include the MySQL databases. Though, you can manually add data to it using a module in-built in the application.



### Project Overview
There are mainly the following features in the given project:

1. To create flashcards for with two faces, "Front" and "Back", along with a Card-id for each card.
2. To display the entire deck of flashcards created by the user.
3. To give a test from the flashcards created by the user for memorization.
4. To search for specific flashcards for reference purpose of the used by Text on front, back or by the card-id.
5. To obtain the result of all the previous tests given by the user stored in the database.
6. To export the result of the user from database to a printable textfile.
7. To automatically create all the necessary databases and tables.


All of the above features are connected using a Main Menu where the user can navigate throughout the features. The scores and faces of the cards are saved in a Database and can be accessed by selecting the respective options after running program and choosing the option deck can be accessed in the similar way.

All of the above features are basically functions defined individually and then collectively called on user request corresponding the user's choice on the Main Menu.


The database used here is MySQL and is connected to the program using the mysql-connector-python library.

### Further Scope
* Using object-oriented programming we can use each deck as a separate deck of flashcards which can be used for multiple purposes.
* Search can be made keyword based and throughout the databases.
* The UI and UX can be improved.
* Importing and Exporting features of Flashcards via File Handling.
* Documentation and comments can be added for smoother customization.
* Efficiency of the program can be increased.
* Program can be diveded into several modules for easier editing and released as a complete package.
