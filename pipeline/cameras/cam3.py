visitor_positions = {}

ENTRY_LINE_X = 900


def process_cam3(
        track_id,
        center_x
):

    previous_x = visitor_positions.get(
        track_id
    )

    visitor_positions[track_id] = center_x

    if previous_x is None:
        return None

    # Right -> Left
    if (
        previous_x > ENTRY_LINE_X
        and
        center_x < ENTRY_LINE_X
    ):
        return "ENTRY"

    # Left -> Right
    if (
        previous_x < ENTRY_LINE_X
        and
        center_x > ENTRY_LINE_X
    ):
        return "EXIT"

    return None
