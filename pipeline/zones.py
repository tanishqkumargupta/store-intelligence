import cv2
import numpy as np


def get_zone_for_point(
    camera_name,
    x,
    y
):
    ZONE_MAP = {
        "CAM1": CAM1_ZONES,
    }
    zones = ZONE_MAP.get(camera_name)

    if zones is None:
        return None

    for zone_name, points in zones.items():

        polygon = np.array(
            points,
            dtype=np.int32
        )

        inside = cv2.pointPolygonTest(
            polygon,
            (x, y),
            False
        )

        if inside >= 0:
            return zone_name

    return None


def draw_zones(frame):

    for zone_name, points in CAM1_ZONES.items():

        pts = np.array(
            points,
            np.int32
        )

        cv2.polylines(
            frame,
            [pts],
            True,
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            zone_name,
            points[0],
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

    return frame


CAM1_ZONES = {

    "BACK_WALL": [
        (50, 120),
        (1800, 120),
        (1800, 580),
        (50, 580)
    ],

    "PROMO_ISLAND": [
        (650, 650),
        (1150, 650),
        (1150, 1080),
        (650, 1080)
    ],

    "MAKEUP_TABLE": [
        (1200, 520),
        (1650, 520),
        (1650, 980),
        (1200, 980)
    ],

    "IQ_COUNTER": [
        (1650, 650),
        (1920, 650),
        (1920, 1080),
        (1650, 1080)
    ]
}
