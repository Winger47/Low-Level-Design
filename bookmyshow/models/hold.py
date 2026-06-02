from models.user import User
from models.show import Show
from models.seat import Seat    
from datetime import datetime,timedelta




class Hold:
    """Represents a 2-minute lock on selected seats for a user."""

    HOLD_DURATION_MINUTES = 2
    def __init__(self,hold_id:int,user:User,show:Show,seats:list[Seat]):
        self.hold_id=hold_id
        self.user=user
        self.show=show
        self.seats=seats
        self.created_at=datetime.now()
        self.expires_at = self.created_at + timedelta(minutes=self.HOLD_DURATION_MINUTES)
        self.is_active=True
    
    def is_expired(self)->bool:
        return datetime.now() > self.expires_at
        
    def release(self):
        self.is_active=False    
        for seat in self.seats:
            seat.release()

        
    def __repr__(self):
        return f"Hold(hold_id={self.hold_id}, user={self.user.name},  seats={self.seats}, created_at={self.created_at}, expires_at={self.expires_at}, is_active={self.is_active})"
        