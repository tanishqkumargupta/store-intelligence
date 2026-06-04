from track import track_people
import os

video_path = r"C:\Users\tkg91\PycharmProjects\store-intelligence\data\CCTV FOOTAGE\CAM 1.mp4"

print("Exists:", os.path.exists(video_path))

track_people(
    video_path, "CAM_1"
)
