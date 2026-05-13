from models.user import User

alice1 = User("U1", "Alice")
alice2 = User("U1", "Alice Smith")   # same id, different name
bob = User("U2", "Bob")

print(alice1 == alice2)    # True — same id
print(alice1 == bob)       # False
print(hash(alice1) == hash(alice2))   # True

# Can use as dict key
balances = {alice1: 100}
print(balances[alice2])    # 100 — works because they're equal