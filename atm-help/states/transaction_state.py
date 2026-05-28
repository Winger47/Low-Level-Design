from typing import Optional, TYPE_CHECKING

from states.atm_state import ATMState

if TYPE_CHECKING:
    from services.atm import ATM

from models.card import Card
from models.transaction import Transaction
from enums import TransactionType
from exceptions import InvalidOperationError


class TransactionState(ATMState):
    """ATM is in a transaction — perform the selected operation."""

    def __init__(self, atm: "ATM", operation: TransactionType) -> None:
        super().__init__(atm)
        self.operation: TransactionType = operation

    # ── ATMState abstract methods ──────────────────────────────────────

    def insert_card(self, card: Card) -> None:
        self._invalid_operation("insert_card")

    def enter_pin(self, pin: str) -> None:
        self._invalid_operation("enter_pin")

    def eject_card(self) -> None:
        from states.idle_state import IdleState
        print(f"Card {self.atm.current_card.card_number} ejected.")
        self.atm.set_current_card(None)
        self.atm.set_state(IdleState(self.atm))

    def select_operation(self, operation: TransactionType) -> None:
        self._invalid_operation("select_operation")

    # ── Transaction operations ─────────────────────────────────────────

    def withdraw(self, amount: float) -> None:
        if self.operation != TransactionType.WITHDRAW:
            raise InvalidOperationError("withdraw", type(self).__name__)

        txn = self._create_transaction(amount)
        account = self.atm.current_card.account

        try:
            # Dispense cash first (validates ATM has enough notes)
            dispensed = self.atm.cash_dispenser.dispense(int(amount))
            # Debit the account
            account.withdraw(amount)
            txn.mark_success()
            print(f"Dispensed {amount}: {self._format_dispensed(dispensed)}")
        except Exception as e:
            txn.mark_failed(str(e))
            raise
        finally:
            self._finish(txn)

    def deposit(self, amount: float) -> None:
        if self.operation != TransactionType.DEPOSIT:
            raise InvalidOperationError("deposit", type(self).__name__)

        txn = self._create_transaction(amount)
        account = self.atm.current_card.account

        try:
            account.deposit(amount)
            txn.mark_success()
            print(f"Deposited {amount}. New balance: {account.get_balance()}")
        except Exception as e:
            txn.mark_failed(str(e))
            raise
        finally:
            self._finish(txn)

    def check_balance(self) -> None:
        if self.operation != TransactionType.CHECK_BALANCE:
            raise InvalidOperationError("check_balance", type(self).__name__)

        txn = self._create_transaction()
        account = self.atm.current_card.account

        try:
            balance = account.get_balance()
            txn.mark_success()
            print(f"Current balance: {balance}")
        except Exception as e:
            txn.mark_failed(str(e))
            raise
        finally:
            self._finish(txn)

    def change_pin(self, old_pin: str, new_pin: str) -> None:
        if self.operation != TransactionType.CHANGE_PIN:
            raise InvalidOperationError("change_pin", type(self).__name__)

        txn = self._create_transaction()
        card = self.atm.current_card

        try:
            card.change_pin(old_pin, new_pin)
            txn.mark_success()
            print("PIN changed successfully.")
        except Exception as e:
            txn.mark_failed(str(e))
            raise
        finally:
            self._finish(txn)

    # ── Private helpers ────────────────────────────────────────────────

    def _create_transaction(self, amount: Optional[float] = None) -> Transaction:
        txn_id = self.atm.next_transaction_id()
        return Transaction(
            transaction_id=txn_id,
            account=self.atm.current_card.account,
            transaction_type=self.operation,
            amount=amount,
        )

    def _finish(self, txn: Transaction) -> None:
        self.atm.transactions.append(txn)
        from states.pin_authenticated_state import PinAuthenticatedState
        self.atm.set_state(PinAuthenticatedState(self.atm))

    @staticmethod
    def _format_dispensed(dispensed: dict) -> str:
        return ", ".join(
            f"{count} x ₹{denom.value}" for denom, count in dispensed.items()
        )

    def __repr__(self) -> str:
        return f"TransactionState(operation={self.operation.name})"
