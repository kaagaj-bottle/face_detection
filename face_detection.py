from mtcnn import MTCNN
import cv2
import time

def detect_faces_mtcnn(image_path):

    detector = MTCNN()

    image = cv2.imread(image_path)

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    u= time.time()
    detections = detector.detect_faces(image_rgb)
    v=time.time()
    dt_for_model =v-u

    return len(detections), dt_for_model


if __name__=="__main__":
    image_path = "data/auditcity.webp"

    len_detections, dt_for_model = detect_faces_mtcnn(image_path)

    print(f"No of faces detected: {len_detections}")
    print(f"Time required for model: {dt_for_model}")
