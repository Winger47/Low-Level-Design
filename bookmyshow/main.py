from datetime import datetime, timedelta
from models.user import User
from models.movie import Movie
from models.theater import Theater
from models.screen import Screen
from models.seat import Seat
from models.show import Show
from enums import SeatType, PaymentMethod
from services.show_service import ShowService
from services.booking_service import BookingService
from services.payment_service import PaymentService
from strategies.refund_policy import TimeBasedRefundPolicy


def build_world():
    # Users
    alice = User(1, "Alice")
    bob = User(2, "Bob")

    # Movie
    inception = Movie(1, "Inception", duration_mins=148)

    # Theater
    pvr = Theater(1, "PVR Forum", "Bengaluru", screens=[])

    # Seats for Screen 1 (5 seats: 3 regular + 2 premium)
    seats = [
        Seat(1, row_num=1, seat_num=1, price=200, seat_type=SeatType.REGULAR),
        Seat(2, row_num=1, seat_num=2, price=200, seat_type=SeatType.REGULAR),
        Seat(3, row_num=1, seat_num=3, price=200, seat_type=SeatType.REGULAR),
        Seat(4, row_num=2, seat_num=1, price=400, seat_type=SeatType.PREMIUM),
        Seat(5, row_num=2, seat_num=2, price=400, seat_type=SeatType.PREMIUM),
    ]

    # Screen
    screen1 = Screen(1, "Screen 1", rows=2, cols=3, theater=pvr, seats=seats)
    pvr.screens.append(screen1)

    # Show (tomorrow at 7:30 PM)
    tomorrow_730 = datetime.now() + timedelta(days=1, hours=2)  # ~2 days from now to test refund
    show1 = Show(
        show_id=1,
        movie=inception,
        screen=screen1,
        start_time=tomorrow_730,
        end_time=tomorrow_730 + timedelta(minutes=148),
    )

    # Services
    show_service = ShowService([show1])
    refund_policy = TimeBasedRefundPolicy()
    booking_service = BookingService(show_service, refund_policy)
    payment_service = PaymentService(booking_service)

    return alice, bob, show1, show_service, booking_service, payment_service


def run_happy_path(alice, show, booking_service, payment_service):
    print("\n=== Happy Path: Alice books 2 seats ===")
    
    # Hold seats 1 and 4
    booking = booking_service.create_hold(alice, show, seat_ids=[1, 4])
    print(f"Created: {booking}")
    
    # Process payment
    payment = payment_service.process_payment(booking, PaymentMethod.UPI)
    print(f"Payment: {payment}")
    print(f"Booking after payment: {booking}")
    
    return booking, payment


def run_cancellation(booking_service, payment_service, booking, payment):
    print("\n=== Cancellation: Alice cancels her booking ===")
    refund_amount = booking_service.cancel_booking(booking.booking_id)
    print(f"Refund amount: ₹{refund_amount}")
    if refund_amount > 0:
        payment_service.refund(payment, refund_amount)
    print(f"Booking after cancellation: {booking}")


def run_double_booking_attempt(bob, show, booking_service):
    print("\n=== Failure case: Bob tries to book seats already cancelled ===")
    try:
        booking = booking_service.create_hold(bob, show, seat_ids=[1, 4])
        print(f"Bob's booking: {booking}")
    except Exception as e:
        print(f"Booking failed: {e}")


def main():
    alice, bob, show, show_service, booking_service, payment_service = build_world()

    # Demo: search
    print("=== Searching for shows ===")
    results = show_service.search_shows(city="Bengaluru", movie_name="Inception")
    for s in results:
        print(f"Found: {s}")

    # Happy path
    booking, payment = run_happy_path(alice, show, booking_service, payment_service)

    # Cancellation
    run_cancellation(booking_service, payment_service, booking, payment)

    # After cancellation, Bob CAN book the same seats (they're released)
    run_double_booking_attempt(bob, show, booking_service)


if __name__ == "__main__":
    main()