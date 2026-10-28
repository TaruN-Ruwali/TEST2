"""Order management and fulfillment module."""
from app.billing import process_charge, calculate_discount
from app.db import get_balance


def create_order(account_id: str, items_total: float, discount_pct: float = 0.0) -> dict:
    """Creates a new order, applies discount, and processes charge."""
    final_amount = calculate_discount(items_total, discount_pct)
    
    current_balance = get_balance(account_id)
    if current_balance < final_amount:
        return {"status": "failed", "reason": "insufficient_balance", "amount": final_amount}

    success = process_charge(account_id, final_amount)
    if not success:
        return {"status": "failed", "reason": "charge_failed", "amount": final_amount}

    return {"status": "success", "amount_charged": final_amount, "account_id": account_id}

