from typing import List, Dict
from .accounts import Account, ProprietaryAccount, CustomerAccount, Trade

# --- FLAW 1: INCOMPLETE CLASSIFICATION ---
# This function does not correctly handle all account types as required by the rule.
def classify_account_type(account: Account) -> str:
    """
    Classifies an account as 'proprietary' or 'customer'.
    This is intentionally incomplete to be non-compliant.
    """
    if isinstance(account, ProprietaryAccount):
        return "proprietary"
    else:
        # FIXME: This should explicitly check for CustomerAccount and raise an error
        # for unknown types, but currently it misclassifies.
        print(f"Warning: Account {account.account_id} is not a proprietary account. Treating as UNKNOWN.")
        return "UNKNOWN"

# --- FLAW 2: DATA SEGREGATION VIOLATION ---
# This function incorrectly mixes proprietary and customer data for margin calculation.
def calculate_portfolio_margin(trades: List[Trade], accounts: Dict[str, Account]) -> float:
    """
    Calculates the total margin requirement for a portfolio of trades.
    This function violates the rule by not separating proprietary and customer assets.
    """
    total_exposure = 0
    print("\nCalculating portfolio margin for all trades...")
    for trade in trades:
        account_type = classify_account_type(accounts[trade.account_id])
        print(f"  - Processing Trade {trade.trade_id} from a '{account_type}' account. Amount: {trade.amount}")
        total_exposure += trade.amount

    # A single margin calculation is applied to the combined exposure, which is incorrect.
    margin_rate = 0.15 # 15%
    total_margin = total_exposure * margin_rate
    
    print(f"Total combined exposure: {total_exposure}")
    print(f"Final calculated margin (15%): {total_margin}")
    return total_margin

def process_trades(trades: List[Trade], accounts: Dict[str, Account]):
    """
    Main processing function to simulate a daily trade processing job.
    """
    print("--- Starting Daily Trade Processing Job ---")
    
    # This call triggers the non-compliant margin calculation.
    margin_requirement = calculate_portfolio_margin(trades, accounts)
    
    print(f"\nTotal margin requirement for the day: ${margin_requirement:,.2f}")
    print("--- Daily Trade Processing Job Finished ---")
