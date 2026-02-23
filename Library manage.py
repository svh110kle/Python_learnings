class Library:
    def __init__(self):
        self.no_of_books =[]
        
    def add_book(self,book):
        self.no_of_books.append(book)
        
    def remove_book(self,book):
        self.no_of_books.remove(book)
        
    def display_books(self):
        print("Books in the library:")
        for book in self.no_of_books:
            print(book)
            
    def number_of_books(self):
        return len(self.no_of_books)
    
library = Library()
library.add_book("Python Programming")
library.add_book("Data Structures and Algorithms")
library.add_book("Machine Learning")
library.display_books()
print(f"Number of books in the library: {library.number_of_books()}")
library.remove_book("Data Structures and Algorithms")
library.display_books()