def show_all_books(all_books):
    print(f"Books available: {all_books}")  
    if len(all_books) == 0:
        print("No books available.")
    else:
        print("---------------------------")
        print("List of all books:")
        for index, book in enumerate(all_books, start=1):
            print(f"{index}. Title: {book['title']}")
            print(f"   Author: {book['author']}")
            print(f"   Publication Year: {book['publication_year']}")
            print(f"   Price: {book['price']} Taka")
            print(f"   Quantity: {book['quantity']}")
            print("---------------------------")
