"""
📦 FILE: asset.py

🎯 Unit 6: OOP
- Define a base class for financial assets
- Use inheritance for specialized asset types

✅ Expectations:
- Define fields, methods, and __str__ override
"""

class Asset:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f"{self.name}: ${self.price}"

    # TODO: Add a method to update the asset price
    # def update_price(self, new_price: float) -> None:
    #     pass