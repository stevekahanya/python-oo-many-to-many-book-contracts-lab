## Book Contracts: Many-to-Many Relationship Lab
This project models a complex Many-to-Many (M:M) relationship between Authors and Books, using a Contract class as the intermediary "join" structure. This design allows authors to have multiple books and books to have multiple authors while tracking specific relationship data like dates and royalties.

## System Architecture
The Many-to-Many Relationship
In this model, an Author and a Book are not linked directly. Instead, they are connected through a Contract.

Author → Contracts: 1 to Many.

Book → Contracts: 1 to Many.

Author ↔ Book: Many to Many (via Contracts).

Data Validation
The Contract class acts as a gatekeeper, using Python properties to ensure data integrity:

Author: Must be an instance of the Author class.

Book: Must be an instance of the Book class.

Date: Must be a string.

Royalties: Must be an integer.

## Core Functionality
Author Model
contracts(): Dynamically retrieves all contract instances associated with the author.

books(): Returns a unique list of all books the author has signed contracts for.

sign_contract(book, date, royalties): A factory method that creates a new Contract between the author and a book.

total_royalties(): Calculates the total earnings across all the author's contracts.

Book Model
contracts(): Retrieves all legal contracts associated with the specific book.

authors(): Returns a unique list of all authors who have contributed to the book.

Contract (Intermediary) Model
all: A class attribute that stores every contract created in the system.

contracts_by_date(date): A class method that filters and returns all contracts signed on a specific date.

🛠️ Setup and Testing
Installation
Ensure you have Python 3.8 installed. Install dependencies using pipenv:

Bash
pipenv install
pipenv shell
Running Tests
This lab is test-driven. You can run the full suite using pytest:

Bash
pytest -x lib/testing/test_many_to_many.py