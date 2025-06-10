from models.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, item_id, title, author, issue_number):
        super().__init__(item_id, title, author)
        self.issue_number = issue_number  # رقم العدد أو الإصدار

    def display_info(self):
        status = "Available" if self.is_available else "Not Available"
        print(f"Magazine: {self.title} by {self.author}, Issue: {self.issue_number}, Status: {status}")

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "issue_number": self.issue_number
        })
        return data

    @classmethod
    def from_dict(cls, data):
        magazine = cls(
            item_id=data["item_id"],
            title=data["title"],
            author=data["author"],
            issue_number=data.get("issue_number", "Unknown")
        )
        magazine.is_available = data.get("is_available", True)
        return magazine
