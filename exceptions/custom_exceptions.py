# exceptions/custom_exceptions.py

class ItemNotAvailableError(Exception):
    """Raised when an item is not available for borrowing or reservation."""
    pass

class UserNotFoundError(Exception):
    """Raised when a user is not found in the system."""
    pass

class ItemNotFoundError(Exception):
    """Raised when an item is not found in the system."""
    pass
