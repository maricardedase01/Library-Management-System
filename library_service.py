"""
LibraryService class for managing all library operations
"""

from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookNotAvailableError,
    MemberLimitExceededError,
    InvalidLoanError,
    OverdueLoanError
)
from book import Book
from member import Member
from loan import Loan
from datetime import datetime


class LibraryService:
    """Main service class for library management"""
    
    def __init__(self):
        """Initialize the library service"""
        self.books = {}  # book_id -> Book
        self.members = {}  # member_id -> Member
        self.loans = {}  # loan_id -> Loan
        self.loan_counter = 0
    
    # ===== BOOK MANAGEMENT =====
    
    def add_book(self, book_id, title, author, isbn, quantity):
        """
        Add a new book to the library
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
            isbn (str): ISBN of the book
            quantity (int): Number of copies to add
            
        Returns:
            Book: The created book object
        """
        if book_id in self.books:
            # Update quantity if book already exists
            self.books[book_id].total_quantity += quantity
            self.books[book_id].quantity += quantity
            return self.books[book_id]
        
        book = Book(book_id, title, author, isbn, quantity)
        self.books[book_id] = book
        return book
    
    def get_book(self, book_id):
        """
        Get a book by its ID
        
        Args:
            book_id (str): The book's unique identifier
            
        Returns:
            Book: The book object
            
        Raises:
            BookNotFoundError: If the book doesn't exist
        """
        if book_id not in self.books:
            raise BookNotFoundError(f"Book with ID '{book_id}' not found")
        return self.books[book_id]
    
    def search_books_by_title(self, title):
        """
        Search for books by title (partial match)
        
        Args:
            title (str): Title or partial title to search for
            
        Returns:
            list: List of matching books
        """
        title_lower = title.lower()
        return [book for book in self.books.values() 
                if title_lower in book.title.lower()]
    
    def search_books_by_author(self, author):
        """
        Search for books by author (partial match)
        
        Args:
            author (str): Author or partial author name to search for
            
        Returns:
            list: List of matching books
        """
        author_lower = author.lower()
        return [book for book in self.books.values() 
                if author_lower in book.author.lower()]
    
    def list_all_books(self):
        """
        Get list of all books in the library
        
        Returns:
            list: List of all book objects
        """
        return list(self.books.values())
    
    def list_available_books(self):
        """
        Get list of all available books
        
        Returns:
            list: List of available book objects
        """
        return [book for book in self.books.values() if book.is_available()]
    
    # ===== MEMBER MANAGEMENT =====
    
    def add_member(self, member_id, name, email, phone):
        """
        Register a new member to the library
        
        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member
            phone (str): Phone number of the member
            
        Returns:
            Member: The created member object
        """
        if member_id in self.members:
            raise ValueError(f"Member with ID '{member_id}' already exists")
        
        member = Member(member_id, name, email, phone)
        self.members[member_id] = member
        return member
    
    def get_member(self, member_id):
        """
        Get a member by their ID
        
        Args:
            member_id (str): The member's unique identifier
            
        Returns:
            Member: The member object
            
        Raises:
            MemberNotFoundError: If the member doesn't exist
        """
        if member_id not in self.members:
            raise MemberNotFoundError(f"Member with ID '{member_id}' not found")
        return self.members[member_id]
    
    def list_all_members(self):
        """
        Get list of all members in the library
        
        Returns:
            list: List of all member objects
        """
        return list(self.members.values())
    
    # ===== LOAN MANAGEMENT =====
    
    def borrow_book(self, member_id, book_id):
        """
        Borrow a book from the library
        
        Args:
            member_id (str): The member's ID
            book_id (str): The book's ID
            
        Returns:
            Loan: The created loan object
            
        Raises:
            MemberNotFoundError: If member doesn't exist
            BookNotFoundError: If book doesn't exist
            BookNotAvailableError: If book is not available
            MemberLimitExceededError: If member has reached the borrowing limit
        """
        member = self.get_member(member_id)
        book = self.get_book(book_id)
        
        # Check member's borrowing limit
        if not member.can_borrow_more():
            raise MemberLimitExceededError(
                f"Member '{member.name}' has reached the maximum borrowing limit of {Member.MAX_BOOKS_ALLOWED}"
            )
        
        # Check if book is available
        if not book.is_available():
            raise BookNotAvailableError(
                f"Book '{book.title}' is not available for borrowing"
            )
        
        # Create loan
        self.loan_counter += 1
        loan_id = f"LOAN_{self.loan_counter:05d}"
        loan = Loan(loan_id, book, member)
        
        # Update quantities
        book.decrease_quantity()
        member.add_borrowed_book(loan)
        self.loans[loan_id] = loan
        
        return loan
    
    def return_book(self, loan_id):
        """
        Return a borrowed book to the library
        
        Args:
            loan_id (str): The loan's ID
            
        Returns:
            Loan: The updated loan object
            
        Raises:
            InvalidLoanError: If loan doesn't exist or is already returned
        """
        if loan_id not in self.loans:
            raise InvalidLoanError(f"Loan with ID '{loan_id}' not found")
        
        loan = self.loans[loan_id]
        
        if loan.is_returned:
            raise InvalidLoanError(f"Loan '{loan_id}' has already been returned")
        
        # Check if overdue and warn
        if loan.is_overdue():
            overdue_days = loan.get_overdue_days()
            print(f"WARNING: Book '{loan.book.title}' is {overdue_days} day(s) overdue!")
        
        # Mark loan as returned
        loan.return_book()
        
        # Update quantities
        loan.book.increase_quantity()
        loan.member.remove_borrowed_book(loan)
        
        return loan
    
    def get_loan(self, loan_id):
        """
        Get a loan by its ID
        
        Args:
            loan_id (str): The loan's ID
            
        Returns:
            Loan: The loan object
            
        Raises:
            InvalidLoanError: If loan doesn't exist
        """
        if loan_id not in self.loans:
            raise InvalidLoanError(f"Loan with ID '{loan_id}' not found")
        return self.loans[loan_id]
    
    def get_member_active_loans(self, member_id):
        """
        Get all active loans for a member
        
        Args:
            member_id (str): The member's ID
            
        Returns:
            list: List of active loan objects
            
        Raises:
            MemberNotFoundError: If member doesn't exist
        """
        member = self.get_member(member_id)
        return member.get_borrowed_books()
    
    def get_overdue_loans(self, member_id=None):
        """
        Get all overdue loans
        
        Args:
            member_id (str, optional): If provided, get overdue loans for specific member
            
        Returns:
            list: List of overdue loan objects
        """
        overdue = []
        for loan in self.loans.values():
            if not loan.is_returned and loan.is_overdue():
                if member_id is None or loan.member.member_id == member_id:
                    overdue.append(loan)
        return overdue
    
    def list_all_loans(self):
        """
        Get list of all loans
        
        Returns:
            list: List of all loan objects
        """
        return list(self.loans.values())
    
    # ===== STATISTICS =====
    
    def get_library_stats(self):
        """
        Get overall statistics of the library
        
        Returns:
            dict: Dictionary containing library statistics
        """
        total_books = sum(book.total_quantity for book in self.books.values())
        available_books = sum(book.quantity for book in self.books.values())
        borrowed_books = total_books - available_books
        
        return {
            'total_unique_books': len(self.books),
            'total_book_copies': total_books,
            'available_copies': available_books,
            'borrowed_copies': borrowed_books,
            'total_members': len(self.members),
            'total_loans': len(self.loans),
            'active_loans': sum(1 for loan in self.loans.values() if not loan.is_returned),
            'overdue_loans': len(self.get_overdue_loans())
        }
