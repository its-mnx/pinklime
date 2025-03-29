"""Module for the GuestService class, managing guest service requests."""

from datetime import datetime

class GuestService:
    """
    Represents guest service requests exactly as defined in UML.
    Contains all attributes and methods specified in Part A.
    """

    def __init__(self, service_id: int, service_type: str, status: str,
                 guest_id: int, request_time: str):
        """
        Initializes GuestService with UML-specified attributes:
        - service_id: Unique identifier (int)
        - service_type: Type of service (str)
        - status: Current status (str)
        - guest_id: Associated guest ID (int)
        - request_time: When requested (str, செறிவு-MM-DD HH:MM:SS)
        """
        # UML-specified private attributes
        self._service_id = service_id
        self._service_type = service_type
        self._status = status
        self._guest_id = guest_id
        self._request_time = request_time

    # UML-REQUIRED METHODS (exact matches)
    def get_service_id(self) -> int:
        """Returns service ID (UML-compliant getter)."""
        return self._service_id

    def set_service_id(self, service_id: int) -> None:
        """Sets service ID (UML-compliant setter)."""
        self._service_id = service_id

    def get_service_type(self) -> str:
        """Returns service type (UML-compliant getter)."""
        return self._service_type

    def set_service_type(self, service_type: str) -> None:
        """Sets service type (UML-compliant setter)."""
        self._service_type = service_type

    def get_status(self) -> str:
        """Returns status (UML-compliant getter)."""
        return self._status

    def set_status(self, status: str) -> None:
        """Sets status (UML-compliant setter)."""
        self._status = status

    def get_guest_id(self) -> int:
        """Returns guest ID (UML-compliant getter)."""
        return self._guest_id

    def set_guest_id(self, guest_id: int) -> None:
        """Sets guest ID (UML-compliant setter)."""
        self._guest_id = guest_id

    def get_request_time(self) -> str:
        """Returns request time (UML-compliant getter)."""
        return self._request_time

    def set_request_time(self, request_time: str) -> None:
        """Sets request time (UML-compliant setter)."""
        # Validate request time format (YYYY-MM-DD HH:MM:SS)
        try:
            datetime.strptime(request_time, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            raise ValueError("Time must be in செறிவு-MM-DD HH:MM:SS format")
        self._request_time = request_time

    def mark_as_completed(self) -> None:
        """Marks service as completed (UML-required method)."""
        # Set the status to 'Completed'
        self._status = "Completed"

    # NON-UML ELEMENTS (justified additions)
    def __str__(self) -> str:
        """Standard Python string representation (not in UML)."""
        return (f"Service #{self._service_id}: {self._service_type} "
                f"(Status: {self._status})")