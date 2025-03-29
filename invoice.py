"""Module for the Invoice class."""

class Invoice:
    """
    Represents a booking invoice.
    """

    def __init__(self, invoice_id: int, total_amount: float,
                 discounts: float, payment_method: str, booking_id: int,
                 payment_status: str):  # Added payment_status
        """
        Initializes Invoice with attributes.

        Args:
            invoice_id: Unique identifier.
            total_amount: Gross amount.
            discounts: Applied discounts.
            payment_method: Payment type.
            booking_id: Associated booking.
            payment_status: Status of payment.
        """
        self._invoice_id = invoice_id
        self._total_amount = total_amount
        self._discounts = discounts
        self._payment_method = payment_method
        self._booking_id = booking_id
        self._payment_status = payment_status  # Initialize payment_status

    # Getters and Setters
    def get_invoice_id(self) -> int:
        """Returns the invoice ID."""
        return self._invoice_id

    def set_invoice_id(self, invoice_id: int) -> None:
        """Sets the invoice ID."""
        self._invoice_id = invoice_id

    def get_total_amount(self) -> float:
        """Returns the total amount."""
        return self._total_amount

    def set_total_amount(self, amount: float) -> None:
        """Sets the total amount."""
        self._total_amount = amount

    def get_discounts(self) -> float:
        """Returns the discounts."""
        return self._discounts

    def set_discounts(self, discounts: float) -> None:
        """Sets the discounts."""
        self._discounts = discounts

    def get_payment_method(self) -> str:
        """Returns the payment method."""
        return self._payment_method

    def set_payment_method(self, method: str) -> None:
        """Sets the payment method."""
        self._payment_method = method

    def get_booking_id(self) -> int:
        """Returns the booking ID."""
        return self._booking_id

    def set_booking_id(self, booking_id: int) -> None:
        """Sets the booking ID."""
        self._booking_id = booking_id

    def get_payment_status(self) -> str:
        """Returns the payment status."""
        return self._payment_status

    def set_payment_status(self, status: str) -> None:
        """Sets the payment status."""
        self._payment_status = status

    # UML-REQUIRED METHODS
    def calculate_total(self) -> float:
        """Calculates final amount after discounts."""
        return self._total_amount - self._discounts

    def process_payment(self) -> bool:
        """
        Processes the payment.

        Returns:
            True if payment is successful, False otherwise.
        """
        #  Placeholder implementation.
        #  Needs actual payment processing logic.
        #  For now, just assume it's successful.
        return True

    def __str__(self) -> str:
        """Returns a string representation of the invoice."""
        return (f"Invoice #{self._invoice_id}: "
                f"Total: ${self._total_amount:.2f}, "
                f"Discounts: ${self._discounts:.2f}, "
                f"Final: ${self.calculate_total():.2f}, "
                f"Payment: {self._payment_method}, "
                f"Booking ID: {self._booking_id}, "
                f"Status: {self._payment_status}")  # Added payment_status