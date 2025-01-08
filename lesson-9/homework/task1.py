class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def borrow_book(self, member_name, book_title):
        member = next((member for member in self.members if member.name == member_name), None)
        book = next((book for book in self.books if book.title == book_title), None)

        if book is None:
            raise BookNotFoundException("Book not found in the library")

        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book is already borrowed")

        if len(member.borrowed_books) >= 3:
            raise MemberLimitExceededException("Member has reached the book borrowing limit")

        book.is_borrowed = True
        member.borrowed_books.append(book)

    def return_book(self, member_name, book_title):
        member = next((member for member in self.members if member.name == member_name), None)
        book = next((book for book in member.borrowed_books if book.title == book_title), None)

        if book is None:
            raise BookNotFoundException("Book not found in the member's borrowed books")

        book.is_borrowed = False
        member.borrowed_books.remove(book)

# Test your program
library = Library()

book1 = Book("Me Before you", "Jojo Moyes")
book2 = Book("Python Basics", "Fletcher Heisler")
book3 = Book("Python 3 OOP", "Dusty Phillips")

member1 = Member("Dalloris")
member2 = Member("Nozima")
member3 = Member("Barchinoy")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.add_member(member1)
library.add_member(member2)
library.add_member(member3)

try:
    library.borrow_book("Barchinoy", "Me Before")
    library.borrow_book("Barchinoy", "Python Basics")
    library.borrow_book("Barchinoy", "Python 3 OOP")  # This should raise MemberLimitExceededException
except (BookNotFoundException, BookAlreadyBorrowedException, MemberLimitExceededException) as e:
    print(e)