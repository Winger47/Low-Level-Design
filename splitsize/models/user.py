

class User:
    def __init__(self, user_id: str, name: str):
        self.user_id=user_id
        self.name=name
    
    def __repr__(self) -> str:
        return f"User(id={self.user_id}, name={self.name})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)