

## 🧱 Code Quality & Project Rules

### Code Standards  
- Follow [PEP8](https://peps.python.org/pep-0008/) (lint: `flake8`)
- Use `snake_case` for variables/functions; `PascalCase` for classes  
- Every class/function *must* have type hints and docstrings  
- One class or _closely related_ function set per file

### Python Unit-Based Guidance

#### Unit 6: OOP
- Business logic in classes: `Asset`, `Portfolio`, `RiskModel`
- Use inheritance for asset types, polymorphism for models
- Absolute *no globals*: use instance state/config injection

#### Unit 7: Data Handling
- All data wrangling: `pandas`/`numpy`
- Consistent input/output (CSV/parquet)
- Handle all missing/invalid values (no silent NaNs!)
- Validate data joins for integrity

#### Unit 8: Exception Handling & Debugging
- Wrap every I/O/API/db in `try/except`
- Log using `/utils/logger.py` _at the right event level_: error, warning, info
- Custom exceptions on failures; no silent or catch-all excepts

#### Unit 9: Regex & String Manipulation
- Regex for market cap, ticker verification/cleaning
- Avoid manual string parsing; use regex or pandas string methods

#### Unit 10: Algorithms & Data Structures
- Financial metrics: favor vectorized numpy/pandas
- Pick right structure: `list` (ordered), `set` (uniqueness), `dict` (fast lookup)
- Comment all custom algorithms

#### Unit 11: Graphics & Reporting
- Use Matplotlib/Plotly for charts; all charts need a title, axes, legend
- Reports: templated with Jinja2, converted to PDF (pdfkit or similar)
- Prefer Builder pattern for multi-step generation

#### Unit 12: Advanced Programming
- FastAPI for modular, real-time API endpoints; validate input with Pydantic
- Apply design patterns: Factory, Strategy, Singleton, Builder, Observer, Repository, Adapter (e.g., Supabase→pandas)

---

## 🧪 Testing & Validation

- Use pytest; maintain 80%+ coverage
- Mock all Supabase/API dependencies
- Must test: data ingestion, analysis/model outputs, reporting, API behavior

---


## 🔐 Security & Config

- All secrets/config in `.env` (never in code)
- `.env.example` updated with new vars (i.e. `SUPABASE_URL`, `SUPABASE_KEY`)
- Never commit keys, tokens, passwords

---

## 🧹 Pre-Submission Checklist

- All classes fully documented (docstrings, type hints)
- Errors and key events logged
- Passes all linting/tests (run `flake8`, `pytest`)
- No secrets/checkpoint data committed

---

## 📃 License & Credits

This project is for advanced Python/finance instruction & simulation use only.

---

Thanks for making HedgeAI better! 🙌 Let’s build something robust, pythonic, and innovative. 🐍

---
