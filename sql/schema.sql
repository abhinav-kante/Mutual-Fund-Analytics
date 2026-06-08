CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
fund_house TEXT,
scheme_name TEXT,
category TEXT,
sub_category TEXT,
fund_manager TEXT
);

CREATE TABLE dim_date (
date_id INTEGER PRIMARY KEY,
full_date DATE,
year INTEGER,
month INTEGER,
quarter INTEGER
);

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
date_id INTEGER,
nav REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id TEXT,
amfi_code INTEGER,
transaction_date DATE,
transaction_type TEXT,
amount_inr REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
perf_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
sharpe_ratio REAL,
beta REAL,
alpha REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
aum_crore REAL,
FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);
