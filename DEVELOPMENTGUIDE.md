# 📊 HedgeAI Project

HedgeAI is a risk analytics platform that ingests financial data, performs portfolio risk analysis using machine learning models, and generates professional reports and Power BI dashboards.

---

## 🧰 Tech Stack

- **Backend:** FastAPI  
- **ML & Analytics:** Python (Pandas, NumPy, Scikit-learn)  
- **Templating:** Jinja2  
- **BI Integration:** Power BI (exportable datasets)  
- **Database:** Supabase (as source for raw datasets)  
- **Environment:** `.env` configuration  

---

## 📦 Prerequisites

Before starting, make sure you have the following installed:

- [Python 3.10+](https://www.python.org/)
- [pip](https://pip.pypa.io/)
- [Git](https://git-scm.com/)
- [Power BI Desktop](https://powerbi.microsoft.com/)
- (Optional) [Poetry](https://python-poetry.org/) or [virtualenv](https://virtualenv.pypa.io/)

---

# 📅 Development Guide for HedgeAI

## 📜 Overview

This document provides a structured plan for developers on setting up, running, and contributing to the HedgeAI project, a risk analytics platform designed to handle financial data analysis and reporting.

---

## 🏗️ 3-Week Development Plan

- **Week 1: Initial Setup & Risk Analytics**
  - Set up the development environment and establish connections to Supabase.
  - Develop OOP classes for assets and portfolios.
  - Implement risk metrics like volatility and the Sharpe ratio.

- **Week 2: Data Handling & Report Generation**
  - Use Pandas for data cleaning and preprocessing; handle missing values and normalization.
  - Create ETL pipelines for data ingestion.
  - Generate PDF and HTML reports using Jinja2 and pdfkit. Design templates in `reports/templates/`.

- **Week 3: FastAPI Integration & BI Dashboard**
  - Integrate FastAPI to provide RESTful endpoints.
  - Implement endpoints for portfolio summaries and risk levels.
  - Export datasets for Power BI dashboard creation.
  - Conduct thorough testing and documentation.

---

## 👩‍💻 Weekly Meetings

We will meet for 2 hours every Friday to discuss progress, challenges, and next steps. These meetings will help ensure that the project stays on track and any issues are promptly addressed.

---

## 👨‍💻 Setup Steps
### Clone the Repository

```bash
git clone https://github.com/your-username/hedgeai_project.git
cd hedgeai_project
