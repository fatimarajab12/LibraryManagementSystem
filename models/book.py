from models.library_item import LibraryItem
from abc import abstractmethod

class Reservable:
    @abstractmethod
    def reserve(self, user):
        pass

class Book(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, pages):
        super().__init__(item_id, title, author)
        self.pages = pages
        self.is_reserved = False
        self.reserved_by = None

    def display_info(self):
        status = "Available" if self.is_available else "Not Available"
        reserved = f", Reserved by User {self.reserved_by.user_id}" if self.is_reserved else ""
        print(f"Book: {self.title} by {self.author}, Pages: {self.pages}, Status: {status}{reserved}")

    def reserve(self, user):
        if self.is_reserved:
            raise Exception(f"Book '{self.title}' is already reserved.")
        self.is_reserved = True
        self.reserved_by = user

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "pages": self.pages,
            "is_reserved": self.is_reserved,
            "reserved_by": self.reserved_by.user_id if self.reserved_by else None,
        })
        return data

    @classmethod
    def from_dict(cls, data):
        book = cls(
            item_id=data["item_id"],
            title=data["title"],
            author=data["author"],
            pages=data.get("pages", 0)
        )
        book.is_available = data.get("is_available", True)
        book.is_reserved = data.get("is_reserved", False)
        book.reserved_by = None  # ربط المستخدم المحتجز لاحقًا
        return book
