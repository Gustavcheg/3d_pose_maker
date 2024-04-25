import cv2 as cv
import numpy as np

import os
import json

from .cfg_load import cfg

def video_to_frames():


    return 0

def show_image(image, title="42"):
    cv.imshow(title, image)
    cv.waitKey(0)


def img_preproccess(image="me_test_1.jpg"):
    img_path = cfg['paths']['media'] + image

    return 0

# Parse Json from detected landmarks
def joints_to_json(detection_result, filename_prefix="singleimg"):
    joint_coord = {}

    joint_coord['00_nose'] = {}
    joint_coord['00_nose']["x"] = detection_result.pose_world_landmarks[0][0].x
    joint_coord['00_nose']["y"] = detection_result.pose_world_landmarks[0][0].y
    joint_coord['00_nose']["z"] = detection_result.pose_world_landmarks[0][0].z

    joint_coord['01_l_eye'] = {}
    joint_coord['01_l_eye']["x"] = detection_result.pose_world_landmarks[0][1].x
    joint_coord['01_l_eye']["y"] = detection_result.pose_world_landmarks[0][1].y
    joint_coord['01_l_eye']["z"] = detection_result.pose_world_landmarks[0][1].z

    joint_coord['02_l_eye'] = {}
    joint_coord['02_l_eye']["x"] = detection_result.pose_world_landmarks[0][2].x
    joint_coord['02_l_eye']["y"] = detection_result.pose_world_landmarks[0][2].y
    joint_coord['02_l_eye']["z"] = detection_result.pose_world_landmarks[0][2].z

    joint_coord['03_l_eye'] = {}
    joint_coord['03_l_eye']["x"] = detection_result.pose_world_landmarks[0][3].x
    joint_coord['03_l_eye']["y"] = detection_result.pose_world_landmarks[0][3].y
    joint_coord['03_l_eye']["z"] = detection_result.pose_world_landmarks[0][3].z

    joint_coord['04_r_eye'] = {}
    joint_coord['04_r_eye']["x"] = detection_result.pose_world_landmarks[0][4].x
    joint_coord['04_r_eye']["y"] = detection_result.pose_world_landmarks[0][4].y
    joint_coord['04_r_eye']["z"] = detection_result.pose_world_landmarks[0][4].z

    joint_coord['05_r_eye'] = {}
    joint_coord['05_r_eye']["x"] = detection_result.pose_world_landmarks[0][5].x
    joint_coord['05_r_eye']["y"] = detection_result.pose_world_landmarks[0][5].y
    joint_coord['05_r_eye']["z"] = detection_result.pose_world_landmarks[0][5].z

    joint_coord['06_r_eye'] = {}
    joint_coord['06_r_eye']["x"] = detection_result.pose_world_landmarks[0][6].x
    joint_coord['06_r_eye']["y"] = detection_result.pose_world_landmarks[0][6].y
    joint_coord['06_r_eye']["z"] = detection_result.pose_world_landmarks[0][6].z

    joint_coord['07_l_ear'] = {}
    joint_coord['07_l_ear']["x"] = detection_result.pose_world_landmarks[0][7].x
    joint_coord['07_l_ear']["y"] = detection_result.pose_world_landmarks[0][7].y
    joint_coord['07_l_ear']["z"] = detection_result.pose_world_landmarks[0][7].z

    joint_coord['08_r_ear'] = {}
    joint_coord['08_r_ear']["x"] = detection_result.pose_world_landmarks[0][8].x
    joint_coord['08_r_ear']["y"] = detection_result.pose_world_landmarks[0][8].y
    joint_coord['08_r_ear']["z"] = detection_result.pose_world_landmarks[0][8].z

    joint_coord['09_l_mouth'] = {}
    joint_coord['09_l_mouth']["x"] = detection_result.pose_world_landmarks[0][9].x
    joint_coord['09_l_mouth']["y"] = detection_result.pose_world_landmarks[0][9].y
    joint_coord['09_l_mouth']["z"] = detection_result.pose_world_landmarks[0][9].z

    joint_coord['10_r_mouth'] = {}
    joint_coord['10_r_mouth']["x"] = detection_result.pose_world_landmarks[0][10].x
    joint_coord['10_r_mouth']["y"] = detection_result.pose_world_landmarks[0][10].y
    joint_coord['10_r_mouth']["z"] = detection_result.pose_world_landmarks[0][10].z

    joint_coord['11_l_shoulder'] = {}
    joint_coord['11_l_shoulder']["x"] = detection_result.pose_world_landmarks[0][11].x
    joint_coord['11_l_shoulder']["y"] = detection_result.pose_world_landmarks[0][11].y
    joint_coord['11_l_shoulder']["z"] = detection_result.pose_world_landmarks[0][11].z

    joint_coord['12_r_shoulder'] = {}
    joint_coord['12_r_shoulder']["x"] = detection_result.pose_world_landmarks[0][12].x
    joint_coord['12_r_shoulder']["y"] = detection_result.pose_world_landmarks[0][12].y
    joint_coord['12_r_shoulder']["z"] = detection_result.pose_world_landmarks[0][12].z

    joint_coord['13_l_elbow'] = {}
    joint_coord['13_l_elbow']["x"] = detection_result.pose_world_landmarks[0][13].x
    joint_coord['13_l_elbow']["y"] = detection_result.pose_world_landmarks[0][13].y
    joint_coord['13_l_elbow']["z"] = detection_result.pose_world_landmarks[0][13].z

    joint_coord['14_r_elbow'] = {}
    joint_coord['14_r_elbow']["x"] = detection_result.pose_world_landmarks[0][14].x
    joint_coord['14_r_elbow']["y"] = detection_result.pose_world_landmarks[0][14].y
    joint_coord['14_r_elbow']["z"] = detection_result.pose_world_landmarks[0][14].z

    joint_coord['15_l_wrist'] = {}
    joint_coord['15_l_wrist']["x"] = detection_result.pose_world_landmarks[0][15].x
    joint_coord['15_l_wrist']["y"] = detection_result.pose_world_landmarks[0][15].y
    joint_coord['15_l_wrist']["z"] = detection_result.pose_world_landmarks[0][15].z

    joint_coord['16_r_wrist'] = {}
    joint_coord['16_r_wrist']["x"] = detection_result.pose_world_landmarks[0][16].x
    joint_coord['16_r_wrist']["y"] = detection_result.pose_world_landmarks[0][16].y
    joint_coord['16_r_wrist']["z"] = detection_result.pose_world_landmarks[0][16].z

    joint_coord['17_l_downpalm'] = {}
    joint_coord['17_l_downpalm']["x"] = detection_result.pose_world_landmarks[0][17].x
    joint_coord['17_l_downpalm']["y"] = detection_result.pose_world_landmarks[0][17].y
    joint_coord['17_l_downpalm']["z"] = detection_result.pose_world_landmarks[0][17].z

    joint_coord['18_r_downpalm'] = {}
    joint_coord['18_r_downpalm']["x"] = detection_result.pose_world_landmarks[0][18].x
    joint_coord['18_r_downpalm']["y"] = detection_result.pose_world_landmarks[0][18].y
    joint_coord['18_r_downpalm']["z"] = detection_result.pose_world_landmarks[0][18].z

    joint_coord['19_l_uppalm'] = {}
    joint_coord['19_l_uppalm']["x"] = detection_result.pose_world_landmarks[0][19].x
    joint_coord['19_l_uppalm']["y"] = detection_result.pose_world_landmarks[0][19].y
    joint_coord['19_l_uppalm']["z"] = detection_result.pose_world_landmarks[0][19].z

    joint_coord['20_r_uppalm'] = {}
    joint_coord['20_r_uppalm']["x"] = detection_result.pose_world_landmarks[0][20].x
    joint_coord['20_r_uppalm']["y"] = detection_result.pose_world_landmarks[0][20].y
    joint_coord['20_r_uppalm']["z"] = detection_result.pose_world_landmarks[0][20].z

    joint_coord['21_l_thumb'] = {}
    joint_coord['21_l_thumb']["x"] = detection_result.pose_world_landmarks[0][21].x
    joint_coord['21_l_thumb']["y"] = detection_result.pose_world_landmarks[0][21].y
    joint_coord['21_l_thumb']["z"] = detection_result.pose_world_landmarks[0][21].z

    joint_coord['22_r_thumb'] = {}
    joint_coord['22_r_thumb']["x"] = detection_result.pose_world_landmarks[0][22].x
    joint_coord['22_r_thumb']["y"] = detection_result.pose_world_landmarks[0][22].y
    joint_coord['22_r_thumb']["z"] = detection_result.pose_world_landmarks[0][22].z

    joint_coord['23_l_pelvis'] = {}
    joint_coord['23_l_pelvis']["x"] = detection_result.pose_world_landmarks[0][23].x
    joint_coord['23_l_pelvis']["y"] = detection_result.pose_world_landmarks[0][23].y
    joint_coord['23_l_pelvis']["z"] = detection_result.pose_world_landmarks[0][23].z

    joint_coord['24_r_pelvis'] = {}
    joint_coord['24_r_pelvis']["x"] = detection_result.pose_world_landmarks[0][24].x
    joint_coord['24_r_pelvis']["y"] = detection_result.pose_world_landmarks[0][24].y
    joint_coord['24_r_pelvis']["z"] = detection_result.pose_world_landmarks[0][24].z

    joint_coord['25_l_knee'] = {}
    joint_coord['25_l_knee']["x"] = detection_result.pose_world_landmarks[0][25].x
    joint_coord['25_l_knee']["y"] = detection_result.pose_world_landmarks[0][25].y
    joint_coord['25_l_knee']["z"] = detection_result.pose_world_landmarks[0][25].z

    joint_coord['26_r_knee'] = {}
    joint_coord['26_r_knee']["x"] = detection_result.pose_world_landmarks[0][26].x
    joint_coord['26_r_knee']["y"] = detection_result.pose_world_landmarks[0][26].y
    joint_coord['26_r_knee']["z"] = detection_result.pose_world_landmarks[0][26].z

    joint_coord['27_l_ankle'] = {}
    joint_coord['27_l_ankle']["x"] = detection_result.pose_world_landmarks[0][27].x
    joint_coord['27_l_ankle']["y"] = detection_result.pose_world_landmarks[0][27].y
    joint_coord['27_l_ankle']["z"] = detection_result.pose_world_landmarks[0][27].z

    joint_coord['28_r_ankle'] = {}
    joint_coord['28_r_ankle']["x"] = detection_result.pose_world_landmarks[0][28].x
    joint_coord['28_r_ankle']["y"] = detection_result.pose_world_landmarks[0][28].y
    joint_coord['28_r_ankle']["z"] = detection_result.pose_world_landmarks[0][28].z

    joint_coord['29_l_heel'] = {}
    joint_coord['29_l_heel']["x"] = detection_result.pose_world_landmarks[0][29].x
    joint_coord['29_l_heel']["y"] = detection_result.pose_world_landmarks[0][29].y
    joint_coord['29_l_heel']["z"] = detection_result.pose_world_landmarks[0][29].z

    joint_coord['30_r_heel'] = {}
    joint_coord['30_r_heel']["x"] = detection_result.pose_world_landmarks[0][30].x
    joint_coord['30_r_heel']["y"] = detection_result.pose_world_landmarks[0][30].y
    joint_coord['30_r_heel']["z"] = detection_result.pose_world_landmarks[0][30].z

    joint_coord['31_l_toe'] = {}
    joint_coord['31_l_toe']["x"] = detection_result.pose_world_landmarks[0][31].x
    joint_coord['31_l_toe']["y"] = detection_result.pose_world_landmarks[0][31].y
    joint_coord['31_l_toe']["z"] = detection_result.pose_world_landmarks[0][31].z

    joint_coord['32_r_toe'] = {}
    joint_coord['32_r_toe']["x"] = detection_result.pose_world_landmarks[0][32].x
    joint_coord['32_r_toe']["y"] = detection_result.pose_world_landmarks[0][32].y
    joint_coord['32_r_toe']["z"] = detection_result.pose_world_landmarks[0][32].z

    joints_coord_path = cfg['paths']['landmarks_result'] + '/{0}_joint_coords.json'.format(filename_prefix)
    with open(joints_coord_path, 'w') as outfile:
        json.dump(joint_coord, outfile, indent=4)

    return joint_coord

if __name__ == "__main__":
    print(os.path.dirname(os.path.realpath(__file__)))
