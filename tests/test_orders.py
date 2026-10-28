"""Integration tests for order creation lifecycle."""
from app.orders import create_order


def test_order_creation_success():
    result = create_order("acc_user_1", items_total=100.0, discount_pct=10.0)
    assert result["status"] == "success"
    assert result["amount_charged"] == 90.0


def test_order_creation_insufficient_funds():
    result = create_order("acc_user_1", items_total=1000.0)
    assert result["status"] == "failed"
    assert result["reason"] == "insufficient_balance"

