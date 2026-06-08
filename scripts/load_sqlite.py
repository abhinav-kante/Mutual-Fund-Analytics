from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

pd.read_csv(
    "data/processed/fund_master_clean.csv"
).to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/nav_history_clean.csv"
).to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
).to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
).to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)