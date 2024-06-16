from pose_detector.utils.tools import show_image
from pose_detector.landmarks_point_detector import PoseDetector

from pose_detector.utils.cfg_load import cfg

from loguru import logger
import sys
from datetime import datetime

FLAGS = ['-video', '-image']
OUT_FLAGS = ['output']

if __name__ == "__main__":
    logger.add(cfg['paths']['logs'] + 'logee.log', format="{time: YYYY-MM-DD HH:mm:SS} | {level} | {message}")
    logger.info("App started!")
    poser = PoseDetector()



    if len(sys.argv) == 1:
        logger.info("Running on video test in\out data!")
        poser.detect_pose_on_video(visualize=True)
    else:
        flag_mode = sys.argv[1]
        path_from = sys.argv[2]

        # Check command line args
        if flag_mode not in FLAGS:
            logger.error("Bad commnad line args!")
        else:
            # Check running mode
            if flag_mode == "-image":
                if path_from == "":
                    # Run on test image
                    detected_result, annotated_image = poser.detect_pose_on_image(visualize=True)
                else:
                    # Run on user image
                    detected_result, annotated_image = poser.detect_pose_on_image(rgb_image=path_from, visualize=True)

                show_image(annotated_image)

            elif flag_mode == "-video":
                if path_from == "":
                    # Run on test video
                    poser.detect_pose_on_video(visualize=True)
                else:
                    # Run on user video
                    poser.detect_pose_on_video(video=path_from, visualize=True)

        

    logger.info("App stopped!")