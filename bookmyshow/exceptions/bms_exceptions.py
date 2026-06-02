class BMSException(Exception):
    """Base exception for BookMyShow."""
    pass


class SeatNotAvailableError(BMSException):
    """Raised when a seat is not in AVAILABLE state."""
    pass


class HoldExpiredError(BMSException):
    """Raised when a hold has expired."""
    pass


class UserAlreadyHasActiveHoldError(BMSException):
    """Raised when a user already has an active hold."""
    pass


class BookingNotFoundError(BMSException):
    """Raised when a booking ID does not exist."""
    pass


class BookingNotCancellableError(BMSException):
    """Raised when a booking cannot be cancelled in its current state."""
    pass


class InvalidPaymentError(BMSException):
    """Raised for invalid payment requests."""
    pass


class MaxSeatsExceededError(BMSException):
    """Raised when more than 10 seats are selected in one booking."""
    pass


class InvalidSeatConfigurationError(BMSException):
    """Raised when screen seat configuration is invalid."""
    pass


class PaymentProcessingError(BMSException):
    """Raised when payment processing fails."""
    pass