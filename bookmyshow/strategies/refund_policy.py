
from abc import ABC, abstractmethod
from datetime import datetime
from models.booking import Booking


class RefundPolicy(ABC):
    """Computes refund amount"""
    @abstractmethod
    def compute_refund(self,booking:Booking)->float:
        pass

class TimeBasedRefundPolicy(RefundPolicy):
    """Refund based on time:

    ->24 hours:100%
    ->2-24 hours:50%
    ->less than 2 hours:0%
    """
    def compute_refund(self,booking:Booking)->float:

        time_untill_show=booking.show.start_time-datetime.now()
        hours_untill_show=time_untill_show.total_seconds()/3600

        if hours_untill_show>=24:
            return booking.total_amount*1.0
        elif 2<=hours_untill_show<24:
            return booking.total_amount*0.5
        else:
            return 0.0          
    