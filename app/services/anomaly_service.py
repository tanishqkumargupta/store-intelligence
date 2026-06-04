from app.services.metrics_service import (
    get_unique_visitors,
    get_avg_dwell_per_zone
)


def get_anomalies(
        db,
        store_id
):

    anomalies = []

    visitors = get_unique_visitors(
        db,
        store_id
    )

    if visitors == 0:

        anomalies.append({
            "type": "LOW_TRAFFIC",
            "message": "No visitors detected"
        })

    dwell_data = get_avg_dwell_per_zone(
        db,
        store_id
    )

    for zone, dwell in dwell_data.items():

        if dwell > 20000:

            anomalies.append({
                "type": "HIGH_DWELL",
                "zone": zone,
                "value_ms": dwell,
                "message": (
                    f"Visitors spending "
                    f"too long in {zone}"
                )
            })

    return anomalies
