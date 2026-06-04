from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Event


def get_heatmap(
        db: Session,
        store_id: str
):

    rows = (
        db.query(
            Event.zone_id,
            func.count(Event.zone_id)
        )
        .filter(
            Event.store_id == store_id,
            Event.zone_id is not None
        )
        .group_by(
            Event.zone_id
        )
        .all()
    )

    result = {}

    for zone, count in rows:
        result[zone] = count

    return result
