import pandas as pd

files = [
    "data/raw/03_aum_by_fund_house.csv",
    "data/raw/04_monthly_sip_inflows.csv",
    "data/raw/05_category_inflows.csv",
    "data/raw/06_industry_folio_count.csv",
    "data/raw/09_portfolio_holdings.csv",
    "data/raw/10_benchmark_indices.csv"
]

for f in files:
    df = pd.read_csv(f)

    print("\n" + "=" * 60)
    print(f)
    print(df.columns.tolist())