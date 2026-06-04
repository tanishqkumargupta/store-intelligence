from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.metrics_service import (
    get_unique_visitors,
    get_avg_dwell_per_zone,
    get_conversion_rate,
    get_queue_depth,
    get_abandonment_rate
)

router = APIRouter()


@router.get("/stores/{store_id}/metrics")
def get_metrics(
        store_id: str,
        db: Session = Depends(get_db)
):
    conversion_rate = get_conversion_rate(
        db,
        store_id
    )

    queue_depth = get_queue_depth(
        db,
        store_id
    )

    abandonment_rate = get_abandonment_rate(
        db,
        store_id
    )

    unique_visitors = get_unique_visitors(
        db,
        store_id
    )

    avg_dwell = get_avg_dwell_per_zone(
        db,
        store_id
    )

    return {
        "store_id": store_id,
        "unique_visitors": unique_visitors,
        "avg_dwell_per_zone": avg_dwell,
        "conversion_rate": conversion_rate,
        "queue_depth": queue_depth,
        "abandonment_rate": abandonment_rate
    }
