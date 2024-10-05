from library_management import Book, library  
def main():
    # Setup a small library
    Library = library()
    Library.add_book(Book("Brave New World", "Aldous Huxley"))
    Library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    Library.list_available_books()

    # Simulate checking out a book
    Library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    Library.list_available_books()

    # Simulate returning a book
    Library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    Library.list_available_books()

if __name__ == "__main__":
    main()