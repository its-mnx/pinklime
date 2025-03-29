"""Module for the Feedback class, handling guest feedback."""

from datetime import datetime

class Feedback:
    """
    Represents guest feedback.
    """

    def __init__(self, feedback_id: int, rating: float, comments: str,
                 guest_id: int, feedback_date: str):
        """
        Initializes Feedback with attributes.

        Args:
            feedback_id: Unique identifier.
            rating: Numeric rating.
            comments: Feedback text.
            guest_id: Associated guest ID.
            feedback_date: Date of feedback.
        """
        self._feedback_id = feedback_id
        self._rating = rating
        self._comments = comments
        self._guest_id = guest_id
        self._feedback_date = feedback_date

    # Getters and Setters
    def get_feedback_id(self) -> int:
        """Returns the feedback ID."""
        return self._feedback_id

    def set_feedback_id(self, feedback_id: int) -> None:
        """Sets the feedback ID."""
        self._feedback_id = feedback_id

    def get_rating(self) -> float:
        """Returns the rating."""
        return self._rating

    def set_rating(self, rating: float) -> None:
        """Sets the rating."""
        self._rating = rating

    def get_comments(self) -> str:
        """Returns the comments."""
        return self._comments

    def set_comments(self, comments: str) -> None:
        """Sets the comments."""
        self._comments = comments

    def get_guest_id(self) -> int:
        """Returns the guest ID."""
        return self._guest_id

    def set_guest_id(self, guest_id: int) -> None:
        """Sets the guest ID."""
        self._guest_id = guest_id

    def get_feedback_date(self) -> str:
        """Returns the feedback date."""
        return self._feedback_date

    def set_feedback_date(self, date: str) -> None:
        """Sets the feedback date."""
        self._feedback_date = date

    # UML-REQUIRED METHODS
    def validate_rating(self) -> None:
        """Validates the rating."""
        # Add validation for rating range (1.0 to 5.0)
        if not 1.0 <= self._rating <= 5.0:
            raise ValueError("Rating must be between 1.0 and 5.0")

    def generate_feedback_summary(self) -> str:
        """Generates a feedback summary string."""
        return (f"Feedback #{self._feedback_id}: "
                f"Rating: {self._rating}/5, "
                f"Guest: {self._guest_id}")

    # NON-UML ELEMENTS
    def __str__(self) -> str:
        """Returns a string representation of the Feedback object."""
        return (f"Feedback #{self._feedback_id}: "
                f"Rating: {self._rating}/5, "
                f"Comment: {self._comments}, "
                f"Guest: {self._guest_id}, "
                f"Date: {self._feedback_date}")