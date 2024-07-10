from ultralytics import YOLO
model = YOLO('./ultralytics/cfg/models/v8/yolov8m-train.yaml').load('yolov8m.pt')  # build from YAML and transfer weights
# Train the model
results = model.train(data='duoguang.yaml', epochs=300, imgsz=1280,device='0',batch=-1)