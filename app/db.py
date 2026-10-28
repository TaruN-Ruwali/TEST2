"""Mock database storage for accounts and transactions."""
from typing import Dict, Any, List

ACCOUNTS_TABLE: Dict[str, float] = {
    "acc_user_1": 500.0,
    "acc_user_2": 1250.0,
}

TRANSACTIONS_LOG: List[Dict[str, Any]] = []


def get_balance(account_id: str) -> float:
    return ACCOUNTS_TABLE.get(account_id, 0.0)


def record_transaction(account_id: str, amount: float, tx_type: str) -> bool:
    TRANSACTIONS_LOG.append({
        "account_id": account_id,
        "amount": amount,
        "type": tx_type
    })
    return True

