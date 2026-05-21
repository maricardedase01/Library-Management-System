"""
Loan class for the Library Management System
"""

from datetime import datetime, timedelta


class Loan:
    """Represents a book loan transaction"""
    
    LOAN_DURATION_DAYS = 14
    
    def __init__(self, loan_id, book, member, loan_date=None):
        """
        Initialize a loan with given details
        
        Args:
            loan_id (str): Unique identifier for the loan
            book (Book): The book being loaned
            member (Member): The member borrowing the book
            loan_date (datetime): The date of the loan (defaults to today)
        """
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.loan_date = loan_date or datetime.now()
        self.due_date = self.loan_date + timedelta(days=self.LOAN_DURATION_DAYS)
        self.return_date = None
        self.is_returned = False
    
    def return_book(self, return_date=None):
        """
        Mark the book as returned
        
        Args:
            return_date (datetime): The date of return (defaults to today)
            
        Returns:
            bool: True if return was successful
        """
        if not self.is_returned:
            self.return_date = return_date or datetime.now()
            self.is_returned = True
            return True
        return False
    
    def is_overdue(self, check_date=None):
        """
        Check if the loan is overdue
        
        Args:
            check_date (datetime): Date to check against (defaults to today)
            
        Returns:
            bool: True if the loan is overdue
        """
        if self.is_returned:
            return False
        check_date = check_date or datetime.now()
        return check_date > self.due_date
    
    def get_overdue_days(self, check_date=None):
        """
        Get the number of overdue days
        
        Args:
            check_date (datetime): Date to check against (defaults to today)
            
        Returns:
            int: Number of overdue days (0 if not overdue)
        """
        if not self.is_overdue(check_date):
            return 0
        check_date = check_date or datetime.now()
        return (check_date - self.due_date).days
    
    def get_days_remaining(self, check_date=None):
        """
        Get the number of days remaining before due date
        
        Args:
            check_date (datetime): Date to check against (defaults to today)
            
        Returns:
            int: Number of days remaining (negative if overdue)
        """
        check_date = check_date or datetime.now()
        return (self.due_date - check_date).days
    
    def __str__(self):
        """String representation of the loan"""
        status = "Returned" if self.is_returned else "Active"
        return (f"Loan(ID: {self.loan_id}, Book: {self.book.title}, "
                f"Member: {self.member.name}, Status: {status}, "
                f"Due: {self.due_date.date()})")
    
    def __repr__(self):
        """Developer-friendly representation of the loan"""
        return self.__str__()
