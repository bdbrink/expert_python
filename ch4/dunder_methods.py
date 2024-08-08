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

# Create some Book objects
book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Fluent Python", "Luciano Ramalho", 792)
book3 = Book("Python Crash Course", "Eric Matthes", 544)

# Test __str__
print(book1)

# Test __len__
print(len(book1))

# Test __eq__
print(book1 == book2)
print(book1 == book3)

# Test __lt__
print(book1 < book2)

# Test __add__
print(book1 + book2)
print(book1 + 100)

# This will raise a TypeError
# print(book1 + "100")