import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/bluestock_mf.db")

checks = [
    ("dim_fund", "data/processed/fund_master_clean.csv"),
    ("fact_nav", "data/processed/nav_history_clean.csv"),
    ("fact_transactions", "data/processed/investor_transactions_clean.csv"),
    ("fact_performance", "data/processed/scheme_performance_clean.csv")
]

print("\nROW COUNT VERIFICATION")
print("=" * 50)

for table_name, csv_path in checks:

    csv_rows = len(pd.read_csv(csv_path))

    query = f"SELECT COUNT(*) FROM {table_name}"
    db_rows = pd.read_sql(query, conn).iloc[0, 0]

    status = "MATCH" if csv_rows == db_rows else "MISMATCH"

    print(f"{table_name}")
    print(f"CSV Rows : {csv_rows}")
    print(f"DB Rows  : {db_rows}")
    print(f"Status   : {status}")
    print("-" * 50)

conn.close()