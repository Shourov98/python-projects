def add_book(all_books):
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    isbn = int(input("Enter the ISBN number: "))
    publication_year = input("Enter the publication year: ")
    price = int(input("Enter the price: "))
    quantity = int(input("Enter the quantity: "))

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "publication_year": publication_year,
        "price": price,
        "quantity": quantity
    }

    all_books.append(book)
    print("Book added successfully!")
