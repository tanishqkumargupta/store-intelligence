from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.heatmap_service import (
    get_heatmap
)

router = APIRouter()


@router.get(
    "/stores/{store_id}/heatmap"
)
def heatmap(
        store_id: str,
        db: Session = Depends(get_db)
):

    return get_heatmap(
        db,
        store_id
    )
