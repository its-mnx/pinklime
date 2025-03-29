"""Room class implementation."""

class Room:
    """
    Represents a hotel room.
    Contains attributes and methods for room management.
    """

    def __init__(self, room_number: int, room_type: str, price_per_night: float):
        """
        Initializes a Room object.
        - room_number: Unique identifier for the room.
        - room_type: Category of the room (e.g., "Standard", "Suite").
        - price_per_night: Base rate for one night's stay.
        """
        self._room_number = room_number
        self._room_type = room_type
        self._price_per_night = price_per_night
        self._amenities: list[str] = []  # Start with no amenities.
        self._availability = True  # Rooms are available by default.

    def get_room_number(self) -> int:
        """Returns the room's unique number."""
        return self._room_number

    def set_room_number(self, room_number: int) -> None:
        """Sets the room's unique number."""
        self._room_number = room_number

    def get_room_type(self) -> str:
        """Returns the room's category."""
        return self._room_type

    def set_room_type(self, room_type: str) -> None:
        """Sets the room's category."""
        self._room_type = room_type

    def get_price_per_night(self) -> float:
        """Returns the room's nightly rate."""
        return self._price_per_night

    def set_price_per_night(self, price: float) -> None:
        """Sets the room's nightly rate."""
        self._price_per_night = price

    def get_amenities(self) -> list[str]:
        """Returns the list of amenities in the room."""
        return self._amenities

    def set_amenities(self, amenities: list[str]) -> None:
        """Sets the list of amenities in the room."""
        self._amenities = amenities

    def get_availability(self) -> bool:
        """Returns the room's availability status."""
        return self._availability

    def set_availability(self, available: bool) -> None:
        """Sets the room's availability status."""
        self._availability = available

    def is_available(self) -> bool:
        """Checks if the room is currently available."""
        return self._availability

    def add_amenity(self, amenity: str) -> None:
        """Adds a new amenity to the room's list of amenities."""
        # Only add the amenity if it's not already in the list.
        if amenity not in self._amenities:
            self._amenities.append(amenity)

    def calculate_total_cost(self, nights: int) -> float:
        """
        Calculates the total cost of staying in the room for a given number of nights.
        Args:
            nights: The number of nights the guest will stay.
        Returns:
            The total cost of the stay.
        """
        # Ensure the number of nights is a positive value.
        if nights <= 0:
            raise ValueError("Nights must be positive")
        return self._price_per_night * nights

    def find_available_rooms(self, room_type: str, check_in_date: str, check_out_date: str) -> list['Room']:  # Added method
        """
        Finds available rooms of a specific type within a date range.

        Args:
            room_type: The type of room to search for.
            check_in_date: The check-in date (YYYY-MM-DD).
            check_out_date: The check-out date (YYYY-MM-DD).

        Returns:
            A list of available Room objects.
            (Currently always returns an empty list - needs implementation with booking system)
        """
        # Placeholder implementation - needs integration with a booking/reservation system
        return []

    def __str__(self) -> str:
        """Returns a string representation of the Room object."""
        # Construct a string showing room details.
        return (f"Room {self._room_number} ({self._room_type}): "
                f"${self._price_per_night}/night, "
                f"Amenities: {', '.join(self._amenities)}, "
                f"Available: {'Yes' if self._availability else 'No'}")