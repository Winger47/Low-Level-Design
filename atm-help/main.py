"""
ATM Low-Level Design — End-to-End Demo
=======================================
Demonstrates the State Pattern driving an ATM through its full lifecycle:
  IdleState → CardInsertedState → PinAuthenticatedState → TransactionState
"""

from models.user import User
from models.account import Account
from models.card import Card
from models.cash_dispenser import CashDispenser
from enums import Denomination, TransactionType
from exceptions import (
    InvalidPinError,
    InsufficientFundsError,
    InsufficientCashInATMError,
    InvalidOperationError,
)
from services.atm import ATM


def separator(title: str) -> None:
    print(f"\n{'─' * 50}")
    print(f"  {title}")
    print(f"{'─' * 50}")


def main() -> None:
    # ── 1. Setup ───────────────────────────────────────────────────────
    separator("SETUP")

    user = User(user_id="U001", name="Shikhar Pandav")
    account = Account(user=user, account_id="ACC-1001", balance=50000.0)
    card = Card(card_number="4111-1111-1111-1111", account=account, pin="1234")

    print(f"User   : {user}")
    print(f"Account: {account}")
    print(f"Card   : {card}")

    dispenser = CashDispenser(inventory={
        Denomination.TWO_THOUSAND: 10,
        Denomination.FIVE_HUNDRED: 20,
        Denomination.HUNDRED: 50,
    })
    print(f"ATM Cash: ₹{dispenser.total_cash()}")

    atm = ATM(cash_dispenser=dispenser)
    print(f"ATM    : {atm}")

    # ── 2. Insert card ─────────────────────────────────────────────────
    separator("INSERT CARD")
    atm.insert_card(card)
    print(f"ATM    : {atm}")

    # ── 3. Enter wrong PIN twice (show retry counter) ──────────────────
    separator("WRONG PIN ATTEMPTS")

    for attempt, wrong_pin in enumerate(["0000", "9999"], start=1):
        try:
            atm.enter_pin(wrong_pin)
        except InvalidPinError as e:
            print(f"  Attempt {attempt} — caught: {e}")

    # ── 4. Enter correct PIN ───────────────────────────────────────────
    separator("CORRECT PIN")
    atm.enter_pin("1234")
    print(f"ATM    : {atm}")

    # ── 5. Check balance ───────────────────────────────────────────────
    separator("CHECK BALANCE")
    atm.select_operation(TransactionType.CHECK_BALANCE)
    atm.check_balance()
    print(f"ATM    : {atm}")

    # ── 6. Withdraw ₹4,600 ─────────────────────────────────────────────
    separator("WITHDRAW ₹4,600")
    atm.select_operation(TransactionType.WITHDRAW)
    atm.withdraw(4600)
    print(f"ATM    : {atm}")
    print(f"Account balance: ₹{account.get_balance()}")
    print(f"ATM cash remaining: ₹{dispenser.total_cash()}")

    # ── 7. Deposit ₹2,000 ──────────────────────────────────────────────
    separator("DEPOSIT ₹2,000")
    atm.select_operation(TransactionType.DEPOSIT)
    atm.deposit(2000)
    print(f"Account balance: ₹{account.get_balance()}")

    # ── 8. Change PIN ──────────────────────────────────────────────────
    separator("CHANGE PIN")
    atm.select_operation(TransactionType.CHANGE_PIN)
    atm.change_pin("1234", "5678")

    # ── 9. Eject card ──────────────────────────────────────────────────
    separator("EJECT CARD")
    atm.eject_card()
    print(f"ATM    : {atm}")

    # ── 10. Error demos ────────────────────────────────────────────────
    separator("ERROR: OPERATION IN WRONG STATE")
    try:
        atm.withdraw(1000)
    except InvalidOperationError as e:
        print(f"  Caught: {e}")

    separator("ERROR: INSUFFICIENT FUNDS")
    atm.insert_card(card)
    atm.enter_pin("5678")  # new PIN from step 8
    atm.select_operation(TransactionType.WITHDRAW)
    try:
        atm.withdraw(999999)
    except (InsufficientFundsError, InsufficientCashInATMError) as e:
        print(f"  Caught: {e}")
    atm.eject_card()

    # ── Summary ────────────────────────────────────────────────────────
    separator("TRANSACTION LOG")
    for txn in atm.transactions:
        print(f"  {txn}")

    print(f"\n✅ Demo completed successfully! {len(atm.transactions)} transactions recorded.")


if __name__ == "__main__":
    main()
