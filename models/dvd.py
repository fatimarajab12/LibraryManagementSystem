from models.library_item import LibraryItem
from abc import abstractmethod

class Reservable:
    @abstractmethod
    def reserve(self, user):
        pass

class DVD(LibraryItem, Reservable):
    def __init__(self, item_id, title, author, duration):
        super().__init__(item_id, title, author)
        self.duration = duration  # مدة الـ DVD بالدقائق
        self.is_reserved = False
        self.reserved_by = None

    def display_info(self):
        status = "Available" if self.is_available else "Not Available"
        reserved = f", Reserved by User {self.reserved_by.user_id}" if self.is_reserved else ""
        print(f"DVD: {self.title} by {self.author}, Duration: {self.duration} mins, Status: {status}{reserved}")

    def reserve(self, user):
        if self.is_reserved:
            raise Exception(f"DVD '{self.title}' is already reserved.")
        self.is_reserved = True
        self.reserved_by = user

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "duration": self.duration,
            "is_reserved": self.is_reserved,
            "reserved_by": self.reserved_by.user_id if self.reserved_by else None,
        })
        return data

    @classmethod
    def from_dict(cls, data):
        dvd = cls(
            item_id=data["item_id"],
            title=data["title"],
            author=data["author"],
            duration=data.get("duration", 0)
        )
        dvd.is_available = data.get("is_available", True)
        dvd.is_reserved = data.get("is_reserved", False)
        # Note: reserved_by will be linked later when loading users
        dvd.reserved_by = None
        return dvd
