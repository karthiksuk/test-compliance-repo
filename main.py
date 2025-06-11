from src.accounts import ProprietaryAccount, CustomerAccount, Trade
from src.processing import calculate_portfolio_margin

if __name__ == "__main__":
    # --- Sample Data ---
    house_account = ProprietaryAccount(account_id="prop-001", holder="Our Firm")
    customer_account = CustomerAccount(account_id="cust-123", holder="Customer A")
    accounts_map = {"prop-001": house_account, "cust-123": customer_account}

    # A mix of proprietary and customer trades
    sample_trades = [
        Trade(trade_id="t-prop-01", account_id="prop-001", amount=1_000_000, instrument="US-T Bill"),
        Trade(trade_id="t-cust-a-01", account_id="cust-123", amount=500_000, instrument="US-T Bond"),
    ]

    # --- Run the flawed processing logic ---
    calculate_portfolio_margin(sample_trades, accounts_map)
