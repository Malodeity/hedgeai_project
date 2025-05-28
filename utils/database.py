"""
📦 FILE: database.py

🎯 Units:
- Unit 8: Env-based config
- Unit 12: DB adapter pattern

✅ Expectations:
- Return a connection from SQLAlchemy engine
"""

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment")

engine = create_engine(DATABASE_URL)

def get_connection():
    """
    TODO:
    - Return engine connection for querying
    """
    return engine.connect()