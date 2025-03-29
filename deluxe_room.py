"""Module for DeluxeRoom class, a specialized Room with premium features."""

from room import Room

class DeluxeRoom(Room):
    """
    Represents a deluxe room exactly as defined in UML.
    Inherits from Room with 3 additional attributes and methods.
    """

    def __init__(
        self,
        room_number: int,
        price_per_night: float,
        view: str,
        jacuzzi: bool,
        breakfast_included: bool
    ) -> None:
        """
        Initializes DeluxeRoom with UML-specified attributes.
        Note: room_type is hardcoded as "Deluxe" per typical hotel conventions.
        """
        super().__init__(room_number, "Deluxe", price_per_night)  # room_type fixed as "Deluxe"
        # UML-specified additional attributes
        self._view = view
        self._jacuzzi = jacuzzi
        self._breakfast_included = breakfast_included

    # UML-REQUIRED METHODS (exact matches)
    def get_view(self) -> str:
        """Returns view type (UML-compliant getter)."""
        return self._view

    def set_view(self, view: str) -> None:
        """Sets view type (UML-compliant setter)."""
        self._view = view

    def is_jacuzzi(self) -> bool:
        """Returns jacuzzi status (UML-compliant method)."""
        return self._jacuzzi

    def set_jacuzzi(self, has_jacuzzi: bool) -> None:
        """Sets jacuzzi status (UML-compliant setter)."""
        self._jacuzzi = has_jacuzzi

    def is_breakfast_included(self) -> bool:
        """Returns breakfast status (UML-compliant method)."""
        return self._breakfast_included

    def set_breakfast_included(self, includes_breakfast: bool) -> None:
        """Sets breakfast status (UML-compliant setter)."""
        self._breakfast_included = includes_breakfast

    # NON-UML ELEMENTS (justified additions)
    def __str__(self) -> str:
        """Standard Python string representation (not in UML)."""
        return (f"Deluxe Room {self.get_room_number()}: "
                f"View: {self._view}, "
                f"Jacuzzi: {'Yes' if self._jacuzzi else 'No'}, "
                f"Breakfast: {'Included' if self._breakfast_included else 'Extra'}")