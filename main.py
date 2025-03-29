# main.py
"""
Royal Stay Hotel Management System - Main Application
Updated for separate Room/DeluxeRoom files
"""

from datetime import datetime, timedelta
from room import Room
from deluxe_room import DeluxeRoom
from guest import Guest
from vip_guest import VIPGuest
from booking import Booking
from invoice import Invoice
from feedback import Feedback
from guest_service import GuestService
from premium_service import PremiumService
from loyalty_program import LoyaltyProgram

def initialize_sample_data():
    """Creates sample data for demonstration."""
    # Initialize rooms
    standard_room = Room(101, "Standard", 99.99)
    deluxe_room = DeluxeRoom(201, 199.99, "Ocean", True, True)

    # Initialize guests
    regular_guest = Guest(1, "Ali AlKhaldi", "alice@email.com", "Silver")
    vip_guest = VIPGuest(2, "Rashid AlHashmi", "bob@email.com", True, True, False)

    # Initialize bookings
    today = datetime.now()
    booking1 = Booking(
        1,
        regular_guest.get_guest_id(),
        standard_room.get_room_number(),
        (today + timedelta(days=1)).strftime("%Y-%m-%d"),
        (today + timedelta(days=3)).strftime("%Y-%m-%d")
    )

    booking2 = Booking(
        2,
        vip_guest.get_guest_id(),
        deluxe_room.get_room_number(),
        (today + timedelta(days=5)).strftime("%Y-%m-%d"),
        (today + timedelta(days=10)).strftime("%Y-%m-%d")
    )

    # Initialize invoices
    invoice1 = Invoice(1, 199.98, 0.00, "Credit Card", 1, "Paid")  # Added payment_status
    invoice2 = Invoice(2, 999.95, 100.00, "Bank Transfer", 2, "Pending")  # Added payment_status

    # Initialize services
    service1 = GuestService(1, "Room Service", "Pending", 2, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    premium_service = PremiumService(2, "Spa Treatment", "Scheduled", 2,
                                   (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S"),
                                   "Platinum", True, True)

    # Initialize loyalty program
    loyalty = LoyaltyProgram(1500, ["Free Night", "Room Upgrade"], 2, "Gold", "2023-12-31")

    # Initialize feedback
    feedback = Feedback(1, 4.5, "Great stay!", 1, datetime.now().strftime("%Y-%m-%d"))

    return {
        "rooms": [standard_room, deluxe_room],
        "guests": [regular_guest, vip_guest],
        "bookings": [booking1, booking2],
        "invoices": [invoice1, invoice2],
        "services": [service1, premium_service],
        "loyalty": loyalty,
        "feedback": feedback
    }

def demonstrate_system(data):
    """Demonstrates all system features with detailed and organized output."""
    print("\n=== ROOMS ===")
    for room in data["rooms"]:
        print(f"  {room}")
        if isinstance(room, DeluxeRoom):
            print(f"    - View: {room.get_view()}")
            print(f"    - Jacuzzi: {'Yes' if room.is_jacuzzi() else 'No'}")
            print(f"    - Breakfast: {'Included' if room.is_breakfast_included() else 'Not Included'}")

    print("\n=== GUESTS ===")
    for guest in data["guests"]:
        print(f"  {guest}")
        if isinstance(guest, VIPGuest):
            print(f"    - Personal Assistant: {'Yes' if guest.get_personal_assistant() else 'No'}")
            print(f"    - Private Transportation: {'Yes' if guest.get_private_transportation() else 'No'}")
            print(f"    - Dedicated Concierge: {'Yes' if guest.get_dedicated_concierge() else 'No'}")

    print("\n=== BOOKINGS ===")
    for booking in data["bookings"]:
        print(f"  {booking.generate_booking_summary()}")
        print(f"    - Duration: {booking.calculate_booking_duration()} nights")

    print("\n=== SERVICES ===")
    for service in data["services"]:
        print(f"  {service}")
        if isinstance(service, PremiumService):
            print(f"    - Premium Level: {service.get_premium_level()}")

    print("\n=== INVOICES ===")
    for invoice in data["invoices"]:
      print(f"  {invoice}")

    print("\n=== FEEDBACK ===")
    print(f"   {data['feedback']}")

    print("\n=== LOYALTY PROGRAM ===")
    print(f"   {data['loyalty']}")

def main():
    """Entry point for the application"""
    print("=== ROYAL STAY HOTEL SYSTEM ===")
    hotel_data = initialize_sample_data()
    demonstrate_system(hotel_data)
    print("\nSystem demonstration completed successfully!")

if __name__ == "__main__":
    main()