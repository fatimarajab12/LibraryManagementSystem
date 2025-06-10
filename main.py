from models.library import Library
from exceptions.custom_exceptions import (
    ItemNotAvailableError,
    UserNotFoundError,
    ItemNotFoundError
)

def main():
    lib = Library()
    print("Welcome to the Library Management System!")

    while True:
        print("\nOptions:")
        print("1. Display all items")
        print("2. Borrow an item")
        print("3. Return an item")
        print("4. Reserve an item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        try:
            if choice == "1":
                for item in lib.items:
                    item.display_info()

            elif choice == "2":
                user_id = input("Enter your user ID: ")
                item_id = input("Enter item ID to borrow: ")
                lib.borrow_item(user_id, item_id)
                print("Item borrowed successfully.")

            elif choice == "3":
                user_id = input("Enter your user ID: ")
                item_id = input("Enter item ID to return: ")
                lib.return_item(user_id, item_id)
                print("Item returned successfully.")

            elif choice == "4":
                user_id = input("Enter your user ID: ")
                item_id = input("Enter item ID to reserve: ")
                lib.reserve_item(user_id, item_id)
                print("Item reserved successfully.")

            elif choice == "5":
                print("Goodbye!")
                lib.save_data()
                break

            else:
                print("Invalid choice. Please select from 1 to 5.")

        except (ItemNotAvailableError, UserNotFoundError, ItemNotFoundError, Exception) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
