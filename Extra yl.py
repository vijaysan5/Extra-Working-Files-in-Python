
from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam (0 = Default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Cannot read frame")
        break

    # Object Detection
    results = model(frame)

    # Draw detections
    annotated_frame = results[0].plot()

    # Display webcam output
    cv2.imshow("YOLOv8 Real-Time Object Detection", annotated_frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
