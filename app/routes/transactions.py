from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.transaction_service import (
    load_transactions
)

router = APIRouter()


@router.post("/transactions/import")
def import_transactions(
        db: Session = Depends(get_db)
):
    inserted = load_transactions(
        "data/Brigade_Bangalore.csv",
        db
    )

    return {
        "inserted": inserted
    }
