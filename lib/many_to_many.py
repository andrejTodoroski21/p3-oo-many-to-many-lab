class Author:
    def __init__(self, name:str):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])
    
class Book:
    def __init__(self, title:str):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]

class Contract:

    all = []

    def __init__(self, author:Author, book:Book, date:str, royalties:int):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if type(value) == Author:
            self._author = value
        else:
            raise TypeError("Must be of type Author")
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if type(value) == Book:
            self._book = value
        else:
            raise TypeError("Must be of type Book")
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if type(value) == str:
            self._date = value
        else:
            raise TypeError("Must be of type string")
        
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if type(value) == int:
            self._royalties = value
        else:
            raise TypeError("Must be of type integer")
        
    
    