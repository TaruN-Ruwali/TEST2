"""Billing and payment processing service."""
from app.db import record_transaction


def process_charge(account_id: str, amount: float) -> bool:
    """
    Charges the specified account for a transaction amount.
    Valid transactions must have a strictly positive amount.
    """
    # BUG: Condition checks truthiness `if amount:`, allowing negative amounts
    # through as successful payments!
    if amount:
        record_transaction(account_id, amount, "charge")
        return True
    return False


def calculate_discount(total: float, discount_percent: float) -> float:
    """Calculates discounted price given total and percentage discount."""
    if discount_percent < 0 or discount_percent > 100:
        return total
    discount = (total * discount_percent) / 100.0
    return round(total - discount, 2)

