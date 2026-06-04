import cv2
import numpy as np


BILLING_ROI = [
    (200, 150),
    (1200, 150),
    (1200, 850),
    (200, 850)
]


def process_cam5(
        track_id,
        x,
        y
):
    polygon = np.array(
        BILLING_ROI,
        dtype=np.int32
    )

    inside = cv2.pointPolygonTest(
        polygon,
        (x, y),
        False
    )

    if inside >= 0:
        return "BILLING_AREA"

    return None