# Library Management System

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, book_name):
        if book_id in self.books:
            print("Book ID already exists!")
        else:
            self.books[book_id] = {"name": book_name, "issued": False}
            print("Book added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available in library.")
        else:
            print("\nAvailable Books:")
            print("ID\tBook Name\tStatus")
            for book_id, details in self.books.items():
                status = "Issued" if details["issued"] else "Available"
                print(f"{book_id}\t{details['name']}\t{status}")

    def issue_book(self, book_id):
        if book_id in self.books:
            if not self.books[book_id]["issued"]:
                self.books[book_id]["issued"] = True
                print("Book issued successfully!")
            else:
                print("Book is already issued.")
        else:
            print("Book not found!")

    def return_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]["issued"]:
                self.books[book_id]["issued"] = False
                print("Book returned successfully!")
            else:
                print("Book was not issued.")
        else:
            print("Book not found!")


def main():
    library = Library()

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_id = input("Enter Book ID: ")
            book_name = input("Enter Book Name: ")
            library.add_book(book_id, book_name)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            book_id = input("Enter Book ID to issue: ")
            library.issue_book(book_id)

        elif choice == "4":
            book_id = input("Enter Book ID to return: ")
            library.return_book(book_id)

        elif choice == "5":
            print("Thank you! Exiting Library System.")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
