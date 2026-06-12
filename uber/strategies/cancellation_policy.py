from datetime import datetime
from abc import ABC, abstractmethod

from models.trip import Trip


class CancellationPolicy(ABC):
    @abstractmethod
    def compute_fee(self, trip: Trip, cancelled_by: str) -> float:
        pass


class TimeBasedCancellationPolicy(CancellationPolicy):
    def __init__(self, free_window_minutes: float = 2.0, cancellation_fee: float = 100.0):
        self.free_window_minutes = free_window_minutes
        self.cancellation_fee = cancellation_fee

    def compute_fee(self, trip: Trip, cancelled_by: str) -> float:
        elapsed = (datetime.now() - trip.requested_at).total_seconds() / 60
        if elapsed <= self.free_window_minutes:
            return 0.0
        return self.cancellation_fee