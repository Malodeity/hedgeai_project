"""
📦 FILE: portfolio.py

🎯 Units:
- Unit 6: OOP
- Unit 10: Algorithms & Data Structures

✅ Expectations:
- Aggregate assets
- Compute portfolio total value
"""

from typing import List
from models.asset import Asset

class Portfolio:
    def __init__(self, assets: List[Asset]) -> None:
        self.assets = assets

    def total_value(self) -> float:
        return sum(asset.price for asset in self.assets)

    # TODO: Add methods to add/remove assets
   