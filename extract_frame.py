import cv2 as cv 
import cv2
import os

video_path = "videos/1462_CH04_20250607210159_211703.mp4"
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_rate = 5  # mỗi 5 frame lấy 1 (tuỳ chỉnh)
count = 0
saved_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    if count % frame_rate == 0:
        filename = f"{output_dir}/frame_{saved_count:04d}.jpg"
        cv2.imwrite(filename, frame)
        saved_count += 1
    
    count += 1

cap.release()
print(f"Đã xuất {saved_count} khung hình vào {output_dir}")
