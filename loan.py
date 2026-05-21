"""Loan class for the Library Management System."""

from datetime import datetime, timedelta
import uuid


class Loan:
    """Represents a book loan in the library."""

    LOAN_DURATION_DAYS = 14  # Duration of a loan in days

    def __init__(self, member_id, isbn):
        """
        Initialize a Loan object.

        Args:
            member_id (str): ID of the member borrowing the book
            isbn (str): ISBN of the book being borrowed
        """
        self.loan_id = str(uuid.uuid4())[:8]
        self.member_id = member_id
        self.isbn = isbn
        self.borrow_date = datetime.now()
        self.due_date = self.borrow_date + timedelta(days=self.LOAN_DURATION_DAYS)
        self.return_date = None

    def __str__(self):
        """Return string representation of the loan."""
        return_status = f"Returned: {self.return_date.strftime('%Y-%m-%d')}" if self.return_date else "Not Returned"
        return f"Loan ID: {self.loan_id} | Member: {self.member_id} | ISBN: {self.isbn} | Due: {self.due_date.strftime('%Y-%m-%d')} | {return_status}"

    def __repr__(self):
        """Return detailed representation of the loan."""
        return f"Loan(id='{self.loan_id}', member_id='{self.member_id}', isbn='{self.isbn}', due_date='{self.due_date}')"

    def is_overdue(self):
        """
        Check if the loan is overdue (not returned and past due date).

        Returns:
            bool: True if overdue, False otherwise
        """
        if self.return_date:
            return False  # Returned books are not overdue
        return datetime.now() > self.due_date

    def get_days_overdue(self):
        """
        Get the number of days the loan is overdue.

        Returns:
            int: Number of days overdue, or 0 if not overdue
        """
        if not self.is_overdue():
            return 0
        return (datetime.now() - self.due_date).days

    def mark_returned(self):
        """Mark the book as returned."""
        self.return_date = datetime.now()

    def is_active(self):
        """
        Check if the loan is still active (not returned).

        Returns:
            bool: True if active, False if returned
        """
        return self.return_date is None

    def days_until_due(self):
        """
        Get the number of days until the book is due.

        Returns:
            int: Number of days until due, or negative if overdue
        """
        return (self.due_date - datetime.now()).days
