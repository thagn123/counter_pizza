from ultralytics import YOLO
import cv2

# Hàm áp dụng CLAHE
def apply_clahe(frame):
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    merged = cv2.merge((cl, a, b))
    enhanced_frame = cv2.cvtColor(merged, cv2.COLOR_LAB2BGR)
    return enhanced_frame

# Nạp mô hình YOLO
model = YOLO("runs/detect/train/weights/best.pt")

# Nạp video
video_path = r"videos\1462_CH03_20250607192844_202844.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Không mở được video, kiểm tra đường dẫn video!")
    exit()

# Tạo cửa sổ hiển thị
window_name = "YOLO + CLAHE (Cân bằng sáng)"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("✅ Hoàn thành video hoặc không đọc được frame.")
        break

    # Áp dụng CLAHE cân bằng sáng
    balanced_frame = apply_clahe(frame)

    # YOLO nhận diện
    results = model(balanced_frame, verbose=False)
    annotated_frame = results[0].plot()

    # Resize hiển thị
    h, w = annotated_frame.shape[:2]
    new_w = 800
    new_h = int(h * (new_w / w))
    resized_frame = cv2.resize(annotated_frame, (new_w, new_h), interpolation=cv2.INTER_AREA)

    cv2.imshow(window_name, resized_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
