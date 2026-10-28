"""Unit tests for billing and charge verification."""
from app.billing import process_charge, calculate_discount


def test_positive_charge_succeeds():
    assert process_charge("acc_user_1", 50.0) is True


def test_zero_amount_charge_fails():
    assert process_charge("acc_user_1", 0.0) is False


def test_negative_amount_charge_rejected():
    """
    CRITICAL INVARIANT: Negative charge amounts must be strictly rejected
    and return False to prevent balance inflation!
    """
    assert process_charge("acc_user_1", -100.0) is False


def test_discount_calculation():
    assert calculate_discount(200.0, 25.0) == 150.0

