# Library Management System Using Python

**Author:** Aradhya Negi
**Course:** CSE1021: Introduction to Python and Problem Solving
**Submission Type:** Evaluated Course Project

-Introduction & Problem Statement
Managing books manually can lead to errors, lost information, and difficulty searching or updating records. This Python-based console application was developed to help store, manage, and retrieve book-related records efficiently. This digital solution enables faster operations, better tracking, and reliable data storage.

- Objectives & Features
The core objectives of this project include designing a functional menu-driven system, implementing CRUD operations, and permanently storing data using file handling to simulate real-world problem solving.

* **Add Book:** Add new book entries to the database.
* **Display Books:** View all available records.
* **Search & Update Book:** Lookup by book title or author, and modify existing records.
* **Delete Book:** Remove a book from the system.
* **Issue/Return Book:** Manage borrowing actions and track statuses.

-Implementation Details & Architecture
The system is built with a focus on usability, maintainability, and reliability. It utilizes modular function-based code, validation logic to prevent incorrect input, and conditional/loop structures for repeated execution. 

Data is stored persistently in text files:
* `books.txt`: Contains the master book list.
* `issued.txt`: Contains current issue records.

-Setup and Installation
1. Ensure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Open a terminal or command prompt in the project folder.
4. Run the application using the following command:
   `python projectcode.py`

--How to Use
Upon running the application, you will be greeted with the main menu. Type the number corresponding to the action you want to perform and hit Enter. The system will automatically generate the `books.txt` and `issued.txt` files to store your data once you start adding or issuing books.
* Using SQLite or JSON instead of text files for more robust storage.
* Implementing user authentication.
* Adding an overdue fine calculation feature.
