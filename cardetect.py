# Install dependencies first:
# pip install ultralytics opencv-python

import cv2
from ultralytics import YOLO

# Load YOLO model (small, fast version)
model = YOLO("yolov8n.pt")

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO inference
    results = model(frame)

    # Draw detections on frame
    annotated_frame = results[0].plot()

    # Show the frame
    cv2.imshow("YOLO Person Detection", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
