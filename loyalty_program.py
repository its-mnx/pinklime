"""Module for the LoyaltyProgram class."""
from typing import List

class LoyaltyProgram:
    """
    Represents a loyalty program exactly as defined in UML.
    Contains all attributes and methods specified in Part A.
    """

    def __init__(self, points_earned: int, rewards_available: List[str],
                 guest_id: int, tier: str, points_expiry_date: str):
        """
        Initializes LoyaltyProgram with UML-specified attributes.
        """
        self._points_earned = points_earned
        self._rewards_available = rewards_available
        self._guest_id = guest_id
        self._tier = tier
        self._points_expiry_date = points_expiry_date

    def get_points_earned(self) -> int:
        """Returns earned points."""
        return self._points_earned

    def set_points_earned(self, points: int) -> None:
        """Sets earned points."""
        self._points_earned = points

    def get_rewards_available(self) -> List[str]:
        """Returns available rewards."""
        return self._rewards_available

    def set_rewards_available(self, rewards: List[str]) -> None:
        """Sets available rewards."""
        self._rewards_available = rewards

    def get_guest_id(self) -> int:
        """Returns guest ID."""
        return self._guest_id

    def set_guest_id(self, guest_id: int) -> None:
        """Sets guest ID."""
        self._guest_id = guest_id

    def get_tier(self) -> str:
        """Returns loyalty tier."""
        return self._tier

    def set_tier(self, tier: str) -> None:
        """Sets loyalty tier."""
        self._tier = tier

    def get_points_expiry_date(self) -> str:
        """Returns points expiry date."""
        return self._points_expiry_date

    def set_points_expiry_date(self, date: str) -> None:
        """Sets points expiry date."""
        self._points_expiry_date = date

    def redeem_points(self, points: int) -> str:
        """
        Redeems points for rewards.
        Returns: Name of redeemed reward or error message.
        """
        # Check if the guest has enough points to redeem.
        if points > self._points_earned:
            return "Not enough points"

        # Generate a placeholder reward string.
        # This would be more complex in a real system.
        reward = f"Reward for {points} points"

        # Deduct the redeemed points from the guest's total.
        self._points_earned -= points

        # Return the reward string.
        return reward

    def __str__(self) -> str:
        """String representation of the loyalty program."""
        return (f"Loyalty Program for Guest {self._guest_id}: "
                f"Tier: {self._tier}, Points: {self._points_earned}, "
                f"Benefits: {self._rewards_available}, "
                f"Expiration: {self._points_expiry_date}")