# Problem statement in description

class library:

    def __init__(self, listofbooks, library_name):
        self.library_name = library_name
        self.books = dict.fromkeys(listofbooks)
    
    def add_book(self):
        book = input("Enter book name: ")
        if book not in self.books:
            self.books[book] = None
        else:
            print("Book already available in library")

    def display_book(self):
        for book in self.books:
            print(book, "-", self.books[book])
        print()

    def lend_book(self):
        book = input("Enter book name: ")
        if book not in self.books:
            print("Sorry! Book not available")
        else:
            if self.books[book] is None:
                name = input("Enter lender's name: ")
                self.books[book] = name
            else:
                print("Sorry! Book is already issued")

    def return_book(self):
        book = input("Enter book name: ")
        if book not in self.books:
            print("Sorry! Book not available")
        else:
            if self.books[book] is None:
                print("Book not issued")
            else:
                self.books[book] = None

def mainmenu():
    books = ["Python", "C++", "Java", "C", "DSA", "CP"]
    
    delhi_library = library(books, "Delhi Library")
    
    while True:
        print("1. Display Book")
        print("2. Add Book")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice [1-5]: ")

        if choice == '1':
            delhi_library.display_book()
        elif choice == '2':
            delhi_library.add_book()
        elif choice == '3':
            delhi_library.lend_book()
        elif choice == '4':
            delhi_library.return_book()
        elif choice == '5':
            break
        else:
            print("Invalid choice")

mainmenu()

