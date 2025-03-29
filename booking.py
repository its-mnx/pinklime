"""
Handles hotel room bookings including reservations, cancellations, and date management
"""

from datetime import datetime
from invoice import Invoice

class Booking:
    """Manages booking information and operations"""

    def __init__(self, booking_id: int, guest_id: int, room_number: int,
                 check_in_date: str, check_out_date: str):
        """Initialize booking with provided details"""
        self._booking_id = booking_id
        self._guest_id = guest_id
        self._room_number = room_number
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._invoice = None
        self._is_cancelled = False

    # Property accessors
    def get_booking_id(self) -> int:
        """Return unique booking identifier"""
        return self._booking_id

    def get_guest_id(self) -> int:
        """Return ID of guest who made booking"""
        return self._guest_id

    def get_room_number(self) -> int:
        """Return room number for this booking"""
        return self._room_number

    def get_check_in_date(self) -> str:
        """Return scheduled check-in date (YYYY-MM-DD)"""
        return self._check_in_date

    def get_check_out_date(self) -> str:
        """Return scheduled check-out date (YYYY-MM-DD)"""
        return self._check_out_date

    def is_cancelled(self) -> bool:
        """Check if booking has been cancelled"""
        return self._is_cancelled

    def set_cancelled(self, cancelled: bool) -> None:
        """Set booking cancellation status"""
        self._is_cancelled = cancelled

    # Property mutators
    def set_booking_id(self, booking_id: int) -> None:
        """Update booking identifier"""
        self._booking_id = booking_id

    def set_guest_id(self, guest_id: int) -> None:
        """Update guest identifier"""
        self._guest_id = guest_id

    def set_room_number(self, room_number: int) -> None:
        """Update assigned room number"""
        self._room_number = room_number

    def set_check_in_date(self, date: str) -> None:
        """Update check-in date after validation"""
        self._validate_date(date)
        if hasattr(self, '_check_out_date'):
            self.validate_dates(date, self._check_out_date)
        self._check_in_date = date

    def set_check_out_date(self, date: str) -> None:
        """Update check-out date after validation"""
        self._validate_date(date)
        if hasattr(self, '_check_in_date'):
            self.validate_dates(self._check_in_date, date)
        self._check_out_date = date

    # Invoice management
    def get_invoice(self) -> Invoice:
        """Get associated invoice object"""
        return self._invoice

    def set_invoice(self, invoice: Invoice) -> None:
        """Set associated invoice object"""
        self._invoice = invoice

    # Business logic methods
    def calculate_booking_duration(self) -> int:
        """Calculate total nights between check-in and check-out"""
        fmt = "%Y-%m-%d"
        delta = (datetime.strptime(self._check_out_date, fmt) -
                 datetime.strptime(self._check_in_date, fmt))
        return delta.days

    def is_booking_active(self, current_date: str) -> bool:
        """Check if booking is active on given date"""
        fmt = "%Y-%m-%d"
        current = datetime.strptime(current_date, fmt)
        check_in = datetime.strptime(self._check_in_date, fmt)
        check_out = datetime.strptime(self._check_out_date, fmt)
        return check_in <= current <= check_out and not self._is_cancelled

    def generate_booking_summary(self) -> str:
        """Generate formatted booking details string"""
        status = " (Cancelled)" if self._is_cancelled else ""
        return (f"Booking #{self._booking_id}: Room {self._room_number}, "
                f"Dates: {self._check_in_date} to {self._check_out_date}{status}")

    # Validation methods
    def cancel_booking(self) -> None:
        """Mark booking as cancelled if not already cancelled"""
        if self._is_cancelled:
            raise ValueError("Booking already cancelled")
        self._is_cancelled = True

    def validate_dates(self, check_in: str, check_out: str) -> None:
        """Verify check-out date is after check-in date"""
        check_in_date = datetime.strptime(check_in, "%Y-%m-%d")
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d")
        if check_out_date <= check_in_date:
            raise ValueError("Check-out date must be after check-in date")

    def _validate_date(self, date_str: str) -> None:
        """Verify date string format is YYYY-MM-DD"""
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format")

    def __str__(self) -> str:
        """Return string representation of booking"""
        return self.generate_booking_summary()