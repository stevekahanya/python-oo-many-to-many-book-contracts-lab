class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Filters the Contract.all list for contracts belonging to this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Uses the Contract class as an intermediary to find unique related books
        return list(set([contract.book for contract in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        # Creates and returns a new Contract object
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Returns the sum of all royalties from this author's contracts
        return sum([contract.royalties for contract in self.contracts()])


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # Returns a list of contracts related to this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Returns a list of unique authors related to this book
        return list(set([contract.author for contract in self.contracts()]))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Property setters handle validation
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # --- Properties and Validations ---
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("author must be an instance of Author class")

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if isinstance(value, Book):
            self._book = value
        else:
            raise Exception("book must be an instance of Book class")

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if isinstance(value, str):
            self._date = value
        else:
            raise Exception("date must be an instance of a str")

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if isinstance(value, int):
            self._royalties = value
        else:
            raise Exception("royalties must be an instance of an int")

    @classmethod
    def contracts_by_date(cls, date):
        # Returns all contracts matching the specified date
        return [contract for contract in cls.all if contract.date == date]