from zones import get_zone_for_point

def process_cam1(
        center_x,
        center_y
):
    return get_zone_for_point(
        "cam1",
        center_x,
        center_y
    )
