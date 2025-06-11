from typing import List, Dict
from .accounts import Account, Trade

# --- FLAW: DATA SEGREGATION VIOLATION ---
# This function is the primary violation of the FICC rule.
# It mixes proprietary and customer trades into a single margin calculation.
def calculate_portfolio_margin(trades: List[Trade], accounts: Dict[str, Account]) -> float:
    """
    Calculates the total margin requirement for a portfolio of trades.
    This function VIOLATES the rule by not separating proprietary and customer assets.
    """
    total_exposure = 0
    print("\nCalculating portfolio margin for all trades...")
    
    # It loops through all trades without separating them by account type.
    for trade in trades:
        print(f"  - Processing Trade {trade.trade_id} from account {trade.account_id}. Amount: {trade.amount}")
        total_exposure += trade.amount

    # A single margin calculation is applied to the combined exposure. This is the violation.
    margin_rate = 0.15 # 15%
    total_margin = total_exposure * margin_rate
    
    print(f"Total combined exposure: {total_exposure}")
    print(f"Final calculated margin (15%): {total_margin}")
    return total_margin
