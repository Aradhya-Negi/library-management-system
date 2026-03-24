# -*- coding: utf-8 -*-
"""
Library Management System
By : Aradhya Negi
25BOE10086
"""

import os

# --- 1. Book Logic ---
class Book:
    def __init__(self, title, author, isbn, is_issued=False):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_issued = is_issued

    def issue(self):
        if not self.is_issued:
            self.is_issued = True
            return True
        return False

    def return_book(self):
        self.is_issued = False

    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - [{status}]"

# --- 2. Inventory Logic ---
class LibraryInventory:
    def __init__(self):
        self.books = []
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == str(isbn):
                return book
        return None

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def display_all(self):
        return self.books

    def load_data(self):
        issued_isbns = set()
        if os.path.exists("issued.txt"):
            with open("issued.txt", "r") as f:
                issued_isbns = set(line.strip() for line in f)

        if os.path.exists("books.txt"):
            with open("books.txt", "r") as f:
                for line in f:
                    parts = line.strip().split(',')
                    if len(parts) == 3:
                        title, author, isbn = parts
                        is_issued = isbn in issued_isbns
                        self.books.append(Book(title, author, isbn, is_issued))

    def save_data(self):
        with open("books.txt", "w") as f:
            for book in self.books:
                f.write(f"{book.title},{book.author},{book.isbn}\n")
        
        with open("issued.txt", "w") as f:
            for book in self.books:
                if book.is_issued:
                    f.write(f"{book.isbn}\n")

# --- 3. Main Menu Logic ---
def menu():
    inventory = LibraryInventory()
    while True:
        print("\n==== Library Menu ====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(Book(title, author, isbn))
            print("Book added!")

        elif choice == "2":
            isbn = input("Enter ISBN: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_data()
                print("Book issued!")
            else:
                print("Not available or invalid ISBN.")

        elif choice == "3":
            isbn = input("Enter ISBN: ")
            book = inventory.search_by_isbn(isbn)
            if book:
                book.return_book()
                inventory.save_data()
                print("Book returned!")
            else:
                print("Invalid ISBN.")

        elif choice == "4":
            books = inventory.display_all()
            if books:
                for b in books:
                    print(b)
            else:
                print("No books currently in the system.")

        elif choice == "5":
            title = input("Enter title: ")
            results = inventory.search_by_title(title)
            if results:
                for r in results:
                    print(r)
            else:
                print("No books found matching that title.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()