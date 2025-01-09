Library Management System API
Project Overview

The Library Management System API is a backend application built with Django and Django REST Framework (DRF). The system allows library staff and users to manage books, users, and transactions such as borrowing and returning books. The API provides CRUD operations for books and users, and includes endpoints for checking out and returning books. This project simulates a real-world environment of managing library resources efficiently.
Features

    Books Management (CRUD): Allows you to create, read, update, and delete books.
    Users Management (CRUD): Allows you to manage library users.
    Check-out and Return Books: Users can check out books and return them, updating the availability of books in the library.
    View Available Books: Allows users to view books that are available for borrowing.

Technologies Used

    Django (version 3.x)
    Django REST Framework (DRF) (version 3.x)
    SQLite (default database)
    Django CORS Headers for Cross-Origin Resource Sharing (CORS) setup.
    Django Authentication for managing user login and permissions.

Installation

Follow these steps to set up the project locally:
Step 1: Clone the Repository

git clone git@github.com:Mohammed-nasr7/-Library-Management-System-API.git
cd library-management-system

Step 2: Set up a Virtual Environment

Create and activate a virtual environment:

python -m venv venv

On Windows:

venv\Scripts\activate



Step 3: Install the Requirements

Install the required dependencies:

pip install -r requirements.txt

Step 4: Apply Migrations

Run the migrations to set up the database:

python manage.py migrate

Step 5: Run the Server

Start the development server:

python manage.py runserver

The API will be available at http://127.0.0.1:8000.
API Endpoints
1. Books Endpoints

    GET /api/books/: View all books.
    POST /api/books/: Add a new book.
    PUT /api/books/{id}/: Update an existing book.
    DELETE /api/books/{id}/: Delete a book.

2. Users Endpoints

    GET /api/users/: View all users.
    POST /api/users/: Add a new user.
    PUT /api/users/{id}/: Update user details.
    DELETE /api/users/{id}/: Delete a user.

3. Check-out and Return Books

    POST /api/transactions/checkout/: Check out a book (reduce available copies).
    POST /api/transactions/return/: Return a checked-out book (increase available copies).

4. Available Books Endpoint

    GET /api/books/available_books/: View only books with available copies.

Authentication

    The system uses Django's built-in authentication to manage users.
    Users need to log in to access their borrowing history and perform operations like checking out and returning books.

Example Usage
1. Check Out a Book

POST /api/transactions/checkout/
{
    "book_id": 1
}

Response:

{
    "id": 1,
    "user": 1,
    "book": 1,
    "checked_out_date": "2025-01-09T00:00:00Z",
    "returned_date": null
}

2. Return a Book

POST /api/transactions/return/
{
    "transaction_id": 1
}

Response:

{
    "id": 1,
    "user": 1,
    "book": 1,
    "checked_out_date": "2025-01-09T00:00:00Z",
    "returned_date": "2025-01-10T00:00:00Z"
}

Challenges Faced

    Handling book availability when checking out and returning books. It was challenging to ensure that the number of copies was properly updated when a book was borrowed or returned.
    Implementing proper error handling for cases like invalid book IDs or trying to return a book that wasn’t checked out.

Future Improvements

    Add user roles (e.g., Admin, Member).
    Implement overdue tracking and penalty for late returns.
    Add email notifications for overdue books or when a book becomes available.
    Improve pagination and filtering options for the books list.

Conclusion

This Library Management System API project successfully simulates a library system where users can check out and return books, and manage library resources efficiently. The project leverages Django and Django REST Framework to provide a RESTful API for managing books and users.

Thank you for reviewing this project