"""
📦 FILE: test_asset.py

🎯 Unit: Testing & Validation

✅ Expectations:
- Test that asset object initializes correctly
"""

from models.asset import Asset

def test_asset_creation():
    asset = Asset("AAPL", 150.0)
    assert asset.name == "AAPL"
    assert asset.price == 150.0