"""
Book class for the Library Management System
"""


class Book:
    """Represents a book in the library"""
    
    def __init__(self, book_id, title, author, isbn, quantity):
        """
        Initialize a book with given details
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
            isbn (str): ISBN of the book
            quantity (int): Available quantity of the book
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.total_quantity = quantity
    
    def decrease_quantity(self):
        """Decrease the available quantity when a book is borrowed"""
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False
    
    def increase_quantity(self):
        """Increase the available quantity when a book is returned"""
        self.quantity += 1
        return True
    
    def is_available(self):
        """Check if the book is available for borrowing"""
        return self.quantity > 0
    
    def get_available_count(self):
        """Get the current available count of the book"""
        return self.quantity
    
    def __str__(self):
        """String representation of the book"""
        return (f"Book(ID: {self.book_id}, Title: {self.title}, "
                f"Author: {self.author}, ISBN: {self.isbn}, "
                f"Available: {self.quantity}/{self.total_quantity})")
    
    def __repr__(self):
        """Developer-friendly representation of the book"""
        return self.__str__()
