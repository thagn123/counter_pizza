from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train2/weights/best.pt")
video_path = r"C:\Users\daoth\Downloads\counter_pizza\counter_pizza\videos\train_pizza.mp4"
cap = cv2.VideoCapture(video_path)

# Kiểm tra mở video
if not cap.isOpened():
    print("❌ Không mở được video, kiểm tra đường dẫn video!")
    exit()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("❌ Không đọc được frame từ video.")
        break

    results = model(frame, verbose=False)
    annotated_frame = results[0].plot()

    # Thử hiển thị
    cv2.imshow("Kết quả YOLO", annotated_frame)

    # Kiểm tra cv2 window có đóng sớm không
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
