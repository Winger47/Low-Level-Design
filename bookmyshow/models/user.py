

class User:

    def __init__(self,user_id:int,name:str):
        self.user_id=user_id
        self.name=name  

    def __repr__(self):
        return f"User(user_id={self.user_id},name={self.name})"
    