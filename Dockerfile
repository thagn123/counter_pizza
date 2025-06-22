# Sử dụng Python slim làm base image
FROM python:3.8-slim

# Tạo thư mục ứng dụng
WORKDIR /app

# Sao chép tất cả vào container
COPY . /app

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
