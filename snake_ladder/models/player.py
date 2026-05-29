


class Player:
    """ Represent A player."""
    def __init__(self,name:str,position:int =0):       
        self.name=name
        self.position=position  

    def move_to(self,new_position:int):
        self.position = new_position        
    def __repr__(self):
        return f"<Player name={self.name} position={self.position}>"    
    