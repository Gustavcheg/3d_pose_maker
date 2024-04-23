import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import Image

import numpy as np
import cv2 as cv

from utils.cfg_load import cfg
from utils.tools import show_image, draw_landmarks_on_image


class PoseDetector():
    def __init__(self) -> None:
        self.model_path = cfg['paths']['models']['mediapipe'] + '/pose_landmarker_full.task'
        self.base_options = python.BaseOptions
        self.pose_landmarker = vision.PoseLandmarker
        self.landmarker_option = vision.PoseLandmarkerOptions
        self.running_mode = vision.RunningMode

    def detect_pose_on_image(self, rgb_image=None):
        mode = self.running_mode.IMAGE
        option = self.landmarker_option(
            base_options=self.base_options(model_asset_path=self.model_path),
            running_mode=mode
        )

        with self.pose_landmarker.create_from_options(option) as detector:
            img_path = cfg['paths']['media'] + "me_test_1.jpg"
            image = Image.create_from_file(img_path)

            detection_result = detector.detect(image)

            annotated_image = draw_landmarks_on_image(image.numpy_view(), detection_result)
            return detection_result, annotated_image
        
