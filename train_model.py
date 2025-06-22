from ultralytics import YOLO

def train_model():
    model = YOLO("yolov8m.pt")
    model.train(
    data="mydata.yaml",         
    epochs=200,                  
    imgsz=640,                  
    batch=32,                   
    device=0,                    
    degrees=15,                  
    translate=0.2,               
    scale=0.6,                   
    shear=2.0,                   
    flipud=0.1,                  
    fliplr=0.5,                  
    hsv_h=0.015,                 
    hsv_s=0.5,                   
    hsv_v=0.5,                   
    mosaic=0.5,                  
    mixup=0.1,                   

    optimizer='AdamW',           
    lr0=0.003,                  
    cos_lr=True,                 
    patience=30,                 
    cache=True,                  
    workers=4,                   

    project="runs/train",
    name="pizza_counter_improve"
)


if __name__ == "__main__":
    train_model()
