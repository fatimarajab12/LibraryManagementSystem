class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []  # قائمة العناصر اللي استعارها

    def borrow_item(self, item):
        if item.is_available:
            self.borrowed_items.append(item)
            item.is_available = False
            print(f"{self.name} borrowed '{item.title}'.")
        else:
            raise Exception(f"Item '{item.title}' is not available for borrowing.")

    def return_item(self, item):
        if item in self.borrowed_items:
            self.borrowed_items.remove(item)
            item.is_available = True
            print(f"{self.name} returned '{item.title}'.")
        else:
            raise Exception(f"{self.name} did not borrow item '{item.title}'.")

    def display_borrowed_items(self):
        if not self.borrowed_items:
            print(f"{self.name} has not borrowed any items.")
        else:
            print(f"{self.name} has borrowed:")
            for item in self.borrowed_items:
                print(f"- {item.title}")

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "borrowed_items": [item.item_id for item in self.borrowed_items]  # نفس المفتاح المستخدم في JSON
        }

    @classmethod
    def from_dict(cls, data, all_items):
        user = cls(data["user_id"], data["name"])
        borrowed_ids = data.get("borrowed_items", [])  # نفس المفتاح هنا
        for item_id in borrowed_ids:
            item = next((i for i in all_items if i.item_id == item_id), None)
            if item:
                user.borrowed_items.append(item)
                item.is_available = False
        return user
