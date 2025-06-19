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

    def __str__(self):
        return f"{self.__title} by {self.__author}, published in {self.__year}"

    def __repr__(self):
        return f"Book('{self.__title}', '{self.__author}', {self.__year})"

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    # @author.setter
    # def author(self, value):
    #     self.__author = value

    @property
    def year(self):
        return self.__year

    def __del__(self):
        print(f"Deleting {self.__title}")
