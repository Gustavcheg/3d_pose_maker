import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from mediapipe import Image

from mediapipe import solutions
from mediapipe.framework.formats import landmark_pb2

import numpy as np
import cv2 as cv
import time
from loguru import logger

from pose_detector.utils.cfg_load import cfg
from .utils.tools import joints_to_json



class PoseDetector():
    def __init__(self) -> None:
        self.model_path = cfg['paths']['models']['mediapipe'] + '/pose_landmarker_full.task'
        self.base_options = python.BaseOptions
        self.pose_landmarker = vision.PoseLandmarker
        self.landmarker_option = vision.PoseLandmarkerOptions
        self.running_mode = vision.RunningMode
    
    @logger.catch
    def detect_pose_on_image(self, rgb_image="me_test_1.jpg", output_dir="", visualize=False):
        """ 
            Select IMAGE mode 
            rgb_image: (str) path to image file
            visualize: (bool) draw keypoints on image and show it?
        """
        logger.info("Image detection started!")

        mode = self.running_mode.IMAGE
        option = self.landmarker_option(
            base_options=self.base_options(model_asset_path=self.model_path),
            running_mode=mode
        )

        with self.pose_landmarker.create_from_options(option) as detector:
            logger.info("Running on " + rgb_image + " file.")
            # Image visualization info
            if visualize:
                logger.warning("Detecting and visualizing...")
            else:
                logger.warning('Only visualizing')
            
            img_path = cfg['paths']['media'] + rgb_image
            mp_image = Image.create_from_file(img_path)

            detection_result = detector.detect(mp_image)

            # Save keypoints (landmarks) in JSON file
            try:
                json = joints_to_json(detection_result.pose_landmarks[0])
                logger.success("Successfully save keypoints coordinates in JSON!")
            except:
                logger.exception("Error occured, see logs...")

            # Draw keypoints on image
            annotated_image = []
            if visualize:
                annotated_image = self._draw_landmarks_on_image(mp_image.numpy_view(), detection_result)

            return detection_result, annotated_image
        
    @logger.catch
    def detect_pose_on_video(self, video="001_Test.mp4", output_dir="", visualize=False):
        """ 
            Detect pose on multiple frames (video)
            video: (str) path to image video file
            visualize: (bool) draw keypoints on video and show it?
        """
        logger.info("Video detection started!")

        mode = self.running_mode.VIDEO

        # Option for VIDEO
        option = self.landmarker_option(
            base_options=self.base_options(model_asset_path=self.model_path),
            running_mode=mode
        )

        # Create PoseLandmarker task from options
        with self.pose_landmarker.create_from_options(option) as detector:
            logger.info("Running on " + video + " file.")
            # Image visualization info
            if visualize:
                logger.warning("Detecting and visualizing...")
            else:
                logger.warning('Only visualizing')

            video_path = cfg['paths']['media']
            cap = cv.VideoCapture(video_path + video)

            # FourCC byte code for video codec and path for video saving
            fourcc = cv.VideoWriter_fourcc(*"VIDX")
            out = cv.VideoWriter(video_path + "DETECTED_" + video, fourcc, 20.0, (640, 480))

            # Read video frame by frame
            while cap.isOpened():
                frame_exists, frame = cap.read()
                if not frame_exists:
                    logger.warning("Can't recieve frame. Exitting...")
                    break
                
                ''' TO CORRECT: ADD IMAGE PRE-PROCCESS '''
                # frame_gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)

                # Convert frame to mp.Image
                mp_frame = Image(image_format=mp.ImageFormat.SRGB, data=frame)
                # Detect pose on each frame
                detection_result = detector.detect_for_video(mp_frame, (int(cap.get(cv.CAP_PROP_POS_MSEC))))

                # Save keypoints(landmarks) in JSON file
                ''' TO CORRECT: First 15 frames Doesn't calculate '''
                try:
                    json = joints_to_json(detection_result=detection_result,
                                          frame_number=int(cap.get(cv.CAP_PROP_POS_FRAMES)),
                                           filename_prefix=video)
                except Exception as e:
                    if e.__class__.__name__ != "IndexError":
                        logger.exception("Error occured, see logs...")
                        break
                    else:
                        continue
                
                # Write video with keypoints
                if visualize:
                    annotated_image = self._draw_landmarks_on_image(mp_frame.numpy_view(), detection_result)
                    out.write(annotated_image)
                    cv.imshow('frame', annotated_image)
                    if cv.waitKey(1) == ord('q'):
                        logger.info("Frame recieving stopped")
                        break
                    
            cv.waitKey(0)
            cap.release()
            out.release()
            cv.destroyAllWindows()

        logger.success("Success video detection!")
        return 0
    
    def _draw_landmarks_on_image(self, rgb_image, detection_result):
        """
            Draw keypoints on image
            rgb_image: (numpy.ndarray) Input image
            detection_result: (NormalizedLandmarkList) List of detected landmarks (keypoints)
        """

        # Get landmarks (keypoints)
        pose_landmarks_list = detection_result.pose_landmarks
        annotated_image = np.copy(rgb_image)

        # Normilize and draw landmarks
        for idx in range(len(pose_landmarks_list)):
            pose_landmarks = pose_landmarks_list[idx]

            pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
            pose_landmarks_proto.landmark.extend([
                landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in pose_landmarks
            ])

            solutions.drawing_utils.draw_landmarks(
                annotated_image,
                pose_landmarks_proto,
                solutions.pose.POSE_CONNECTIONS,
                solutions.drawing_styles.get_default_pose_landmarks_style()
            )

        return annotated_image
        

    # def _write_joints_to_json(landmarks, frame_number, filename_prefix="singleimg"):
    #     joint_coords = {}
    #     for idx, landmark in enumerate(landmarks):
    #         joint_coords[f"{MP_POSE.PoseLandmark(idx).name,}"] = [idx, landmark.x, landmark.y, landmark.z]

    #     joints_coord_path = cfg['paths']['landmarks_result'] + '/{0}_joint_coords.json'.format(filename_prefix)
    #     with open(joints_coord_path, 'w') as outfile:
    #         json.dump(joint_coords, outfile, indent=4)

    # return joint_coords