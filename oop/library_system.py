class Book:
    def __init__(self, title, author):
        """
        Base class representing a book with title and author.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        String representation of a generic book.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """
        Derived class representing an electronic book.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        String representation of an e-book, including file size.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """
        Derived class representing a printed book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        String representation of a print book, including page count.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """
        Represents a library that holds a collection of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book (Book, EBook, or PrintBook) to the library.
        """
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """
        Lists all books in the library.
        """
        for book in self.books:
            print(book)


def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()


if __name__ == "__main__":
    main()