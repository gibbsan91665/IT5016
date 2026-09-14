import random # Added for potential future use or if needed by other parts not visible in snippet

# Simple Library System
#Wk7 Lab

# Define the classes
class Book:
  """Represents a book with a title, author, and availability status."""
  def __init__(self, title: str, author: str):
    self.title = title
    self.author = author
    self.is_borrowed = False # False means available, True means borrowed

  def __str__(self):
    status = "Borrowed" if self.is_borrowed else "Available"
    return f"{self.title} by {self.author} - {status}"

class Member:
  """Represents a library member with a name and a list of borrowed books."""
  def __init__(self, name: str):
    self.name = name
    self.borrowed_books = []

  def borrow_book(self, book: Book):
    self.borrowed_books.append(book)

  def return_book(self, book: Book):
    if book in self.borrowed_books:
      self.borrowed_books.remove(book)

  def __str__(self):
        titles = [b.title for b in self.borrowed_books]
        books_str = ", ".join(titles) if titles else "None"
        return f"Member: {self.name} | Borrowed: {books_str}"

class Library:
  """Manages collections of books and members, and handles borrowing/returning."""
  def __init__(self, name: str):
    self.name = name
    self.books = []
    self.members = []

  def add_book(self, book: Book):
    """Adds a book to the library collection"""
    self.books.append(book)

  def register_member(self, member: Member):
    self.members.append(member)
    print(f"Registered member: {member.name}")

  def display_books(self):
    """Lists all books with their availability status."""
    print(f"\n--- {self.name} Book Collection ---")
    if not self.books:
      print("No books in the library.")
      return

    for index, book in enumerate(self.books, start=1):
      print(f"{index}. {book}")
    print("---------------------------------")

  def borrow_book(self, member: Member, book_title: str):
    """Marks a book as borrowed if available and assigns it to a member."""
    for book in self.books:
      if book.title.lower() == book_title.lower():
        if book.is_borrowed:
          print(f"Sorry, '{book.title}' is currently borrowed.")
          return # Exit if already borrowed
        # If not borrowed, proceed to mark as borrowed and assign
        book.is_borrowed = True
        member.borrow_book(book)
        print(f"Success: '{book.title}' was borrowed by {member.name}.")
        return # Exit after successful borrowing

    print(f"Error: Book '{book_title}' not found in the library.")

  def return_book(self, member: Member, book_title: str): # Moved and indented into Library class
    """Marks a book as returned and available again"""
    for book in member.borrowed_books:
      if book.title.lower() == book_title.lower():
        book.is_borrowed = False
        member.return_book(book)
        print(f"Success: '{book.title}' was returned by {member.name}.")
        return

    print(f"Error: {member.name} has not borrowed a book titled '{book_title}'.")

# ----------------------------------------------------
# Demonstration / Testing
# ----------------------------------------------------
if __name__ == "__main__":
    # 1. Create a Library
    city_library = Library("City Central Library")

    # 2. Create and Add Books
    b1 = Book("1984", "George Orwell")
    b2 = Book("To Kill a Mockingbird", "Harper Lee")
    b3 = Book("The Hobbit", "J.R.R. Tolkien")

    city_library.add_book(b1)
    city_library.add_book(b2)
    city_library.add_book(b3)

    # 3. Create and Register Members
    alice = Member("Alice")
    bob = Member("Bob")
    city_library.register_member(alice)
    city_library.register_member(bob)

    # 4. Display all books initially
    city_library.display_books()

    # 5. Alice borrows "1984"
    city_library.borrow_book(alice, "1984")

    # 6. Bob tries to borrow the same book ("1984")
    city_library.borrow_book(bob, "1984")

    # 7. Check availability status again
    city_library.display_books()

    # 8. Alice returns "1984"
    city_library.return_book(alice, "1984")

    # 9. Final check of book status
    city_library.display_books()
