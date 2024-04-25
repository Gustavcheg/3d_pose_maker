from pose_detector.utils.tools import show_image, draw_landmarks_on_image
from pose_detector.landmarks_point_detector import PoseDetector

if __name__ == "__main__":
    poser = PoseDetector()
    detected_result, annotated_image = poser.detect_pose_on_image()
    show_image(annotated_image)