# Rate Limiter Simulator

## Project Description
A simple Rate limiter simulator that demonstrates CRUD operations, SQLite database integration, input validation, and negative test cases using pytest.
This project is designed to be beginner-friendly, testable, and interview-ready.
The script simulates rate limiting logic commonly used in APIs.

## Features

Flask REST API

Create, Read, Update, Delete (CRUD) tasks

SQLite database integration

Input validation & proper HTTP status codes

Negative test scenarios with pytest

Clean and maintainable project structure

## Project Structure
rate_limiter/   (project root)

├── app.py                  # Flask application

├── database.py             # Database CRUD logic (SQLite)

├── tasks.db                # SQLite database (auto-created)

├── tests/

│   └── test_rate_limiter.py  # Pytest test cases

├── requirements.txt

└── README.md

## Installation

1️. Prerequisites

   Python 3.9+ pip

Check installation:

   python --version
   
   pip --version

2️. Install Dependencies

   pip install -r requirements.txt
   
   Running the Application
   
   python app.py
   
## Expected output:

Running on http://127.0.0.1:5000

## terminal output screenshort 

<img width="1257" height="710" alt="Screenshot 2026-01-13 143740" src="https://github.com/user-attachments/assets/fdd8162d-666b-483b-8ad2-cd73608d39b9" />

## Conclusion

This project is a solid foundation for learning Flask backend development.

It follows best practices, handles edge cases correctly, and includes automated tests to ensure reliability and maintainability.
