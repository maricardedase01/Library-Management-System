"""LibraryService class for managing library operations."""

from book import Book
from member import Member
from loan import Loan
from exceptions import (
    BookNotFound,
    MemberNotFound,
    InvalidLoan,
    BorrowingLimitExceeded,
    InsufficientInventory,
    BookAlreadyExists,
    MemberAlreadyExists,
)


class LibraryService:
    """Core service for library management operations."""

    def __init__(self):
        """Initialize the LibraryService."""
        self.books = {}  # Dictionary with ISBN as key
        self.members = {}  # Dictionary with member_id as key
        self.loans = {}  # Dictionary with loan_id as key

    # ==================== Book Operations ====================

    def add_book(self, isbn, title, author, quantity):
        """
        Add a new book to the library.

        Args:
            isbn (str): Unique ISBN identifier
            title (str): Book title
            author (str): Book author
            quantity (int): Number of copies

        Raises:
            BookAlreadyExists: If book with same ISBN exists
        """
        if isbn in self.books:
            raise BookAlreadyExists(f"Book with ISBN {isbn} already exists")
        self.books[isbn] = Book(isbn, title, author, quantity)

    def search_books_by_title(self, title):
        """
        Search for books by title.

        Args:
            title (str): Title to search for

        Returns:
            list: List of matching books
        """
        return [book for book in self.books.values() if title.lower() in book.title.lower()]

    def search_books_by_author(self, author):
        """
        Search for books by author.

        Args:
            author (str): Author name to search for

        Returns:
            list: List of matching books
        """
        return [book for book in self.books.values() if author.lower() in book.author.lower()]

    def search_books_by_isbn(self, isbn):
        """
        Search for a book by ISBN.

        Args:
            isbn (str): ISBN to search for

        Returns:
            Book: The matching book

        Raises:
            BookNotFound: If book not found
        """
        if isbn not in self.books:
            raise BookNotFound(f"Book with ISBN {isbn} not found")
        return self.books[isbn]

    def get_all_books(self):
        """
        Get all books in the library.

        Returns:
            list: List of all books
        """
        return list(self.books.values())

    # ==================== Member Operations ====================

    def register_member(self, name, email):
        """
        Register a new member in the library.

        Args:
            name (str): Member's name
            email (str): Member's email

        Returns:
            Member: The newly registered member

        Raises:
            MemberAlreadyExists: If member with same email exists
        """
        # Check if member with this email already exists
        for member in self.members.values():
            if member.email.lower() == email.lower():
                raise MemberAlreadyExists(f"Member with email {email} already exists")

        member = Member(name, email)
        self.members[member.member_id] = member
        return member

    def get_member(self, member_id):
        """
        Get a member by ID.

        Args:
            member_id (str): Member's ID

        Returns:
            Member: The member object

        Raises:
            MemberNotFound: If member not found
        """
        if member_id not in self.members:
            raise MemberNotFound(f"Member with ID {member_id} not found")
        return self.members[member_id]

    def get_all_members(self):
        """
        Get all registered members.

        Returns:
            list: List of all members
        """
        return list(self.members.values())

    # ==================== Loan Operations ====================

    def borrow_book(self, member_id, isbn):
        """
        Process a book loan.

        Args:
            member_id (str): ID of the member borrowing
            isbn (str): ISBN of the book to borrow

        Returns:
            Loan: The created loan object

        Raises:
            MemberNotFound: If member doesn't exist
            BookNotFound: If book doesn't exist
            BorrowingLimitExceeded: If member reached limit
            InsufficientInventory: If no copies available
        """
        member = self.get_member(member_id)
        book = self.search_books_by_isbn(isbn)

        if not member.can_borrow():
            raise BorrowingLimitExceeded(
                f"Member {member.name} has reached maximum borrowing limit of {Member.MAX_BOOKS}"
            )

        if not book.is_available():
            raise InsufficientInventory(f"No copies of '{book.title}' are available")

        # Create loan and update inventory
        loan = Loan(member_id, isbn)
        self.loans[loan.loan_id] = loan
        member.add_borrowed_book(isbn)
        book.decrease_quantity(1)

        return loan

    def return_book(self, loan_id):
        """
        Process a book return.

        Args:
            loan_id (str): ID of the loan to close

        Raises:
            InvalidLoan: If loan not found or already returned
        """
        if loan_id not in self.loans:
            raise InvalidLoan(f"Loan with ID {loan_id} not found")

        loan = self.loans[loan_id]

        if not loan.is_active():
            raise InvalidLoan(f"Loan {loan_id} has already been returned")

        # Mark loan as returned and update member and book
        loan.mark_returned()
        member = self.get_member(loan.member_id)
        book = self.search_books_by_isbn(loan.isbn)

        member.remove_borrowed_book(loan.isbn)
        book.increase_quantity(1)

    def get_active_loans(self):
        """
        Get all active (not yet returned) loans.

        Returns:
            list: List of active loans
        """
        return [loan for loan in self.loans.values() if loan.is_active()]

    def get_overdue_loans(self):
        """
        Get all overdue loans.

        Returns:
            list: List of overdue loans
        """
        return [loan for loan in self.loans.values() if loan.is_overdue()]

    def get_member_loans(self, member_id):
        """
        Get all active loans for a specific member.

        Args:
            member_id (str): Member's ID

        Returns:
            list: List of member's active loans
        """
        return [loan for loan in self.loans.values() if loan.member_id == member_id and loan.is_active()]

    # ==================== Statistics ====================

    def get_library_statistics(self):
        """
        Get comprehensive library statistics.

        Returns:
            dict: Dictionary containing library statistics
        """
        total_books = len(self.books)
        total_copies = sum(book.quantity for book in self.books.values())
        total_members = len(self.members)
        active_loans = len(self.get_active_loans())
        overdue_loans = len(self.get_overdue_loans())

        return {
            "total_unique_books": total_books,
            "total_book_copies": total_copies,
            "total_members": total_members,
            "active_loans": active_loans,
            "overdue_loans": overdue_loans,
            "available_copies": sum(book.quantity for book in self.books.values()),
        }
