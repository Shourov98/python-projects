def show_all_books(all_books):
    if len(all_books) == 0:
        print("No books available.")
    else:
        print("---------------------------")
        print("List of all books:")
        for index, book in enumerate(all_books, start=1):
            print(f"{index}. {book['title']} - \n  {book['author']} \n  {book['isbn']} \n  {book['publication_year']} \n  {book['price']} Taka \n  {book['quantity']}.")
        print("---------------------------")
