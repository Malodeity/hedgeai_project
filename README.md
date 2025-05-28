# 📈 HedgeAI – Investment Analytics & Risk Intelligence Platform

## 🧠 Overview

HedgeAI is a modular, Python-based investment analytics platform designed for hedge funds, portfolio managers, and financial analysts. It enables risk classification, return forecasting, and real-time reporting using clean object-oriented design and modern APIs.

The platform integrates data from Supabase, processes it through a custom data pipeline, and exposes results via FastAPI and Power BI dashboards. It is built to reflect professional software engineering and data science practices while fulfilling Python curriculum units 6 through 12.

---
## 🎯 Expanded Project Objectives

1. **Ingest and Preprocess Stock Price and Company Metadata**
   - **Source**: Data is pulled from Supabase, where two tables are hosted:
     - `stock_market_data` Fields: Date, Open, High, Low, Close, Adj Close, Volume, Name, Company Name
     - `company_info` Fields: Symbol, Company Name, Industry, Market Cap
   - **Goals**:
     - Securely load data using a Supabase connection
     - Merge datasets on ticker symbol (Name = Symbols)
     - Handle missing data, date parsing, and data type conversions
     - Parse text values (e.g., “45.3B”) into machine-readable formats
   - **Output**: A clean, merged dataset stored in `/data/processed/` for further use

2. **Analyze Asset-Level Risk Using Financial Metrics**
   - **Metrics Implemented**:
     - Volatility (e.g., rolling 20-day standard deviation of returns)
     - Sharpe Ratio (risk-adjusted return using optional risk-free rate)
     - Drawdown (peak-to-trough loss metric)
   - **Risk Classification**:
     - Assets are categorized into low, medium, or high risk
     - Based on volatility thresholds and historical performance
   - **Business Value**:
     - Helps portfolio managers rebalance based on risk exposure
     - Supports compliance and stress testing

3. **Forecast Future Returns Using Machine Learning**
   - **Modeling Techniques**:
     - Linear Regression or Random Forests for supervised forecasting
     - Use momentum, volume, and past return features
   - **Model Architecture**:
     - Modular with Strategy pattern—allows for easy model switching
   - **Output Includes**:
     - Expected return (30-day horizon)
     - Confidence score
     - Directional flag: Bullish, Bearish, Neutral
   - **Educational Outcome**:
     - Applies regression modeling from Unit 10
     - Uses design patterns from Unit 12 to decouple model logic

4. **Generate Automated PDF/HTML Portfolio Reports**
   - **Format**:
     - HTML template (via Jinja2)
     - Converted into a PDF report (via pdfkit)
   - **Content Includes**:
     - Portfolio value over time
     - Asset allocation (pie chart)
     - Risk classification (histogram)
     - Top 5 risky assets
     - Predicted returns with confidence intervals
   - **Generation**:
     - Automatic via data pipeline (daily)
     - On-demand via API (/report/generate route)
   - **Stakeholder Impact**:
     - Enables non-technical managers to receive actionable summaries

5. **Expose Real-Time Insights via a FastAPI REST API**
   - **Technology**: FastAPI + Uvicorn
   - **Endpoints Include**:
     - `/portfolio/summary`: Key metrics and allocation
     - `/risk/levels`: Asset-by-asset risk classification
     - `/predict/returns`: Model-driven return forecast
     - `/report/generate`: Generate report and return download link
   - **Design Considerations**:
     - Input validation via Pydantic
     - Response schemas for client-side consumption
     - Logging and error handling aligned with Unit 8
   - **Real Use Case**:
     - Integrates with internal dashboards or alerting systems

6. **Visualize Data in Power BI Dashboards**
   - **Data Sources**:
     - Cleaned portfolio CSVs from `/data/powerbi/`
     - Optional: API integration via Power BI Web connector
   - **Dashboards Include**:
     - Portfolio Overview (value trend, allocation)
     - Risk Intelligence (risk classes, correlation heatmap)
     - Predictive Insights (forecast tables, KPIs)
     - Report Archive (download links to PDF/HTML)
   - **Audience**: Executives, analysts, and risk teams

