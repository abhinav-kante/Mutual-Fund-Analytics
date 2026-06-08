# Data Dictionary

## dim_fund

| Column Name       | Data Type | Description                                | Source             |
| ----------------- | --------- | ------------------------------------------ | ------------------ |
| amfi_code         | Integer   | Unique AMFI scheme identifier              | 01_fund_master.csv |
| fund_house        | Text      | Mutual fund company name                   | 01_fund_master.csv |
| scheme_name       | Text      | Name of the mutual fund scheme             | 01_fund_master.csv |
| category          | Text      | Fund category (Equity, Debt, Hybrid, etc.) | 01_fund_master.csv |
| sub_category      | Text      | Detailed scheme classification             | 01_fund_master.csv |
| plan              | Text      | Direct or Regular plan                     | 01_fund_master.csv |
| launch_date       | Date      | Scheme launch date                         | 01_fund_master.csv |
| benchmark         | Text      | Benchmark index used for comparison        | 01_fund_master.csv |
| expense_ratio_pct | Float     | Expense ratio percentage                   | 01_fund_master.csv |
| fund_manager      | Text      | Fund manager name                          | 01_fund_master.csv |

---

## fact_nav

| Column Name | Data Type | Description       | Source             |
| ----------- | --------- | ----------------- | ------------------ |
| amfi_code   | Integer   | Scheme identifier | 02_nav_history.csv |
| date        | Date      | NAV date          | 02_nav_history.csv |
| nav         | Float     | Net Asset Value   | 02_nav_history.csv |

---

## fact_transactions

| Column Name        | Data Type | Description                  | Source                       |
| ------------------ | --------- | ---------------------------- | ---------------------------- |
| investor_id        | Text      | Unique investor identifier   | 08_investor_transactions.csv |
| transaction_date   | Date      | Transaction date             | 08_investor_transactions.csv |
| amfi_code          | Integer   | Scheme identifier            | 08_investor_transactions.csv |
| transaction_type   | Text      | SIP, Lumpsum, Redemption     | 08_investor_transactions.csv |
| amount_inr         | Float     | Transaction amount in INR    | 08_investor_transactions.csv |
| state              | Text      | Investor state               | 08_investor_transactions.csv |
| city               | Text      | Investor city                | 08_investor_transactions.csv |
| city_tier          | Text      | Tier classification          | 08_investor_transactions.csv |
| age_group          | Text      | Investor age bucket          | 08_investor_transactions.csv |
| gender             | Text      | Investor gender              | 08_investor_transactions.csv |
| annual_income_lakh | Float     | Annual income in lakhs       | 08_investor_transactions.csv |
| payment_mode       | Text      | UPI, Net Banking, Card, etc. | 08_investor_transactions.csv |
| kyc_status         | Text      | KYC verification status      | 08_investor_transactions.csv |

---

## fact_performance

| Column Name        | Data Type | Description                         | Source                    |
| ------------------ | --------- | ----------------------------------- | ------------------------- |
| amfi_code          | Integer   | Scheme identifier                   | 07_scheme_performance.csv |
| return_1yr_pct     | Float     | One-year return percentage          | 07_scheme_performance.csv |
| return_3yr_pct     | Float     | Three-year return percentage        | 07_scheme_performance.csv |
| return_5yr_pct     | Float     | Five-year return percentage         | 07_scheme_performance.csv |
| benchmark_3yr_pct  | Float     | Benchmark return                    | 07_scheme_performance.csv |
| alpha              | Float     | Excess return measure               | 07_scheme_performance.csv |
| beta               | Float     | Market sensitivity measure          | 07_scheme_performance.csv |
| sharpe_ratio       | Float     | Risk-adjusted return metric         | 07_scheme_performance.csv |
| sortino_ratio      | Float     | Downside risk-adjusted metric       | 07_scheme_performance.csv |
| std_dev_ann_pct    | Float     | Annualized volatility               | 07_scheme_performance.csv |
| max_drawdown_pct   | Float     | Maximum observed loss               | 07_scheme_performance.csv |
| aum_crore          | Float     | Assets under management (crore INR) | 07_scheme_performance.csv |
| expense_ratio_pct  | Float     | Expense ratio percentage            | 07_scheme_performance.csv |
| morningstar_rating | Integer   | Morningstar rating                  | 07_scheme_performance.csv |
| risk_grade         | Text      | Risk classification                 | 07_scheme_performance.csv |
