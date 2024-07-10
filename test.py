from ultralytics import YOLO
import cv2
import numpy as np
# Load a model
model = YOLO('./runs/detect/train120/weights/best.pt')  # load a custom model
source1 = cv2.imread("/media/ma/文件/jd/A101498/train/images/train/01_missing_hole_01.jpg")
source2 = cv2.imread("/media/ma/文件/jd/A101498/train/images/train/01_missing_hole_01.jpg")
source=np.concatenate((source1, source2), axis=2)
print(source.shape)
# Predict with the model
results = model(source)  # predict on an image
print(results)