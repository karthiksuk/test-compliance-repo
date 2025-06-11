from src.accounts import ProprietaryAccount, CustomerAccount, Trade
from src.processing import process_trades

if __name__ == "__main__":
    # --- Sample Data ---
    # Create account instances
    house_account = ProprietaryAccount(account_id="prop-001", holder="Our Firm")
    customer_a_account = CustomerAccount(account_id="cust-123", holder="Customer A")
    customer_b_account = CustomerAccount(account_id="cust-456", holder="Customer B")

    accounts_map = {
        "prop-001": house_account,
        "cust-123": customer_a_account,
        "cust-456": customer_b_account,
    }

    # Create a list of trades
    sample_trades = [
        Trade(trade_id="t-prop-01", account_id="prop-001", amount=1_000_000, instrument="US-T Bill"),
        Trade(trade_id="t-cust-a-01", account_id="cust-123", amount=500_000, instrument="US-T Bond"),
        Trade(trade_id="t-cust-b-01", account_id="cust-456", amount=250_000, instrument="US-T Bill"),
        Trade(trade_id="t-prop-02", account_id="prop-001", amount=2_000_000, instrument="US-T Bond"),
    ]

    # --- Run the flawed processing logic ---
    process_trades(sample_trades, accounts_map)