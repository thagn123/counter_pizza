import cv2
from ultralytics import YOLO
from norfair import Detection, Tracker
import numpy as np

model = YOLO(r"runs\\train\\pizza_counter_improve\\weights\\best.pt")
tracker_pizza = Tracker(distance_function="euclidean", distance_threshold=30)
tracker_box = Tracker(distance_function="euclidean", distance_threshold=30)

cap = cv2.VideoCapture(r"videos\\0621.mp4")

count = 0
counted_pairs = set()

class_names = ['box', 'knifes', 'person', 'pizza', 'table']

def get_center(box):
    x1, y1, x2, y2 = box
    return np.array([(x1 + x2)/2, (y1 + y2)/2])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    plotted_frame = results[0].plot()

    detections_pizza = []
    detections_box = []

    for det in results[0].boxes:
        cls = int(det.cls.cpu().numpy())
        conf = float(det.conf.cpu().numpy())
        box = det.xyxy[0].cpu().numpy()
        if conf < 0.3:
            continue
        label = class_names[cls] if cls < len(class_names) else str(cls)
        center = get_center(box)
        if label == 'pizza':
            detections_pizza.append(Detection(points=center))
        elif label == 'box':
            detections_box.append(Detection(points=center))

    tracked_pizzas = tracker_pizza.update(detections=detections_pizza)
    tracked_boxes = tracker_box.update(detections=detections_box)

    for tp in tracked_pizzas:
        pid = tp.id
        pc = tp.estimate[0]
        cv2.circle(plotted_frame, (int(pc[0]), int(pc[1])), 5, (0, 0, 255), -1)
        cv2.putText(plotted_frame, f"P:{pid}", (int(pc[0]), int(pc[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

        for tb in tracked_boxes:
            bid = tb.id
            bc = tb.estimate[0]
            distance = np.linalg.norm(pc - bc)
            cv2.putText(plotted_frame, f"B:{bid}", (int(bc[0]), int(bc[1])-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
            cv2.line(plotted_frame, (int(pc[0]), int(pc[1])), (int(bc[0]), int(bc[1])), (0,255,255), 2)

            print(f"Distance P:{pid} - B:{bid} = {distance:.2f}")

            if (pid, bid) not in counted_pairs and distance < 60:
                count += 1
                counted_pairs.add((pid, bid))
                print(f"Pizza đếm: {count}, P:{pid}, B:{bid}, Distance={distance:.2f}")

    cv2.putText(plotted_frame, f"Pizza trong hop: {count}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Pizza + Box Distance Counter", plotted_frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()