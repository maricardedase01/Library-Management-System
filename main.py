"""Main module - Interactive CLI for Library Management System."""

from library_service import LibraryService
from exceptions import (
    BookNotFound,
    MemberNotFound,
    InvalidLoan,
    BorrowingLimitExceeded,
    InsufficientInventory,
    BookAlreadyExists,
    MemberAlreadyExists,
)


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("    LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1.  Add a Book")
    print("2.  Search Books by Title")
    print("3.  Search Books by Author")
    print("4.  Search Books by ISBN")
    print("5.  List All Books")
    print("6.  Register a Member")
    print("7.  View All Members")
    print("8.  Borrow a Book")
    print("9.  Return a Book")
    print("10. View Active Loans")
    print("11. Check Overdue Loans")
    print("12. View Library Statistics")
    print("13. Exit")
    print("="*50)


def add_book(library):
    """Add a new book to the library."""
    print("\n--- Add a Book ---")
    try:
        isbn = input("Enter ISBN: ").strip()
        if not isbn:
            print("❌ ISBN cannot be empty")
            return
        title = input("Enter Title: ").strip()
        if not title:
            print("❌ Title cannot be empty")
            return
        author = input("Enter Author: ").strip()
        if not author:
            print("❌ Author cannot be empty")
            return
        quantity = int(input("Enter Quantity: ").strip())
        if quantity <= 0:
            print("❌ Quantity must be positive")
            return

        library.add_book(isbn, title, author, quantity)
        print(f"✅ Book '{title}' added successfully!")
    except BookAlreadyExists as e:
        print(f"❌ {e}")
    except ValueError:
        print("❌ Invalid input. Quantity must be a number.")


def search_by_title(library):
    """Search for books by title."""
    print("\n--- Search Books by Title ---")
    title = input("Enter Title to search: ").strip()
    if not title:
        print("❌ Title cannot be empty")
        return
    books = library.search_books_by_title(title)
    if books:
        print(f"\nFound {len(books)} book(s):")
        for book in books:
            print(f"  • {book}")
    else:
        print("❌ No books found with that title.")


def search_by_author(library):
    """Search for books by author."""
    print("\n--- Search Books by Author ---")
    author = input("Enter Author to search: ").strip()
    if not author:
        print("❌ Author cannot be empty")
        return
    books = library.search_books_by_author(author)
    if books:
        print(f"\nFound {len(books)} book(s):")
        for book in books:
            print(f"  • {book}")
    else:
        print("❌ No books found by that author.")


def search_by_isbn(library):
    """Search for a book by ISBN."""
    print("\n--- Search Books by ISBN ---")
    isbn = input("Enter ISBN to search: ").strip()
    if not isbn:
        print("❌ ISBN cannot be empty")
        return
    try:
        book = library.search_books_by_isbn(isbn)
        print(f"\n✅ Book found:")
        print(f"  {book}")
    except BookNotFound as e:
        print(f"❌ {e}")


def list_all_books(library):
    """Display all books in the library."""
    print("\n--- All Books in Library ---")
    books = library.get_all_books()
    if books:
        print(f"\nTotal books: {len(books)}\n")
        for book in books:
            print(f"  • {book}")
    else:
        print("❌ No books in the library yet.")


def register_member(library):
    """Register a new member."""
    print("\n--- Register a Member ---")
    try:
        name = input("Enter Name: ").strip()
        if not name:
            print("❌ Name cannot be empty")
            return
        email = input("Enter Email: ").strip()
        if not email:
            print("❌ Email cannot be empty")
            return

        member = library.register_member(name, email)
        print(f"✅ Member '{name}' registered successfully!")
        print(f"   Member ID: {member.member_id}")
    except MemberAlreadyExists as e:
        print(f"❌ {e}")


def view_all_members(library):
    """Display all registered members."""
    print("\n--- All Registered Members ---")
    members = library.get_all_members()
    if members:
        print(f"\nTotal members: {len(members)}\n")
        for member in members:
            print(f"  • {member}")
    else:
        print("❌ No members registered yet.")


def borrow_book(library):
    """Process a book borrow."""
    print("\n--- Borrow a Book ---")
    try:
        member_id = input("Enter Member ID: ").strip()
        if not member_id:
            print("❌ Member ID cannot be empty")
            return
        isbn = input("Enter Book ISBN: ").strip()
        if not isbn:
            print("❌ ISBN cannot be empty")
            return

        loan = library.borrow_book(member_id, isbn)
        member = library.get_member(member_id)
        book = library.search_books_by_isbn(isbn)
        print(f"✅ Book '{book.title}' borrowed successfully!")
        print(f"   Loan ID: {loan.loan_id}")
        print(f"   Due Date: {loan.due_date.strftime('%Y-%m-%d')}")
    except (MemberNotFound, BookNotFound) as e:
        print(f"❌ {e}")
    except (BorrowingLimitExceeded, InsufficientInventory) as e:
        print(f"❌ {e}")


def return_book(library):
    """Process a book return."""
    print("\n--- Return a Book ---")
    try:
        loan_id = input("Enter Loan ID: ").strip()
        if not loan_id:
            print("❌ Loan ID cannot be empty")
            return

        library.return_book(loan_id)
        print(f"✅ Book returned successfully!")
    except InvalidLoan as e:
        print(f"❌ {e}")


def view_active_loans(library):
    """Display all active loans."""
    print("\n--- Active Loans ---")
    loans = library.get_active_loans()
    if loans:
        print(f"\nTotal active loans: {len(loans)}\n")
        for loan in loans:
            print(f"  • {loan}")
    else:
        print("❌ No active loans.")


def check_overdue_loans(library):
    """Display all overdue loans."""
    print("\n--- Overdue Loans ---")
    overdue = library.get_overdue_loans()
    if overdue:
        print(f"\nTotal overdue loans: {len(overdue)}\n")
        for loan in overdue:
            days_overdue = loan.get_days_overdue()
            book = library.search_books_by_isbn(loan.isbn)
            print(f"  • {loan}")
            print(f"    → {days_overdue} day(s) overdue | Book: {book.title}")
    else:
        print("✅ No overdue loans!")


def view_statistics(library):
    """Display library statistics."""
    print("\n--- Library Statistics ---")
    stats = library.get_library_statistics()
    print(f"\n📊 Statistics:")
    print(f"   Total Unique Books: {stats['total_unique_books']}")
    print(f"   Total Book Copies: {stats['total_book_copies']}")
    print(f"   Available Copies: {stats['available_copies']}")
    print(f"   Total Members: {stats['total_members']}")
    print(f"   Active Loans: {stats['active_loans']}")
    print(f"   Overdue Loans: {stats['overdue_loans']}")


def main():
    """Main function to run the library management system."""
    library = LibraryService()

    print("\n" + "#"*50)
    print("#  Welcome to Library Management System  #")
    print("#"*50)

    while True:
        display_menu()
        choice = input("\nEnter your choice (1-13): ").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            search_by_title(library)
        elif choice == "3":
            search_by_author(library)
        elif choice == "4":
            search_by_isbn(library)
        elif choice == "5":
            list_all_books(library)
        elif choice == "6":
            register_member(library)
        elif choice == "7":
            view_all_members(library)
        elif choice == "8":
            borrow_book(library)
        elif choice == "9":
            return_book(library)
        elif choice == "10":
            view_active_loans(library)
        elif choice == "11":
            check_overdue_loans(library)
        elif choice == "12":
            view_statistics(library)
        elif choice == "13":
            print("\n✅ Thank you for using Library Management System!")
            print("#"*50 + "\n")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
