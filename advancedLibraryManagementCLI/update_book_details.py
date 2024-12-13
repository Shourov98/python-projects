from save_books import save_books

def update_book_details(all_books):
    title = input("Enter the title of the book to update: ").strip()
    author = input("Enter the author's name: ").strip()

    for book in all_books:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print(f"Found book: {book['title']} by {book['author']}")
            
            
            book["title"] = input("Enter the new title (leave blank to keep the same): ").strip() or book["title"]
            book["author"] = input("Enter the new author (leave blank to keep the same): ").strip() or book["author"]
            book["publication_year"] = input("Enter the new publication year (leave blank to keep the same): ").strip() or book["publication_year"]
            book["price"] = int(input("Enter the new price (leave blank to keep the same): ").strip() or book["price"])
            book["quantity"] = int(input("Enter the new quantity (leave blank to keep the same): ").strip() or book["quantity"])
            
            print("Book details updated successfully!")
            
            # Save the updated list to the JSON file
            save_books(all_books)
            break
    else:
        print("Book not found.")
