# counter_pizza
Lấy video từ link gg drive: https://drive.google.com/drive/folders/19QSILvBetBvcXyHjR85DahatiHOQSp_A
Chạy file
##extract_frame.py
Để lấy các khung hình huấn luyện.
các khung hình sẽ được ghi đè trong file frames
tiếp tục lấy các frame, sử dụng Label studio để gán nhãn và các bounding_boxs cho các đối tượng
Sử dụng yoloV9 huấn luyện trên tập dữ liệu cá nhân nhằm nhận diện cụ thể chính xác với bối cảnh

##file mydata.yaml:
phần "path" dán đường dẫn thích hợp của folder datasets, tùy theo vị trí tệp của bạn
