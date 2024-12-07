# Create a class Book with a constructor that initializes the title. Override the del method to print a message when the object is deleted.
# Create and delete a Book object to demonstrate this.

class Book:
    def __init__(self, title):
        self.title = title
    def __del__(self):
        print(f"The book '{self.title}' is deleted.")

book1 = Book("Its Ends With Us")
del book1
#  The book 'Its Ends With Us' is deleted.