7. **Demonstrate Advanced Python Design and Development Concepts**
   - **Design Patterns Implemented**:
     - Factory: for creating different asset types
     - Strategy: for switching ML
     - Singleton: for shared DB/config instances
     - Builder: for dynamic report generation
     - Observer: for triggering alerts or reports
     - Repository: to abstract DB layer
     - Adapter: for converting Supabase → pandas formats
	 - Coding Practices:
	 - Full use of OOP and encapsulation
	 - Exception-safe, testable, modular codebase
     - High test coverage (≥ 80%) using pytest

---
## 📚 Learning Units Covered

| Unit | Topic                           | Implementation                                          |
|------|---------------------------------|---------------------------------------------------------|
| 6    | Object-Oriented Programming     | Asset and Portfolio classes, factory & strategy patterns|
| 7    | Data Handling                   | Supabase integration, pandas preprocessing              |
| 8    | Exception Handling              | Robust error and log handling in pipeline and API       |
| 9    | Regex & String Manipulation     | Market cap parsing, symbol cleaning                     |
| 10   | Algorithms and Data Structures  | Risk metrics, return prediction, correlation            |
| 11   | Graphics & GUI Programming      | PDF/HTML reports with charts                            |
| 12   | Advanced Programming Techniques | FastAPI, Singleton, Strategy, Builder patterns          |

---

## 🧱 Project Structure

```
hedgeai_project/
├── api/routes/                # FastAPI endpoints
├── analytics/                 # ML models and risk analysis
├── models/                    # Asset and Portfolio class definitions
├── pipeline/                  # ETL jobs and data ingestion
├── reports/templates/         # Jinja2 HTML templates
├── tests/                     # Pytest suites for core modules
├── utils/                     # Logging, config, adapters
├── data/raw/                  # Input datasets from Supabase
├── data/processed/            # Cleaned datasets for modeling and BI
├── data/powerbi/              # Power BI-friendly export snapshots
├── logs/                      # Application log files
├── .env.example               # Environment variable sample
├── README.md                  # Project overview (this file)
├── requirements.txt           # Python dependencies
├── CONTRIBUTING.md            # Rules for contributors
└── DEVELOPMENT_GUIDE.md       # Weekly dev plan and setup guide
```

---

## 🛠️ Tools & Technologies

- Language: Python 3.10+
- Database: Supabase (PostgreSQL)
- Libraries: pandas, numpy, scikit-learn, matplotlib, plotly, jinja2, pdfkit
- API: FastAPI + Uvicorn
- Testing: Pytest, Coverage
- Visualization: Power BI (external dashboard)
- CI/CD: GitHub, GitHub Actions (optional)

---

## 📆 Weekly Development Plan

| Week | Focus                      | Key Deliverables                                 |
|------|----------------------------|--------------------------------------------------|
| 1    | Risk Analytics Engine      | OOP classes, volatility, Sharpe ratio            |
| 2    | Data Ingestion & Cleaning  | Supabase fetch, regex parsing, ETL pipeline      |
| 3    | Report Generation          | Jinja2 HTML + Matplotlib PDF reports             |
| 4    | FastAPI Setup              | REST endpoints for summary, risk, reports        |
| 5    | Return Prediction Module   | ML model, strategy pattern, forecast route       |
| 6    | BI Integration & Final QA  | Power BI, testing, documentation                 |

---

## 📌 Usage Summary

- Start the project by building data classes in `/models`
- Use `/pipeline` to ingest and process stock data
- Analyze risk and forecast returns via `/analytics`
- Serve real-time results with `/api`
- Generate PDF reports using `/reports`
- Export data for visualization in `/data/powerbi/`

---

## 📃 License & Credits

This project is for educational and instructional use, tailored for advanced Python learning and hedge fund use-case simulation.

---