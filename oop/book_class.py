"""
    Objective:
    Master Python magic methods by implementing a Book class that demonstrates:
    - Constructor (__init__)
    - Destructor (__del__)
    - String representation (__str__)
    - Official representation (__repr__)
"""
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.__title = title
        self.__author = author
        self.__year = year

    @property
    def title(self):
        return self.__title

    @property
    def __author(self):
        return self.__author

    @property
    def __year(self):
        return self.__year

    def __del__(self):
        print(f"Deleting (title of the book)") 

# title (str): The title of the book.
# author (str): The author of the book.
# year (int): The publication year of the book.