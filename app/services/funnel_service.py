from sqlalchemy.orm import Session
from app.models import Event


def get_funnel_data(
        db: Session,
        store_id: str
):

    all_visitors = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id
        )
        .distinct()
        .all()
    )

    zone_visitors = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_ENTER"
        )
        .distinct()
        .all()
    )

    dwell_visitors = (
        db.query(Event.visitor_id)
        .filter(
            Event.store_id == store_id,
            Event.event_type == "ZONE_DWELL"
        )
        .distinct()
        .all()
    )

    # Placeholder until visitor-session to POS
    # correlation is implemented.
    purchase_count = 0

    return {
        "entry": len(all_visitors),
        "zone_visit": len(zone_visitors),
        "billing": len(dwell_visitors),
        "purchase": purchase_count
    }
