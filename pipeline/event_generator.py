import uuid
import time
from datetime import datetime
from event_sender import send_event

visitor_zones = {}
generated_events = []
visitor_enter_time = {}
seen_visitors = set()
last_zone_change = {}
MIN_ZONE_TIME = 2.0


def process_zone_change(
        track_id,
        current_zone
):
    if current_zone is None:
        return

    if track_id not in seen_visitors:
        seen_visitors.add(track_id)

    previous_zone = visitor_zones.get(track_id)

    current_time = time.time()
    last_change = last_zone_change.get(
        track_id,
        0
    )

    if (
            current_time - last_change
            < MIN_ZONE_TIME
    ):
        return

    if previous_zone == current_zone:
        return

    current_time = time.time()

    if (
        previous_zone is not None and
        track_id in visitor_enter_time
    ):

        dwell_seconds = (
            current_time -
            visitor_enter_time[track_id]
        )

        dwell_event = {
            "event_id": str(uuid.uuid4()),
            "store_id": "STORE_BLR_002",
            "camera_id": "CAM_1",
            "visitor_id": f"VIS_{track_id}",
            "event_type": "ZONE_DWELL",
            "timestamp": datetime.utcnow().isoformat(),
            "zone_id": previous_zone,
            "dwell_ms": int(dwell_seconds * 1000),
            "is_staff": False,
            "confidence": 0.90,
            "metadata": {}
        }

        generated_events.append(
            dwell_event
        )

        send_event(dwell_event)

        print(dwell_event)

    visitor_enter_time[track_id] = current_time

    enter_event = {
        "event_id": str(uuid.uuid4()),
        "store_id": "STORE_BLR_002",
        "camera_id": "CAM_1",
        "visitor_id": f"VIS_{track_id}",
        "event_type": "ZONE_ENTER",
        "timestamp": datetime.utcnow().isoformat(),
        "zone_id": current_zone,
        "dwell_ms": 0,
        "is_staff": False,
        "confidence": 0.90,
        "metadata": {}
    }

    generated_events.append(
        enter_event
    )

    send_event(
        enter_event
    )

    print(enter_event)
    last_zone_change[track_id] = current_time
    visitor_zones[track_id] = current_zone
