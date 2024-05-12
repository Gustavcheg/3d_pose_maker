import cv2 as cv
import numpy as np
from mediapipe import solutions
from mediapipe.framework.formats import body_rig_pb2, landmark_pb2

import os
import json

from .cfg_load import cfg

MP_POSE = solutions.pose


def video_to_frames():
    '''
        IN PROGRESS
    '''

    return 0

def show_image(image, title="42"):
    ''''
        Show image
    '''

    cv.imshow(title, image)
    cv.waitKey(0)


def img_preproccess(image="me_test_1.jpg"):
    '''
        IN PROGRESS
    '''
    
    img_path = cfg['paths']['media'] + image

    return 0

 
def joints_to_json(landmarks, frame_number=0, filename_prefix="singleimg"):
    '''
        Save landmarks in json 
            landmarks: predicted and estimated pose landmarks
            frame_number: number of image frame
            filename_prefix: resulting  name 
    '''

    pose_landmarks_proto = landmark_pb2.NormalizedLandmarkList()
    pose_landmarks_proto.landmark.extend([
        landmark_pb2.NormalizedLandmark(x=landmark.x, y=landmark.y, z=landmark.z) for landmark in landmarks
    ])

    joint_coords = {}
    for idx, landmark in enumerate(landmarks):
        joint_coords[f"{idx}_" + f"{MP_POSE.PoseLandmark(idx).name}"] = [landmark.x, landmark.y, landmark.z]

    # Create folder for json_keypoints
    try:
        os.mkdir(cfg['paths']['landmarks_result'] + f"/{filename_prefix}/")
    except Exception as e:
        pass
    
    #  Define the path of the json file
    joints_coord_path = cfg['paths']['landmarks_result'] + f"/{filename_prefix}/" + f'{frame_number}_{filename_prefix}_joint_coords.json'
    with open(joints_coord_path, 'w') as outfile:
        json.dump(joint_coords, outfile, indent=4)

    # return dict of landmark_name: x, y, z, ...
    return joint_coords

if __name__ == "__main__":
    print(os.path.dirname(os.path.realpath(__file__)))
