import json
from models.book import Book
from models.magazine import Magazine
from models.dvd import DVD
from models.user import User
from exceptions.custom_exceptions import (
    ItemNotAvailableError,
    UserNotFoundError,
    ItemNotFoundError
)

class Library:
    def __init__(self, items_file='data/items.json', users_file='data/users.json'):
        self.items_file = items_file
        self.users_file = users_file
        self.items = []
        self.users = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.items_file, 'r') as f:
                items_data = json.load(f)
            for data in items_data:
                item_type = data.get("type")
                if item_type == "Book":
                    item = Book.from_dict(data)
                elif item_type == "Magazine":
                    item = Magazine.from_dict(data)
                elif item_type == "DVD":
                    item = DVD.from_dict(data)
                else:
                    continue
                self.items.append(item)
        except FileNotFoundError:
            pass

        try:
            with open(self.users_file, 'r') as f:
                users_data = json.load(f)
            for data in users_data:
                user = User.from_dict(data, self.items)
                self.users.append(user)
        except FileNotFoundError:
            pass

    def save_data(self):
        with open(self.items_file, 'w') as f:
            json.dump([self._item_to_dict(i) for i in self.items], f, indent=4)
        with open(self.users_file, 'w') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4)

    def _item_to_dict(self, item):
        data = item.to_dict()
        if isinstance(item, Book):
            data["type"] = "Book"
        elif isinstance(item, Magazine):
            data["type"] = "Magazine"
        elif isinstance(item, DVD):
            data["type"] = "DVD"
        return data

    def add_user(self, user):
        if any(u.user_id == user.user_id for u in self.users):
            raise Exception(f"User ID {user.user_id} already exists.")
        self.users.append(user)

    def borrow_item(self, user_id, item_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if user is None:
            raise UserNotFoundError(f"User with ID {user_id} not found.")

        item = next((i for i in self.items if i.item_id == item_id), None)
        if item is None:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")

        if not item.is_available or item.is_reserved:
            raise ItemNotAvailableError(f"Item '{item.title}' is not available for borrowing.")

        item.is_available = False

    def return_item(self, user_id, item_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if user is None:
            raise UserNotFoundError(f"User with ID {user_id} not found.")

        item = next((i for i in self.items if i.item_id == item_id), None)
        if item is None:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")

        if item.is_available:
            raise Exception(f"Item '{item.title}' is already returned.")

        item.is_available = True
        item.is_reserved = False
        item.reserved_by = None

    def reserve_item(self, user_id, item_id):
        user = next((u for u in self.users if u.user_id == user_id), None)
        if user is None:
            raise UserNotFoundError(f"User with ID {user_id} not found.")

        item = next((i for i in self.items if i.item_id == item_id), None)
        if item is None:
            raise ItemNotFoundError(f"Item with ID {item_id} not found.")

        if not hasattr(item, 'reserve'):
            raise ItemNotAvailableError(f"Item '{item.title}' cannot be reserved.")

        if item.is_reserved:
            raise ItemNotAvailableError(f"Item '{item.title}' is already reserved.")

        item.reserve(user)
