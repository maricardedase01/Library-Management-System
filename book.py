"""Book class for the Library Management System."""

from datetime import datetime


class Book:
    """Represents a book in the library."""

    def __init__(self, isbn, title, author, quantity):
        """
        Initialize a Book object.

        Args:
            isbn (str): Unique ISBN identifier
            title (str): Book title
            author (str): Book author
            quantity (int): Number of copies available
        """
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity
        self.created_at = datetime.now()

    def __str__(self):
        """Return string representation of the book."""
        return f"ISBN: {self.isbn} | Title: {self.title} | Author: {self.author} | Quantity: {self.quantity}"

    def __repr__(self):
        """Return detailed representation of the book."""
        return f"Book(isbn='{self.isbn}', title='{self.title}', author='{self.author}', quantity={self.quantity})"

    def increase_quantity(self, amount):
        """
        Increase the quantity of the book.

        Args:
            amount (int): Number of copies to add
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.quantity += amount

    def decrease_quantity(self, amount):
        """
        Decrease the quantity of the book.

        Args:
            amount (int): Number of copies to remove

        Raises:
            ValueError: If quantity would go negative
        """
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.quantity < amount:
            raise ValueError(f"Cannot decrease quantity. Available: {self.quantity}, Requested: {amount}")
        self.quantity -= amount

    def is_available(self):
        """Check if the book is available for borrowing."""
        return self.quantity > 0
