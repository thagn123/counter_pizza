from ultralytics import YOLO



# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolov9m.pt")


results = model.train(data="mydata.yaml", epochs=3)

