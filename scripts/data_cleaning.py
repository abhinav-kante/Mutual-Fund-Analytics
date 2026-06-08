import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# ------------------------
# FUND MASTER
# ------------------------
fund = pd.read_csv("data/raw/01_fund_master.csv")

fund = fund.drop_duplicates()

fund.to_csv(
    "data/processed/fund_master_clean.csv",
    index=False
)

print("fund_master_clean.csv created")

# ------------------------
# NAV HISTORY
# ------------------------
nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

nav["nav"] = pd.to_numeric(
    nav["nav"],
    errors="coerce"
)

nav = nav.drop_duplicates()

nav = nav[nav["nav"] > 0]

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("nav_history_clean.csv created")

# ------------------------
# SCHEME PERFORMANCE
# ------------------------
perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

perf = perf.drop_duplicates()

perf.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("scheme_performance_clean.csv created")

# ------------------------
# INVESTOR TRANSACTIONS
# ------------------------
txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

txn = txn[
    txn["amount_inr"] > 0
]

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.strip()
)

txn = txn.drop_duplicates()

txn.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("investor_transactions_clean.csv created")

print("\nAll cleaned files generated successfully.")