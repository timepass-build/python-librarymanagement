from book import Book

class Management:
    def __init__(self):
        self.book_list = []

    def add_book(self, bookName):
        self.book_list.append(Book(bookName))
        print("\n  ✓ Book added successfully!\n")

    def remove_book(self, num):
        if not self.book_list:
            print("\n  ! Your library is empty.\n")
        elif 1 <= num <= len(self.book_list):
            removed = self.book_list.pop(num - 1)
            print(f"\n  ✓ Removed: {removed.get_bookname()}\n")
        else:
            print("\n  ✗ Invalid book number.\n")

    def view_book(self):
        print("\n" + "═" * 48)
        print("              YOUR BOOK COLLECTION")
        print("═" * 48)

        if not self.book_list:
            print("\n  No books available. Add your first book!")
        else:
            for i, book in enumerate(self.book_list, start=1):
                print(f"  {i:>2}.  {book.get_bookname()}")

        print("\n" + "═" * 48)

    def mark_book(self, num):
        if 1 <= num <= len(self.book_list):
            self.book_list[num - 1].set_bookname()
            print("\n  ✓ Book marked successfully!\n")
        else:
            print("\n  ✗ Invalid book number.\n")
