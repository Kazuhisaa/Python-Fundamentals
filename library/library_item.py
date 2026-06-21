# library_item.py
import abc

class LibraryItem(abc.ABC):
    def __init__ (self,library_ID, title):
        self._library_ID = library_ID
        self._title = title
        self._borrow_date = None
        self._is_borrowed = False

    @property
    def library_ID(self):
        return self._library_ID
    
    @property
    def title(self):
        return self._title
    
    @property
    def is_borrowed(self):
        return self._is_borrowed
    
    def borrowed_item(self,date):
        if self._is_borrowed:
            print(f" '{self._title}' is already borrowed")
            return False
        self._is_borrowed = True
        self._borrow_date = date
        print(f"Succesfully Borrowed '{self._title}' on {date}.")
        return True
    
    def return_item(self):                                                                                                                                 
            if not self._is_borrowed:                                                                                                                          
                print(f"'{self._title}' was not borrowed.")                                                                                                    
                return False                                                                                                                                   
            self._is_borrowed = False                                                                                                                          
            self._borrow_date = None                                                                                                                           
            print(f"Successfully returned '{self._title}'.")                                                                                                   
            return True    
    
    def __eq__(self, other):
        if isinstance(other, LibraryItem):
            return self._library_ID == other._library_ID
        return False
        
    
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
    
    
class Magazine(LibraryItem):
    def __init__(self, library_ID, title,issue_no):
        super().__init__(library_ID, title)

        self._issue_no = issue_no
    def __str__(self):
        return super().__str__() + f" | Issue No.: {self._issue_no}"
    
class DVD(LibraryItem):
    def __init__(self, library_ID, title,duration):
        super().__init__(library_ID, title) 

        self._duration = duration
    def __str__(self):
        return super().__str__() + f" | Duration: {self._duration}"