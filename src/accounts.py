from dataclasses import dataclass

@dataclass
class Trade:
    trade_id: str
    account_id: str
    amount: float
    instrument: str

class Account:
    """Base class for financial accounts."""
    def __init__(self, account_id: str, holder: str):
        self.account_id = account_id
        self.holder = holder

class ProprietaryAccount(Account):
    """Represents the firm's own trading account (house account)."""
    def __init__(self, account_id: str, holder: str):
        super().__init__(account_id, holder)
        self.type = "PROPRIETARY"

class CustomerAccount(Account):
    """Represents a customer's trading account."""
    def __init__(self, account_id: str, holder: str):
        super().__init__(account_id, holder)
        self.type = "CUSTOMER"