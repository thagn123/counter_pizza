from ultralytics import YOLO

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolov9m.pt")

results = model.train(
    data="mydata.yaml",
    epochs=10,
    imgsz=640,
    degrees=10,       # Xoay ±10 độ
    scale=0.5,        # Zoom ±50%
    shear=2.0,        # Nghiêng nhẹ
    flipud=0.1,       # Xác suất lật dọc
    fliplr=0.5,       # Xác suất lật ngang
    hsv_h=0.015, hsv_s=0.7, hsv_v=0.4,  # Điều chỉnh màu
    mosaic=1.0,       # Bật mosaic augmentation
    mixup=0.2,        # Bật mixup
    patience=20       # Dừng sớm nếu val không cải thiện
)
