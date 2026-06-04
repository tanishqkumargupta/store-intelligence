from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.services.event_service import (
    get_recent_events
)

router = APIRouter()


@router.get(
    "/stores/{store_id}/events/recent"
)
def recent_events(
        store_id: str,
        db: Session = Depends(get_db)
):

    events = get_recent_events(
        db,
        store_id
    )

    return [
        {
            "visitor_id": e.visitor_id,
            "event_type": e.event_type,
            "zone_id": e.zone_id,
            "timestamp": e.timestamp
        }
        for e in events
    ]
