from manage import Management
# Main File
def display_welcome():
    print("\n" + "═" * 48)
    print("           📚 LIBRARY MANAGEMENT")
    print("═" * 48)
    print("  1.  +  Add a Book")
    print("  2.  -  Remove a Book")
    print("  3.  ≡  View All Books")
    print("  4.  ✓  Mark a Book")
    print("  5.  ×  Exit")
    print("─" * 48)


manager = Management()

while True:
    display_welcome()

    try:
        userInput = int(input("  ➜ Select an option (1-5): "))
    except ValueError:
        print("\n  ✗ Please enter a valid number.")
        continue

    match userInput:
        case 1:
            print("\n--- ADD NEW BOOK ---")
            book_name = input("  Enter book name: ")
            manager.add_book(book_name)

        case 2:
            manager.view_book()
            if manager.book_list:
                try:
                    num = int(input("\n  Book number to remove: "))
                    manager.remove_book(num)
                except ValueError:
                    print("\n  ✗ Enter a valid number.")

        case 3:
            manager.view_book()

        case 4:
            manager.view_book()
            if manager.book_list:
                try:
                    num = int(input("\n  Book number to mark: "))
                    manager.mark_book(num)
                except ValueError:
                    print("\n  ✗ Enter a valid number.")

        case 5:
            print("\n  Thank you for using Library Management!")
            print("  Goodbye! 👋\n")
            break

        case _:
            print("\n  ✗ Invalid option. Choose 1 to 5.")
