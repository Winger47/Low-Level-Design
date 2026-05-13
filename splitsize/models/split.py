from models.user import User


class Split:
    def __init__(self, user: User, amount: float):
        self.user = user
        self.amount = amount

    def __repr__(self):
        return f"<Split user={self.user.name} amount={self.amount}>"