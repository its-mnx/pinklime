"""Module for the PremiumService class, managing premium guest services."""

from guest_service import GuestService  # For inheritance

class PremiumService(GuestService):
    """
    Represents premium guest services, inheriting from GuestService.
    Adds attributes specific to premium services.
    """

    def __init__(self, service_id: int, service_type: str, status: str,
                 guest_id: int, request_time: str,
                 premium_level: str, specialized_staff: bool, exclusive_access: bool):
        """
        Initializes PremiumService with:
        - Inherited attributes from GuestService.
        - Premium-specific attributes.
        """
        super().__init__(service_id, service_type, status, guest_id, request_time)
        # Additional attributes for premium services.
        self._premium_level = premium_level
        self._specialized_staff = specialized_staff
        self._exclusive_access = exclusive_access

    def get_premium_level(self) -> str:
        """Returns the premium service level."""
        return self._premium_level

    def set_premium_level(self, level: str) -> None:
        """Sets the premium service level."""
        self._premium_level = level

    def get_specialized_staff(self) -> bool:
        """Returns whether specialized staff is assigned."""
        return self._specialized_staff

    def set_specialized_staff(self, has_specialized_staff: bool) -> None:
        """Sets whether specialized staff is assigned."""
        self._specialized_staff = has_specialized_staff

    def get_exclusive_access(self) -> bool:
        """Returns whether exclusive access is granted."""
        return self._exclusive_access

    def set_exclusive_access(self, has_exclusive_access: bool) -> None:
        """Sets whether exclusive access is granted."""
        self._exclusive_access = has_exclusive_access

    def __str__(self) -> str:
        """Returns a string representation of the premium service."""
        # Construct a string that displays premium service information.
        return (f"Premium Service #{self.get_service_id()}: "
                f"Level: {self._premium_level}, "
                f"Specialized: {'Yes' if self._specialized_staff else 'No'}, "
                f"Exclusive: {'Yes' if self._exclusive_access else 'No'}")