def search_books(all_books):
    search_title = input("Enter the title of the book to search: ")

    found_books = []
    for book in all_books:
        if search_title.lower() in book["title"].lower():
            found_books.append(book)

    if len(found_books) == 0:
        print("No matching books found.")
    else:
        print("---------------------------")
        print("Matching books:")
        for index, book in enumerate(found_books, start=1):
            print(f"{index}. Title: {book['title']}")
            print(f"   Author: {book['author']}")
            print(f"   Publication Year: {book['publication_year']}")
            print(f"   Price: {book['price']} Taka")
            print(f"   Quantity: {book['quantity']}")
        print("---------------------------")
