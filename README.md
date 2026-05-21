# Library Management System

A comprehensive Python-based library management system that enables efficient tracking of books, members, and loan transactions.

## Features

✨ **Core Features:**
- **Book Management**: Add, search, and manage library inventory with ISBN, title, author, and quantity tracking
- **Member Management**: Register and manage library members with borrowing limits (max 5 books per member)
- **Loan Management**: Track book loans with automatic due date calculation (14 days)
- **Overdue Detection**: Automatic tracking and reporting of overdue loans
- **Search Functionality**: Find books by title, author, or ISBN
- **Statistics Dashboard**: View comprehensive library statistics and reports
- **User-Friendly CLI**: Interactive menu-driven interface

## Project Structure

```
├── book.py              # Book class and inventory management
├── member.py            # Member class for library users
├── loan.py              # Loan class with due date tracking
├── exceptions.py        # Custom exception classes
├── library_service.py   # Core service with all operations
├── main.py              # Interactive CLI menu
└── README.md            # This file
```

## Requirements

- Python 3.7+
- No external dependencies (uses only standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/maricardedase01/Library-Management-System.git
cd Library-Management-System
```

2. Run the application:
```bash
python main.py
```

## Usage

Once you run `python main.py`, you'll see an interactive menu with the following options:

### Menu Options:

1. **Add a Book** - Add a new book to the library inventory
2. **Search Books by Title** - Find books by title
3. **Search Books by Author** - Find books by author
4. **Search Books by ISBN** - Find books by ISBN
5. **List All Books** - Display all books in the library
6. **Register a Member** - Add a new member to the library
7. **View All Members** - Display all registered members
8. **Borrow a Book** - Member borrows a book from the library
9. **Return a Book** - Member returns a borrowed book
10. **View Active Loans** - Display all active loans
11. **Check Overdue Loans** - View books that are overdue
12. **View Library Statistics** - Get comprehensive library stats
13. **Exit** - Close the application

## Example Workflow

```
1. Start the application: python main.py
2. Add books to the library (Option 1)
3. Register library members (Option 6)
4. Process book loans (Option 8)
5. Track loan status (Options 10, 11)
6. Process returns (Option 9)
7. View statistics (Option 12)
```

## Class Descriptions

### Book Class (`book.py`)
Represents a book in the library with:
- ISBN (unique identifier)
- Title
- Author
- Quantity (total copies available)

### Member Class (`member.py`)
Represents a library member with:
- Member ID
- Name
- Email
- Join date
- Borrowing limit (max 5 books)

### Loan Class (`loan.py`)
Represents a book loan with:
- Loan ID
- Member ID
- ISBN
- Borrow date
- Due date (14 days from borrow date)
- Return date (None if not yet returned)

### LibraryService Class (`library_service.py`)
Core service providing:
- Book CRUD operations
- Member management
- Loan processing
- Search functionality
- Statistics and reporting

## Error Handling

The system includes custom exceptions for:
- Book not found
- Member not found
- Invalid loan operations
- Inventory management errors
- Borrowing limit violations

## Data Persistence

Currently, the system stores data in memory during runtime. For production use, consider implementing:
- Database storage (SQLite, PostgreSQL)
- File-based persistence (JSON, CSV)
- Cloud storage integration

## Future Enhancements

- Database integration (SQLite/PostgreSQL)
- Fine calculation for overdue books
- Book reservation system
- Member notifications
- Advanced reporting and analytics
- Web interface (Flask/Django)
- User authentication system

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Author

Created by maricardedase01

## Support

For issues or questions, please open an issue on the GitHub repository.
