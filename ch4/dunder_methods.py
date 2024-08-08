class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.pages < other.pages

    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        elif isinstance(other, int):
            return self.pages + other
        else:
            raise TypeError("Unsupported operand type for +")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    # Container protocol
    def __contains__(self, item):
        return item in self.books

    def __len__(self):
        return len(self.books)

    # Callable protocol
    def __call__(self, author):
        return [book for book in self.books if book.author == author]

    # Iterable protocol
    def __iter__(self):
        return iter(self.books)

    # Indexing (part of container protocol)
    def __getitem__(self, index):
        return self.books[index]

# Create some Book objects
book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Fluent Python", "Luciano Ramalho", 792)
book3 = Book("Deep Learning", "Ian Goodfellow", 775)

# Create a Library
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Test container protocol
print(book1 in library)  # True
print(len(library))  # 3

# Test callable protocol
eric_books = library("Eric Matthes")
print(eric_books)  # [Python Crash Course by Eric Matthes]

# Test iterable protocol
for book in library:
    print(book.title)

# Test indexing
print(library[1])  # Fluent Python by Luciano Ramalho