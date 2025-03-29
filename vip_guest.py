"""Module for the VIPGuest class, a specialized Guest with premium benefits."""

from guest import Guest

class VIPGuest(Guest):
    """
    Represents a VIP guest, inheriting from the Guest class.
    Adds attributes specific to VIP guests.
    """

    def __init__(self, guest_id: int, name: str, contact_info: str,
                 personal_assistant: bool, private_transportation: bool,
                 dedicated_concierge: bool):
        """
        Initializes a VIPGuest object.
        - Inherits guest_id, name, and contact_info from the Guest class.
        - Sets the guest's loyalty status to "VIP".
        - Adds attributes for VIP-specific services.
        """
        super().__init__(guest_id, name, contact_info, "VIP", [])  # Sets VIP status
        self._personal_assistant = personal_assistant
        self._private_transportation = private_transportation
        self._dedicated_concierge = dedicated_concierge

    def get_personal_assistant(self) -> bool:
        """Returns whether the guest has a personal assistant."""
        return self._personal_assistant

    def set_personal_assistant(self, has_assistant: bool) -> None:
        """Sets whether the guest has a personal assistant."""
        self._personal_assistant = has_assistant

    def get_private_transportation(self) -> bool:
        """Returns whether the guest has private transportation."""
        return self._private_transportation

    def set_private_transportation(self, has_transport: bool) -> None:
        """Sets whether the guest has private transportation."""
        self._private_transportation = has_transport

    def get_dedicated_concierge(self) -> bool:
        """Returns whether the guest has a dedicated concierge."""
        return self._dedicated_concierge

    def set_dedicated_concierge(self, has_concierge: bool) -> None:
        """Sets whether the guest has a dedicated concierge."""
        self._dedicated_concierge = has_concierge

    def __str__(self) -> str:
        """Returns a string representation of the VIP guest."""
        # Construct a string showing VIP guest details.
        return (f"VIP Guest {self.get_guest_id()}: {self.get_name()}\n"
                f"Services: Personal Assistant: {'Yes' if self._personal_assistant else 'No'}, "
                f"Private Transport: {'Yes' if self._private_transportation else 'No'}, "
                f"Dedicated Concierge: {'Yes' if self._dedicated_concierge else 'No'}")