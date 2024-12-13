import random
from datetime import datetime
from save_books import save_books

def add_book(all_books):
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    # isbn = int(input("Enter the ISBN number: "))
    publication_year = input("Enter the publication year: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    # Generate a unique ISBN number
    # isbn = random.randint(100000, 99999)
    bookAddedAt = datetime.now().strftime("%d-%m-%y %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "publication_year": publication_year,
        "price": price,
        "quantity": quantity,
        "bookAddedAt": bookAddedAt
    }

    all_books.append(book)
    save_books(all_books)
    print("Book added successfully!")
