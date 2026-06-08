import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

pd.read_csv(
    "data/processed/fund_master_clean.csv"
).to_sql(
    "dim_fund",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/nav_history_clean.csv"
).to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
).to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
).to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database loaded successfully")