from save_books import save_books

def lend_book(all_books):
    while True:
        title = input("Enter the title of the book to lend: ")
        author = input("Enter the author's name: ")

        if not title or not author:
            print("Title and author cannot be empty.")
        else:
            break

    for book in all_books:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            if book["quantity"] > 0:
                book["quantity"] -= 1
                print(f"Successfully lent '{title}' by {author}.")
                save_books(all_books)
                break
            else:
                print(f"Sorry, '{title}' by {author} is out of stock.")
                break
    else:
        print("Book not found.")