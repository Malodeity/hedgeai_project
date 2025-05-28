"""
📦 FILE: report.py

🎯 Unit 11 & 12: PDF Report Endpoint

✅ Expectations:
- Trigger generation of PDF report from a FastAPI route
"""

from fastapi import APIRouter
from reports.generate_pdf import generate_pdf

router = APIRouter()

@router.get("/report")
def generate_portfolio_report():
    """
    TODO:
    - Call generate_pdf() with dummy data
    - Return message with success confirmation
    """
    sample_data = {
        "assets": [
            {"name": "AAPL", "price": 150.0},
            {"name": "GOOG", "price": 2800.0}
        ]
    }
    generate_pdf(sample_data)
    return {"message": "Report generated."}