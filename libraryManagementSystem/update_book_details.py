def update_book_details(all_books):
    title = input("Enter the title of the book to update: ")
    author = input("Enter the author's name: ")

    for book in all_books:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print(f"Found book: {book['title']} by {book['author']}")
            book["title"] = input("Enter the new title (leave blank to keep the same): ") or book["title"]
            book["author"] = input("Enter the new author (leave blank to keep the same): ") or book["author"]
            book["isbn"] = int(input("Enter the new ISBN (leave blank to keep the same): ") or book["isbn"])
            book["publication_year"] = input("Enter the new publication year (leave blank to keep the same): ") or book["publication_year"]
            book["price"] = int(input("Enter the new price (leave blank to keep the same): ") or book["price"])
            book["quantity"] = int(input("Enter the new quantity (leave blank to keep the same): ") or book["quantity"])
            print("Book details updated successfully!")
            break
    else:
        print("Book not found.")
