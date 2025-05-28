"""
📦 FILE: test_risk.py

🎯 Units: OOP + Strategy Testing

✅ Expectations:
- Verify RiskModel polymorphism works
"""

from analytics.risk_model import RiskModel
from models.asset import Asset
from models.portfolio import Portfolio

def test_dummy_risk():
    class DummyRisk(RiskModel):
        def calculate(self, portfolio):
            return 42.0

    assets = [Asset("TEST", 100)]
    portfolio = Portfolio(assets)
    model = DummyRisk()

    assert model.calculate(portfolio) == 42.0