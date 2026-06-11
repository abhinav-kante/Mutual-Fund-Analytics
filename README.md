# Bluestock Mutual Fund Analytics Capstone Project

## Project Overview

The Bluestock Mutual Fund Analytics Capstone Project is an end-to-end data analytics solution designed to analyze mutual fund performance, investor behavior, SIP trends, portfolio risk, and industry growth.

The project combines Data Engineering, Data Analytics, Financial Risk Modeling, SQL, Python, and Power BI to transform raw mutual fund datasets into actionable business insights.

---

## Business Objectives

* Analyze mutual fund performance across schemes.
* Study AUM and SIP growth trends.
* Evaluate risk-adjusted returns.
* Understand investor transaction behavior.
* Build advanced risk analytics models.
* Develop an interactive Power BI dashboard.
* Generate investment recommendations.

---

## Technology Stack

### Programming & Analytics

* Python
* Pandas
* NumPy
* SciPy
* Matplotlib
* Seaborn
* Plotly

### Database

* SQLite
* SQLAlchemy

### Visualization

* Power BI

### Version Control

* Git
* GitHub

---

## Project Architecture

Raw CSV Data
→ ETL Pipeline
→ Data Cleaning & Validation
→ SQLite Database
→ Exploratory Data Analysis
→ Performance Analytics
→ Advanced Analytics
→ Power BI Dashboard
→ Business Insights

---

## Datasets Used

1. Fund Master Dataset
2. NAV History Dataset
3. AUM by Fund House
4. Monthly SIP Inflows
5. Category Inflows
6. Industry Folio Counts
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Key Features

### ETL Pipeline

* Automated data ingestion
* Data validation
* Missing value handling
* Date standardization
* Clean dataset generation

### Exploratory Data Analysis

* NAV trend analysis
* AUM growth analysis
* SIP inflow analysis
* Investor demographics
* Category inflow analysis

### Performance Analytics

* CAGR
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Fund Scorecard

### Advanced Analytics

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling 90-Day Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Sector HHI Concentration Analysis
* Fund Recommendation Engine

### Dashboard Analytics

* Industry Overview
* Fund Performance
* Investor Analytics
* SIP & Market Trends

---

## Dashboard Preview

### Industry Overview

Provides industry-wide KPIs including:

* Total AUM
* SIP Inflows
* Folios
* Scheme Count

### Fund Performance

Provides:

* Risk vs Return Analysis
* NAV Trends
* Fund Scorecards

### Investor Analytics

Provides:

* Geographic Analysis
* Investor Demographics
* Transaction Trends

### SIP & Market Trends

Provides:

* SIP Growth Trends
* Category Inflows
* Market Participation Insights

---

## Repository Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── data_cleaning.py
│   ├── load_sqlite.py
│   ├── run_pipeline.py
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   └── Advanced_Analytics.ipynb
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── Dashboard.pdf
│   └── screenshots/
│
├── reports/
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
│
└── README.md
```

## Key Deliverables

* SQLite Database
* ETL Pipeline
* EDA Notebook
* Performance Analytics Notebook
* Advanced Analytics Notebook
* Power BI Dashboard
* Final Project Report
* Project Presentation

---

## Skills Demonstrated

* Data Cleaning
* Data Engineering
* SQL Querying
* Database Design
* Financial Analytics
* Risk Analytics
* Statistical Analysis
* Data Visualization
* Dashboard Development
* Business Intelligence
* Git & GitHub

---

## Author

Abhinav Kante

B.Tech – Computer Science and Engineering

CMR Institute of Technology

GitHub:
https://github.com/abhinav-kante

LinkedIn:
https://www.linkedin.com/in/abhinav-kante/

---

## Version

Current Release: v1.0

Status: Completed
