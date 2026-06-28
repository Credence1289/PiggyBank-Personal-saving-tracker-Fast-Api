from fastapi import Depends, APIRouter
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.session import get_db

router = APIRouter(tags=["Health"])

@router.get("/health")
def health_check(
        db:Session = Depends(get_db)
):
    try:
        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "service": "PiggyBank",
            "database": "connected",

        }
    except Exception:
        return {
            "status": "failed",
            "database": "unavailable"
        }