# context.area: CONSOLE
import bpy
import json
import numpy as np

from mathutils import Vector, Euler, Matrix, Quaternion

''' TO CORRECT: Can't see this file if run script from Blender'''
# from cfg_load import cfg

bones_with_indices = {
    0: "0_NOSE",
    1: "1_LEFT_EYE_INNER",
    2: "2_LEFT_EYE",
    3: "3_LEFT_EYE_OUTER",
    4: "4_RIGHT_EYE_INNER",
    5: "5_RIGHT_EYE",
    6: "6_RIGHT_EYE_OUTER",
    7: "7_LEFT_EAR",
    8: "8_RIGHT_EAR",
    9: "9_MOUTH_LEFT",
    10: "10_MOUTH_RIGHT",
    11: "11_LEFT_SHOULDER",
    12: "12_RIGHT_SHOULDER",
    13: "13_LEFT_ELBOW",
    14: "14_RIGHT_ELBOW",
    15: "15_LEFT_WRIST",
    16: "16_RIGHT_WRIST",
    17: "17_LEFT_PINKY",
    18: "18_RIGHT_PINKY",
    19: "19_LEFT_INDEX",
    20: "20_RIGHT_INDEX",
    21: "21_LEFT_THUMB",
    22: "22_RIGHT_THUMB",
    23: "23_LEFT_HIP",
    24: "24_RIGHT_HIP",
    25: "25_LEFT_KNEE",
    26: "26_RIGHT_KNEE",
    27: "27_LEFT_ANKLE",
    28: "28_RIGHT_ANKLE",
    29: "29_LEFT_HEEL",
    30: "30_RIGHT_HEEL",
    31: "31_LEFT_FOOT_INDEX",
    32: "32_RIGHT_FOOT_INDEX"
}


''' TESTING: Methods to calculate rotation data for each landmarks '''
def Rodrigues(rotvec):
    theta = np.linalg.norm(rotvec)
    r = (rotvec/theta).reshape(3, 1) if theta > 0. else rotvec
    cost = np.cos(theta)
    mat = np.asarray([[0, -r[2], r[1]],
                      [r[2], 0, -r[0]],
                      [-r[1], r[0], 0]])
    return (cost*np.eye(3) + (1-cost)*r.dot(r.T) + np.sin(theta)*mat)

def Quaternion_my(coords):
    theta = np.pi / 4
    alpha = theta / 2

    axis = np.array(coords)
    axis = axis / np.linalg.norm(axis)

    return [np.cos(alpha), axis[0] * np.sin(alpha), axis[1] * np.sin(alpha), axis[2] * np.sin(alpha)]
''' ------------------ '''

class PoseMaker:
    def __init__(self) -> None:
        pass

        
    def landmarks_to_model_Blender(landmarks_path, frames=0):
        """
            Converts landmarks from json file into blender animated armature
            landmarks_path: path to json files
            frame: framerange
        """
        ''' TO CORRECT: Add path for keypoint in video '''
        for frame in range(frames):
            ''' TO CORRECT: Set suitable path for each .json file in keypoints path'''
            # path_to_cur_json_landmarks = frame + landmarks_path

            with open("landmarks_path", 'r') as file_obj:
                landmarks_result_dict = json.load(file_obj)
            
            model_path = 'E:\\Job\\Hobby\\diploma\\3d_pose_maker\\data\\Models\\SMPL_Human_f.fbx'

            scene = bpy.data.scenes["Scene"]
            # bpy.ops.import_scene.fbx(filepath=model_path)
            armature = bpy.data.objects["Armature"]
            bones = armature.pose.bones

            for bone_name in bones_with_indices.values():
                bones[bone_name].location = 5*Vector((landmarks_result_dict[bone_name][1],
                                                    landmarks_result_dict[bone_name][2],
                                                    landmarks_result_dict[bone_name][0]))

                bones[bone_name].keyframe_insert('location', frame=0)

        return 0


if __name__ == '__main__':
    pass
    # filename_prefix = 'singleimg'
    # landmarks_filepath = cfg['paths']['landmarks_result'] + "/singleimg/" + f'/0_{filename_prefix}_joint_coords.json'

    # with open(landmarks_filepath, 'r') as file_obj:
    #     landmarks_dict = json.load(file_obj)


