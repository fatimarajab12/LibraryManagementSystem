from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, item_id, title, author):
        self.item_id = item_id
        self.title = title
        self.author = author
        self.is_available = True
        self.is_reserved = False

    @abstractmethod
    def display_info(self):
        pass

    def check_availability(self):
        return self.is_available

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "title": self.title,
            "author": self.author,
            "is_available": self.is_available,
            "is_reserved": self.is_reserved,
            "type": self.__class__.__name__
        }
    
    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        pass
