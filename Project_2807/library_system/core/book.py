class Book:
    def __init__(self, title, author, available=True, borrower=None):
        self.title = title
        self.author = author
        self.available = available
        self.borrower = borrower

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "available": self.available,
            "borrower": self.borrower
        }

    @staticmethod
    def from_dict(data):
        return Book(
            title=data["title"],
            author=data["author"],
            available=data["available"],
            borrower=data["borrower"]
        )

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrower}"
        return f"{self.title} by {self.author} - {status}"
