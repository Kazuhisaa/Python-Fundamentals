# library_item.py
import abc

class LibraryItem(abc.ABC):
    def __init__ (self,library_ID, title):
        self._library_ID = library_ID
        self._title = title
        self._borrow_date = None
        self._is_borrowed = False

    @abc.abstractmethod
    def __str__(self):
        status = f"Borrowed on: {self._borrow_date} " if self._is_borrowed else "Available"
        return f"ID: {self._library_ID} | Title: {self._title} | Status: {status}"
    
class Book(LibraryItem):
    def __init__(self,library_ID, title,author,pub_date):
        super().__init__(library_ID,title)

        self._author = author
        self._pub_date = pub_date
    def __str__(self):
        return super().__str__() + f" | Author: {self._author} | Publication Date: {self._pub_date}"
    
    
