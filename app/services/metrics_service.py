from sqlalchemy.orm import Session
from app.models import Event
from sqlalchemy import func


def get_avg_dwell_per_zone(
        db: Session,
        store_id: str
):

    rows = (
        db.query(
            Event.zone_id,
            func.avg(Event.dwell_ms)
        )
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_DWELL"
        )
        .group_by(Event.zone_id)
        .all()
    )

    result = {}

    for zone, dwell in rows:
        result[zone] = round(dwell, 2)

    return result


def get_unique_visitors(
        db: Session,
        store_id: str
):
    visitors = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.is_staff == False
        )
        .distinct()
        .all()
    )

    return len(visitors)


def get_conversion_rate(
        db: Session,
        store_id: str
):

    visitors = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ENTRY"
        )
        .distinct()
        .count()
    )

    purchasers = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_VISIT"
        )
        .distinct()
        .count()
    )

    if visitors == 0:
        return 0

    return round(
        (purchasers / visitors) * 100,
        2
    )


def get_queue_depth(
        db: Session,
        store_id: str
):

    visitors = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_VISIT"
        )
        .distinct()
        .count()
    )

    return visitors


def get_abandonment_rate(
        db: Session,
        store_id: str
):

    queue_visitors = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "QUEUE_VISIT"
        )
        .distinct()
        .count()
    )

    purchasers = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "BILLING_VISIT"
        )
        .distinct()
        .count()
    )

    if queue_visitors == 0:
        return 0

    abandoned = max(
        queue_visitors - purchasers,
        0
    )

    return round(
        abandoned /
        queue_visitors *
        100,
        2
    )
