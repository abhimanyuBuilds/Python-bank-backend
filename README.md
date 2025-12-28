**Python Bank Backend**

A backend Bank Management System built using Python and PostgreSQL, designed to simulate real-world banking operations such as customer management, account handling, transactions, beneficiaries, and loans. The project is implemented using Object-Oriented Programming (OOP) principles and follows a service-based architecture for clean, modular, and maintainable code. This project also includes a self-designed relational database schema, created independently in PostgreSQL, following real-world banking data modeling practices.

**Features**

. Customer management (create and validate customers)
. Account creation and account management
. Deposit and withdrawal operations with balance validation
. Transaction handling and tracking
. Object-Oriented Programming (OOP)
. Entity-based classes (Customer, Account, Transaction, Loan)
. Encapsulation of business logic
. Reusable and modular design
. Custom exception handling
. PostgreSQL database integration
. Scalable backend architecture

**Project Structure**

bank_project/
│
├── bank/
│   ├── models/          # OOP-based data models
│   ├── services/        # Business logic layer
│   ├── exceptions/      # Custom exceptions
│   ├── utils/           # Database connection & helpers
│   └── __main__.py      # Application entry point
│
├── requirements.txt
└── README.md

**Future Enhancements**

. This project will be extended further with
. Django and Django REST Framework integration
. Conversion of backend logic into RESTful APIs
. Authentication and authorization (JWT)
. Docker containerization
. AWS deployment (EC2, RDS)
. Logging, monitoring, and automated testing

**Database Design (PostgreSQL)**

. Primary and foreign keys are used across all tables to maintain strong data integrity and enforce proper relationships between customers, accounts, transactions, beneficiaries, and loans. This      ensures that all dependent records are always linked to valid parent records.

. CHECK constraints are implemented to enforce business rules at the database level, such as preventing negative account balances, restricting transaction types and modes, and validating monetary     values to ensure consistent and reliable data.

. Default values are applied for important fields like status indicators and timestamps, enabling automatic data consistency for records such as account status, transaction state, and creation time   without requiring manual input.

. Cascading delete rules are defined on foreign key relationships to maintain relational consistency, ensuring that when a parent record (such as a customer or account) is removed, all related        dependent records are automatically deleted, preventing orphaned data.

