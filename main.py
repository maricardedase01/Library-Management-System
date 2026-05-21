"""
Main menu interface for the Library Management System
"""

from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookNotAvailableError,
    MemberLimitExceededError,
    InvalidLoanError
)
from datetime import datetime


class LibraryManagementSystem:
    """Command-line interface for the library management system"""
    
    def __init__(self):
        """Initialize the library management system"""
        self.library = LibraryService()
    
    def display_menu(self):
        """Display the main menu"""
        print("\n" + "="*60)
        print("         LIBRARY MANAGEMENT SYSTEM")
        print("="*60)
        print("\n1.  Add Book")
        print("2.  Search Book by Title")
        print("3.  Search Book by Author")
        print("4.  List All Books")
        print("5.  List Available Books")
        print("6.  Register Member")
        print("7.  List All Members")
        print("8.  Borrow Book")
        print("9.  Return Book")
        print("10. View Member's Active Loans")
        print("11. View Overdue Loans")
        print("12. Library Statistics")
        print("13. Exit")
        print("="*60)
    
    def add_book(self):
        """Add a new book to the library"""
        print("\n--- Add New Book ---")
        try:
            book_id = input("Enter Book ID: ").strip()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            isbn = input("Enter ISBN: ").strip()
            
            try:
                quantity = int(input("Enter Quantity: ").strip())
                if quantity <= 0:
                    print("❌ Quantity must be greater than 0")
                    return
            except ValueError:
                print("❌ Invalid quantity. Please enter a number.")
                return
            
            book = self.library.add_book(book_id, title, author, isbn, quantity)
            print(f"✅ Book added successfully!")
            print(f"   {book}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def search_book_by_title(self):
        """Search for books by title"""
        print("\n--- Search Books by Title ---")
        try:
            title = input("Enter Title (or partial title): ").strip()
            if not title:
                print("❌ Title cannot be empty")
                return
            
            books = self.library.search_books_by_title(title)
            if not books:
                print(f"❌ No books found with title containing '{title}'")
            else:
                print(f"\n✅ Found {len(books)} book(s):")
                for i, book in enumerate(books, 1):
                    print(f"   {i}. {book}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def search_book_by_author(self):
        """Search for books by author"""
        print("\n--- Search Books by Author ---")
        try:
            author = input("Enter Author Name (or partial name): ").strip()
            if not author:
                print("❌ Author name cannot be empty")
                return
            
            books = self.library.search_books_by_author(author)
            if not books:
                print(f"❌ No books found by author '{author}'")
            else:
                print(f"\n✅ Found {len(books)} book(s):")
                for i, book in enumerate(books, 1):
                    print(f"   {i}. {book}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def list_all_books(self):
        """List all books in the library"""
        print("\n--- All Books in Library ---")
        try:
            books = self.library.list_all_books()
            if not books:
                print("❌ No books in the library")
            else:
                print(f"\n✅ Total Books: {len(books)}")
                for i, book in enumerate(books, 1):
                    print(f"   {i}. {book}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def list_available_books(self):
        """List all available books"""
        print("\n--- Available Books ---")
        try:
            books = self.library.list_available_books()
            if not books:
                print("❌ No available books")
            else:
                print(f"\n✅ Available Books: {len(books)}")
                for i, book in enumerate(books, 1):
                    print(f"   {i}. {book}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def register_member(self):
        """Register a new member"""
        print("\n--- Register New Member ---")
        try:
            member_id = input("Enter Member ID: ").strip()
            name = input("Enter Full Name: ").strip()
            email = input("Enter Email: ").strip()
            phone = input("Enter Phone Number: ").strip()
            
            if not all([member_id, name, email, phone]):
                print("❌ All fields are required")
                return
            
            member = self.library.add_member(member_id, name, email, phone)
            print(f"✅ Member registered successfully!")
            print(f"   {member}")
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def list_all_members(self):
        """List all members"""
        print("\n--- All Members ---")
        try:
            members = self.library.list_all_members()
            if not members:
                print("❌ No members registered")
            else:
                print(f"\n✅ Total Members: {len(members)}")
                for i, member in enumerate(members, 1):
                    print(f"   {i}. {member}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def borrow_book(self):
        """Borrow a book"""
        print("\n--- Borrow Book ---")
        try:
            member_id = input("Enter Member ID: ").strip()
            book_id = input("Enter Book ID: ").strip()
            
            if not member_id or not book_id:
                print("❌ Member ID and Book ID cannot be empty")
                return
            
            loan = self.library.borrow_book(member_id, book_id)
            print(f"✅ Book borrowed successfully!")
            print(f"   {loan}")
            print(f"   Due Date: {loan.due_date.date()}")
        except MemberNotFoundError as e:
            print(f"❌ {e}")
        except BookNotFoundError as e:
            print(f"❌ {e}")
        except BookNotAvailableError as e:
            print(f"❌ {e}")
        except MemberLimitExceededError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def return_book(self):
        """Return a borrowed book"""
        print("\n--- Return Book ---")
        try:
            loan_id = input("Enter Loan ID: ").strip()
            
            if not loan_id:
                print("❌ Loan ID cannot be empty")
                return
            
            loan = self.library.return_book(loan_id)
            print(f"✅ Book returned successfully!")
            print(f"   {loan}")
            
            if loan.is_overdue():
                overdue_days = loan.get_overdue_days()
                print(f"   ⚠️  Book was {overdue_days} day(s) overdue")
            else:
                days_early = (loan.due_date - loan.return_date).days
                if days_early >= 0:
                    print(f"   ✓ Returned {days_early} day(s) early")
        except InvalidLoanError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def view_member_loans(self):
        """View member's active loans"""
        print("\n--- Member's Active Loans ---")
        try:
            member_id = input("Enter Member ID: ").strip()
            
            if not member_id:
                print("❌ Member ID cannot be empty")
                return
            
            loans = self.library.get_member_active_loans(member_id)
            member = self.library.get_member(member_id)
            
            print(f"\n✅ Active Loans for {member.name}:")
            if not loans:
                print("   No active loans")
            else:
                for i, loan in enumerate(loans, 1):
                    days_remaining = loan.get_days_remaining()
                    status = "OVERDUE ⚠️" if days_remaining < 0 else f"{days_remaining} days left"
                    print(f"   {i}. {loan.loan_id} - {loan.book.title}")
                    print(f"      Status: {status}")
        except MemberNotFoundError as e:
            print(f"❌ {e}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def view_overdue_loans(self):
        """View overdue loans"""
        print("\n--- Overdue Loans ---")
        try:
            overdue_loans = self.library.get_overdue_loans()
            
            if not overdue_loans:
                print("✅ No overdue loans")
            else:
                print(f"\n⚠️  Total Overdue Loans: {len(overdue_loans)}")
                for i, loan in enumerate(overdue_loans, 1):
                    overdue_days = loan.get_overdue_days()
                    print(f"   {i}. {loan.loan_id}")
                    print(f"      Member: {loan.member.name} ({loan.member.email})")
                    print(f"      Book: {loan.book.title}")
                    print(f"      Overdue by: {overdue_days} day(s)")
                    print()
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def display_statistics(self):
        """Display library statistics"""
        print("\n--- Library Statistics ---")
        try:
            stats = self.library.get_library_stats()
            
            print(f"\n✅ Library Statistics:")
            print(f"   Total Unique Books: {stats['total_unique_books']}")
            print(f"   Total Book Copies: {stats['total_book_copies']}")
            print(f"   Available Copies: {stats['available_copies']}")
            print(f"   Borrowed Copies: {stats['borrowed_copies']}")
            print(f"   Total Members: {stats['total_members']}")
            print(f"   Total Loans: {stats['total_loans']}")
            print(f"   Active Loans: {stats['active_loans']}")
            print(f"   Overdue Loans: {stats['overdue_loans']}")
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def run(self):
        """Run the main menu loop"""
        print("\n" + "="*60)
        print("Welcome to Library Management System!")
        print("="*60)
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-13): ").strip()
            
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.search_book_by_title()
            elif choice == '3':
                self.search_book_by_author()
            elif choice == '4':
                self.list_all_books()
            elif choice == '5':
                self.list_available_books()
            elif choice == '6':
                self.register_member()
            elif choice == '7':
                self.list_all_members()
            elif choice == '8':
                self.borrow_book()
            elif choice == '9':
                self.return_book()
            elif choice == '10':
                self.view_member_loans()
            elif choice == '11':
                self.view_overdue_loans()
            elif choice == '12':
                self.display_statistics()
            elif choice == '13':
                print("\n" + "="*60)
                print("Thank you for using Library Management System!")
                print("="*60 + "\n")
                break
            else:
                print("❌ Invalid choice. Please enter a number between 1 and 13.")


if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.run()
