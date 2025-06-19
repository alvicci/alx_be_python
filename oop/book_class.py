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
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        print(f"Deleting {self.title}")
