import json

def save_books(all_books):
    with open("book.json", "w") as file:
        json.dump(all_books, file, indent=4)
