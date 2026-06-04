from sqlalchemy.orm import Session

from app.models import Event


def event_exists(db: Session, event_id: str):
    return (db.query(Event)
            .filter(Event.event_id == event_id)
            .first())


def create_event(db: Session, event):
    db_event = Event(
        event_id=event.event_id,
        store_id=event.store_id,
        camera_id=event.camera_id,
        visitor_id=event.visitor_id,
        event_type=event.event_type,
        timestamp=event.timestamp,
        zone_id=event.zone_id,
        dwell_ms=event.dwell_ms,
        is_staff=event.is_staff,
        confidence=event.confidence,
        metadata_json=event.metadata
    )

    db.add(db_event)
    db.commit()

    return db_event
