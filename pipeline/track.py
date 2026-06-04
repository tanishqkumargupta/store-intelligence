import cv2
import supervision as sv
from ultralytics import YOLO
from camera_logic import process_camera
from event_generator import (
    process_zone_change
)
from zones import (
    draw_zones,
)

model = YOLO("yolov8n.pt")

tracker = sv.ByteTrack(
    track_activation_threshold=0.25,
    minimum_matching_threshold=0.7,
    lost_track_buffer=90
)


def track_people(
        video_path,
        camera_id
):
    print("Starting track_people")

    cap = cv2.VideoCapture(video_path)
    print("Video opened:", cap.isOpened())

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model(
            frame,
            classes=[0],
            conf=0.35,
            verbose=False
        )[0]

        detections = sv.Detections.from_ultralytics(
            results
        )

        detections = tracker.update_with_detections(
            detections
        )

        frame_height, frame_width = frame.shape[:2]

        for i in range(len(detections)):
            x1, y1, x2, y2 = map(
                int,
                detections.xyxy[i]
            )

            track_id = int(
                detections.tracker_id[i]
            )

            confidence = detections.confidence[i]

            if confidence < 0.35:
                continue

            # Person center point
            foot_x = (x1 + x2) // 2
            foot_y = y2
            width = x2 - x1
            height = y2 - y1

            if width < 60 or height < 120:
                continue

            if (
                    foot_x < 20 or
                    foot_y < 20 or
                    foot_x > frame_width - 20 or
                    foot_y > frame_height - 20
            ):
                continue
            zone = process_camera(
                camera_id,
                foot_x,
                foot_y,
                track_id
            )

            process_zone_change(
                track_id,
                zone
            )

            cv2.circle(
                frame,
                (foot_x, foot_y), 5,
                (0, 0, 255),
                -1
            )

            cv2.putText(
                frame,
                f"ID {track_id} | {zone}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        frame = draw_zones(frame)

        display = cv2.resize(
            frame,
            (1280, 720)
        )

        cv2.imshow(
            "Tracking",
            display
        )

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
