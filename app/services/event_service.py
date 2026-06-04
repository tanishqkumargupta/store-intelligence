from sqlalchemy.orm import Session
from app.models import Event


def get_recent_events(
        db: Session,
        store_id: str,
        limit: int = 50
):

    events = (
        db.query(Event)
        .filter(
            Event.store_id == store_id
        )
        .order_by(
            Event.timestamp.desc()
        )
        .limit(limit)
        .all()
    )

    return events
