from ultralytics import YOLO
import cv2


def detect_people(video_path):

    cap = cv2.VideoCapture(video_path)

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model(
            frame,
            classes=[0],
            conf=0.35,
            verbose=False
        )

        for result in results:

            for box in result.boxes:

                cls = int(box.cls[0])

                if cls == 0:      # person

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        (0, 255, 0),
                        2
                    )

        display = cv2.resize(
            frame,
            (1280, 720)
        )

        cv2.imshow(
            "Detection",
            display
        )

        if cv2.waitKey(1) == 27:
            break

    cap.release()

    cv2.destroyAllWindows()


model = YOLO("yolov8n.pt")
