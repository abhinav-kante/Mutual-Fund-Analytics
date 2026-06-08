-- 1 Top 5 Fund Houses by AUM
SELECT d.fund_house,
       SUM(f.aum_crore) AS total_aum
FROM fact_performance f
JOIN dim_fund d
ON f.amfi_code = d.amfi_code
GROUP BY d.fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- 2
SELECT strftime('%Y-%m', date),
AVG(nav)
FROM fact_nav
GROUP BY 1;

-- 3
SELECT
strftime('%Y', transaction_date),
SUM(amount_inr)
FROM fact_transactions
WHERE transaction_type='SIP'
GROUP BY 1;

-- 4
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 5 Funds with Expense Ratio Below 1%
SELECT d.scheme_name,
       f.expense_ratio_pct
FROM fact_performance f
JOIN dim_fund d
ON f.amfi_code = d.amfi_code
WHERE f.expense_ratio_pct < 1;

-- 6 Top Sharpe Ratio Funds
SELECT scheme_name,
       sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 7 Highest AUM Schemes
SELECT scheme_name,
       aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 10;

-- 8 Highest Alpha Funds
SELECT scheme_name,
       alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 10;

-- 9 Category-wise Average Return
SELECT d.category,
       AVG(f.return_3yr_pct) AS avg_return_3yr
FROM fact_performance f
JOIN dim_fund d
ON f.amfi_code = d.amfi_code
GROUP BY d.category
ORDER BY avg_return_3yr DESC;

-- 10 Risk Grade Distribution
SELECT risk_grade,
       COUNT(*) AS fund_count
FROM fact_performance
GROUP BY risk_grade
ORDER BY fund_count DESC;