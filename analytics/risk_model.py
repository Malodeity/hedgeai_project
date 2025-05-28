"""
📦 FILE: risk_model.py

🎯 Units:
- Unit 6: OOP
- Unit 12: Strategy Pattern

✅ Expectations:
- Build risk model framework with subclasses for different methods
"""

from abc import ABC, abstractmethod
from models.portfolio import Portfolio

class RiskModel(ABC):
    @abstractmethod
    def calculate(self, portfolio: Portfolio) -> float:
        pass

# TODO: Create subclasses like:
# class VolatilityRiskModel(RiskModel): ...
# class SharpeRatioModel(RiskModel): ...