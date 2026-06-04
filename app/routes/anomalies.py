from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

from app.services.anomaly_service import (
    get_anomalies
)

router = APIRouter()


@router.get(
    "/stores/{store_id}/anomalies"
)
def anomalies(
        store_id: str,
        db: Session = Depends(get_db)
):

    return get_anomalies(
        db,
        store_id
    )
