# counter_pizza
Lấy video từ link gg drive: https://drive.google.com/drive/folders/19QSILvBetBvcXyHjR85DahatiHOQSp_A
- Chạy file
```
python extract_frame.py
```
- Để lấy các khung hình huấn luyện.
các khung hình sẽ được ghi đè trong file frames
tiếp tục lấy các frame, sử dụng Label studio để gán nhãn và các bounding_boxs cho các đối tượng
- Sử dụng yoloV9 huấn luyện trên tập dữ liệu cá nhân nhằm nhận diện cụ thể chính xác với bối cảnh

## file mydata.yaml:
- phần "path" dán đường dẫn thích hợp của folder datasets, tùy theo vị trí tệp của bạn

## Logic đếm số lượng pizza
- sẽ là: đếm số lượng pizza đã được cho vào hộp và đưa đến tay của khách hàng
tuy nhiên, trong video sẽ có nhiều bối cảnh khác nhau và việc train mô hình theo dõi đối tượng yêu cầu nhiều tài nghuyên hơn nên chúng ta sẽ chỉ đếm số lượng pizza đã được cho vào hộp ( với thực phẩm như pizza việc cho vào hộp đồng nghĩa đã có hoàn thiện đơn hàng, gần như chắc chắn đơn hàng sẽ được giao đến tay khác hàng)

* Logic đếm pizza
### Nguyên tắc:
- Pizza được tính là hoàn tất khi được cho vào hộp.
- Tâm của bounding box pizza và box gần nhau → được xem là một lần "cho vào hộp".
### Cụ thể:
- Xác định tâm của mỗi bounding box.
- Nếu khoảng cách giữa tâm pizza và box < 80 px → đếm +1.
- Tránh đếm trùng bằng cách kiểm tra khoảng cách giữa các pizza đã đếm trước đó.

### 📌 Lưu ý
- Việc đếm này dựa trên giả định rằng: khi pizza được đóng hộp, đơn hàng đã hoàn thiện.
- Không sử dụng tracking để đơn giản hóa quá trình xử lý video.

