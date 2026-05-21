"""Member class for the Library Management System."""

from datetime import datetime
import uuid


class Member:
    """Represents a library member."""

    MAX_BOOKS = 5  # Maximum books a member can borrow

    def __init__(self, name, email):
        """
        Initialize a Member object.

        Args:
            name (str): Member's full name
            email (str): Member's email address
        """
        self.member_id = str(uuid.uuid4())[:8]
        self.name = name
        self.email = email
        self.joined_at = datetime.now()
        self.borrowed_books = []  # List of ISBNs currently borrowed

    def __str__(self):
        """Return string representation of the member."""
        return f"ID: {self.member_id} | Name: {self.name} | Email: {self.email} | Books Borrowed: {len(self.borrowed_books)}"

    def __repr__(self):
        """Return detailed representation of the member."""
        return f"Member(id='{self.member_id}', name='{self.name}', email='{self.email}')"

    def can_borrow(self):
        """
        Check if the member can borrow more books.

        Returns:
            bool: True if member can borrow, False otherwise
        """
        return len(self.borrowed_books) < self.MAX_BOOKS

    def add_borrowed_book(self, isbn):
        """
        Add a borrowed book to the member's list.

        Args:
            isbn (str): ISBN of the book

        Raises:
            ValueError: If member has reached borrowing limit
        """
        if not self.can_borrow():
            raise ValueError(f"Member has reached maximum borrowing limit of {self.MAX_BOOKS}")
        self.borrowed_books.append(isbn)

    def remove_borrowed_book(self, isbn):
        """
        Remove a returned book from the member's list.

        Args:
            isbn (str): ISBN of the book

        Raises:
            ValueError: If book is not in borrowed list
        """
        if isbn not in self.borrowed_books:
            raise ValueError(f"Book with ISBN {isbn} is not borrowed by this member")
        self.borrowed_books.remove(isbn)

    def get_borrowed_count(self):
        """Get the number of books currently borrowed by this member."""
        return len(self.borrowed_books)
