from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.funnel_service import get_funnel_data

router = APIRouter()


@router.get("/stores/{store_id}/funnel")
def get_funnel(
        store_id: str,
        db: Session = Depends(get_db)
):
    return get_funnel_data(
        db,
        store_id
    )
