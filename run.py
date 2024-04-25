from pose_detector.utils.tools import show_image
from pose_detector.landmarks_point_detector import PoseDetector

from pose_detector.utils.cfg_load import cfg

from loguru import logger
import sys
from datetime import datetime

if __name__ == "__main__":
    logger.add(cfg['paths']['logs'] + 'logee.log', format="{time: YYYY-MM-DD HH:mm:SS} | {level} | {message}")
    logger.info("App started!")
    poser = PoseDetector()
    # detected_result, annotated_image = poser.detect_pose_on_image(visualize=True)
    # show_image(annotated_image)

    poser.detect_pose_on_video(visualize=True)

    logger.info("App stopped!")