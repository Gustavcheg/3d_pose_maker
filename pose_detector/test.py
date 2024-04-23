import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = 'pose_landmarker_full.task'

BaseOption = mp.tasks.BaseOptions
PoseLandmarker = vision.PoseLandmarker
PoseLandmarkerOptions = vision.PoseLandmarkerOptions
VisionRunningMode = vision.RunningMode

option = PoseLandmarkerOptions(
    base_options=BaseOption(model_asset_path=model_path),
    running_mode=VisionRunningMode.VIDEO)

with PoseLandmarker.create_from_options(option) as landmarker:
    print("hello world!")