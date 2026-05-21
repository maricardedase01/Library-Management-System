"""
Custom exceptions for the Library Management System
"""


class LibraryException(Exception):
    """Base exception for library operations"""
    pass


class BookNotFoundError(LibraryException):
    """Raised when a book is not found in the library"""
    pass


class MemberNotFoundError(LibraryException):
    """Raised when a member is not found in the library"""
    pass


class BookNotAvailableError(LibraryException):
    """Raised when a book is not available for loan"""
    pass


class MemberLimitExceededError(LibraryException):
    """Raised when a member exceeds their loan limit"""
    pass


class InvalidLoanError(LibraryException):
    """Raised when loan operation is invalid"""
    pass


class OverdueLoanError(LibraryException):
    """Raised when trying to perform operations on overdue loans"""
    pass
