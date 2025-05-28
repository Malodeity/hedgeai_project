"""
📦 FILE: assets.py

🎯 Unit 12: FastAPI Modular API

✅ Expectations:
- Implement GET endpoint for listing assets
- Later: Add support for POST/PUT/DELETE (CRUD)
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/assets")
def get_assets():
    """
    TODO:
    - Retrieve assets from database or dummy source
    - Return as JSON list
    """
    return {"message": "List of assets will appear here"}