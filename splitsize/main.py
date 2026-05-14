from models.user import User
from enums import SplitType
from services.splitwise_service import SplitwiseService


def main():
    # 1. Create the service
    service = SplitwiseService()

    # 2. Add users
    alice = User("U1", "Alice")
    bob = User("U2", "Bob")
    charlie = User("U3", "Charlie")

    service.add_user(alice)
    service.add_user(bob)
    service.add_user(charlie)
    print(service)

    # 3. Equal split: Alice pays 3000 for dinner with Bob and Charlie
    service.add_expense(
        paid_by=alice,
        amount=3000.0,
        participants=[alice, bob, charlie],
        split_type=SplitType.EQUAL,
    )

    print("\nAfter dinner (equal split):")
    service.show_balances()

    # 4. Exact split: Bob pays 600 for taxi (Alice owes 300, Bob's own share is 300)
    service.add_expense(
        paid_by=bob,
        amount=600.0,
        participants=[alice, bob],
        split_type=SplitType.EXACT,
        exact_amounts={alice: 300.0, bob: 300.0},
    )

    print("\nAfter taxi (exact split):")
    service.show_balances()

    # 5. Overall balances
    print("\nOverall balances:")
    for user in [alice, bob, charlie]:
        balance = service.balance_sheet.get_overall_balance(user)
        if balance > 0:
            print(f"{user.name} is owed {balance}")
        elif balance < 0:
            print(f"{user.name} owes {-balance}")
        else:
            print(f"{user.name} is settled up")


if __name__ == "__main__":
    main()