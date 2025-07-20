def borrow_book(books, title):
    for book in books:
        if book["info"][0].lower() == title.lower():
            if book["available"]:
                book["available"] = False
                print(f"You have borrowed '{book['info'][0]}'.")
            else:
                print("Book is already borrowed.")
            return
    print("Book not found.")

def return_book(books, title):
    for book in books:
        if book["info"][0].lower() == title.lower():
            if not book["available"]:
                book["available"] = True
                print(f"Book '{book['info'][0]}' returned.")
            else:
                print("Book was not borrowed.")
            return
    print("Book not found.")
