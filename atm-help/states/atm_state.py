from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from models.card import Card
from enums import TransactionType
from exceptions import InvalidOperationError

if TYPE_CHECKING:
    from services.atm import ATM


class ATMState(ABC):
    """Abstract base for all ATM states. Each state defines what operations are allowed."""

    def __init__(self, atm: "ATM"):
        self.atm = atm

    @abstractmethod
    def insert_card(self, card: Card) -> None:
        """Handle card insertion."""

    @abstractmethod
    def enter_pin(self, pin: str) -> None:
        """Handle PIN entry."""

    @abstractmethod
    def eject_card(self) -> None:
        """Handle card ejection."""

    @abstractmethod
    def select_operation(self, operation: TransactionType) -> None:
        """Handle operation selection (withdraw, deposit, etc)."""

    def _invalid_operation(self, operation: str) -> None:
        """Helper: raise InvalidOperationError tagged with the current state's class name."""
        raise InvalidOperationError(operation, type(self).__name__)

