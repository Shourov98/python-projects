from display import show_menu
from add_book import add_book
from show_all_books import show_all_books
from search_books import search_books
from update_book_details import update_book_details
from delete_book import delete_book

all_books = []

def main():
    while True:
        show_menu()
        menu = input("Select any number: ")

        if menu == "0":
            print("Thanks for using the Book Library Management System. Goodbye!")
            break
        elif menu == "1":
            add_book(all_books)
        elif menu == "2":
            show_all_books(all_books)
        elif menu == "3":
            search_books(all_books)
        elif menu == "4":
            update_book_details(all_books)
        elif menu == "5":
            delete_book(all_books)
        else:
            print("Invalid input! Please enter a number from 0 to 5.")

if __name__ == "__main__":
    main()
