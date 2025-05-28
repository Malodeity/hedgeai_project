"""
📦 FILE: risk.py

🎯 Unit 12: FastAPI Risk Endpoint

✅ Expectations:
- Calculate and return a sample risk score from API
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/risk")
def get_risk_score():
    """
    TODO:
    - Instantiate a dummy RiskModel subclass
    - Return calculated risk score
    """
    return {"risk_score": "Risk model output placeholder"}