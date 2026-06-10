class UberException(Exception):
    """Base exception for all Uber-related exceptions."""
    pass


class NoDriverAvailableError(UberException):
    """Raised when no drivers are available for a ride request."""
    pass


class TripNotFoundError(UberException):
    """Raised when a trip with the given ID does not exist."""
    pass


class InvalidOTPError(UberException):
    """Raised when the OTP provided to start the trip is invalid."""
    pass


class InvalidTripStateError(UberException):
    """Raised when a trip is in an invalid state for the requested operation."""
    pass


class InvalidPaymentError(UberException):
    """Raised when a payment operation is invalid."""
    pass


class DriverNotAvailableError(UberException):
    """Raised when trying to assign a driver who is not available."""
    pass