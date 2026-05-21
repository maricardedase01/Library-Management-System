"""Custom exceptions for the Library Management System."""


class LibraryException(Exception):
    """Base exception class for library operations."""
    pass


class BookNotFound(LibraryException):
    """Raised when a book is not found in the library."""
    pass


class MemberNotFound(LibraryException):
    """Raised when a member is not found in the library."""
    pass


class InvalidLoan(LibraryException):
    """Raised when a loan operation is invalid."""
    pass


class BorrowingLimitExceeded(LibraryException):
    """Raised when a member exceeds their borrowing limit."""
    pass


class InsufficientInventory(LibraryException):
    """Raised when there are not enough copies of a book."""
    pass


class BookAlreadyExists(LibraryException):
    """Raised when attempting to add a book that already exists."""
    pass


class MemberAlreadyExists(LibraryException):
    """Raised when attempting to register a member that already exists."""
    pass
