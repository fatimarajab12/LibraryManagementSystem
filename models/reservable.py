from abc import ABC, abstractmethod

class Reservable(ABC):
    @abstractmethod
    def reserve(self, user):
        """Method to reserve the item for a user."""
        pass
