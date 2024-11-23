def delete_book(all_books):
    title = input("Enter the title of the book to delete: ")
    author = input("Enter the author of the book to delete: ")

    for book in all_books:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            all_books.remove(book)
            print("Book deleted successfully!")
            break
    else:
        print("Book not found.")
