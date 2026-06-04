from cameras.cam1 import process_cam1
from cameras.cam2 import process_cam2
from cameras.cam3 import process_cam3
from cameras.cam5 import process_cam5


def process_camera(
        camera_id,
        x,
        y,
        track_id
):

    if camera_id == "CAM_1":
        return process_cam1(x, y)

    elif camera_id == "CAM_2":
        return process_cam2(x, y)

    elif camera_id == "CAM_3":
        return process_cam3(track_id, x)

    elif camera_id == "CAM_5":
        return process_cam5(track_id, x, y)

    return None
