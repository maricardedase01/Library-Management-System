"""
Member class for the Library Management System
"""


class Member:
    """Represents a library member"""
    
    MAX_BOOKS_ALLOWED = 5
    
    def __init__(self, member_id, name, email, phone):
        """
        Initialize a member with given details
        
        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member
            phone (str): Phone number of the member
        """
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone
        self.borrowed_books = []
    
    def add_borrowed_book(self, loan):
        """Add a borrowed book to member's list"""
        self.borrowed_books.append(loan)
    
    def remove_borrowed_book(self, loan):
        """Remove a returned book from member's list"""
        if loan in self.borrowed_books:
            self.borrowed_books.remove(loan)
            return True
        return False
    
    def get_borrowed_books_count(self):
        """Get the count of currently borrowed books"""
        return len(self.borrowed_books)
    
    def can_borrow_more(self):
        """Check if the member can borrow more books"""
        return self.get_borrowed_books_count() < self.MAX_BOOKS_ALLOWED
    
    def get_borrowed_books(self):
        """Get list of currently borrowed books"""
        return self.borrowed_books.copy()
    
    def __str__(self):
        """String representation of the member"""
        return (f"Member(ID: {self.member_id}, Name: {self.name}, "
                f"Email: {self.email}, Phone: {self.phone}, "
                f"Borrowed: {self.get_borrowed_books_count()}/{self.MAX_BOOKS_ALLOWED})")
    
    def __repr__(self):
        """Developer-friendly representation of the member"""
        return self.__str__()
