"""Module for the Guest class, representing a hotel guest with booking history."""

from typing import List, Dict
from booking import Booking

class Guest:
    """
    Represents a hotel guest, storing their basic information and booking history.
    """

    def __init__(self, guest_id: int, name: str, contact_info: str,
                 loyalty_status: str = "Basic", reservation_history: List[Booking] = []):
        """
        Initializes a Guest object with:
        - guest_id: Unique identifier for the guest.
        - name: Full name of the guest.
        - contact_info: Contact information (email/phone).
        - loyalty_status: Loyalty tier of the guest (defaults to "Basic").
        - reservation_history: List of Booking objects associated with the guest.
        """
        # Store guest's basic information.
        self._guest_id = guest_id
        self._name = name
        self._contact_info = contact_info
        self._loyalty_status = loyalty_status
        # Store the guest's booking history.
        self._reservation_history: List[Booking] = reservation_history

    # Getter and setter methods for guest attributes.
    def get_guest_id(self) -> int:
        """Returns the guest's unique ID."""
        return self._guest_id

    def set_guest_id(self, guest_id: int) -> None:
        """Sets the guest's unique ID."""
        self._guest_id = guest_id

    def get_name(self) -> str:
        """Returns the guest's name."""
        return self._name

    def set_name(self, name: str) -> None:
        """Sets the guest's name."""
        self._name = name

    def get_contact_info(self) -> str:
        """Returns the guest's contact information."""
        return self._contact_info

    def set_contact_info(self, contact_info: str) -> None:
        """Sets the guest's contact information."""
        self._contact_info = contact_info

    def get_loyalty_status(self) -> str:
        """Returns the guest's loyalty status."""
        return self._loyalty_status

    def set_loyalty_status(self, loyalty_status: str) -> None:
        """Sets the guest's loyalty status."""
        self._loyalty_status = loyalty_status

    def get_reservation_history(self) -> List[Booking]:
        """Returns the guest's booking history."""
        return self._reservation_history

    def set_reservation_history(self, history: List[Booking]) -> None:
        """Sets the guest's booking history."""
        self._reservation_history = history

    # Functional methods for guest operations.
    def upgrade_loyalty_status(self, new_status: str) -> None:
        """Upgrades the guest's loyalty tier to a new status."""
        self._loyalty_status = new_status

    def add_reservation(self, booking: Booking) -> None:
        """Adds a new booking to the guest's reservation history."""
        self._reservation_history.append(booking)

    def get_total_spent(self, room_prices: Dict[int, float]) -> float:
        """
        Calculates the total amount spent by the guest on their bookings.
        - room_prices: A dictionary mapping room numbers to their prices.
        """
        total = 0.0  # Initialize total spending.
        for booking in self._reservation_history:
            room_num = booking.get_room_number()  # Get the room number for the booking.
            if room_num in room_prices:  # Check if the room number is in the dictionary.
                # Add the price of the room times the duration of the booking to the total.
                total += room_prices[room_num] * booking.calculate_booking_duration()
        return round(total, 2)  # Return the total rounded to 2 decimal places.

    def __str__(self) -> str:
        """Returns a string representation of the Guest object."""
        return f"Guest {self._guest_id}: {self._name} (Status: {self._loyalty_status})"