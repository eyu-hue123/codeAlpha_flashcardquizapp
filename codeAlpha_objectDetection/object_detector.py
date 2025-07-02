import cv2

# Load pre-trained MobileNet SSD model
net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt",
                                "MobileNetSSD_deploy.caffemodel")

# Class labels MobileNet SSD was trained to detect
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant",
           "sheep", "sofa", "train", "tvmonitor"]

# Load input image
image = cv2.imread("example.jpg")
(h, w) = image.shape[:2]

# Preprocess image for model
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843,
                             (300, 300), 127.5)
net.setInput(blob)
detections = net.forward()

# Loop over all detected objects
for i in range(detections.shape[2]):
    confidence = detections[0, 0, i, 2]
    if confidence > 0.4:  # Show only high-confidence detections
        idx = int(detections[0, 0, i, 1])
        label = CLASSES[idx]
        box = detections[0, 0, i, 3:7] * [w, h, w, h]
        (startX, startY, endX, endY) = box.astype("int")

        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
        cv2.putText(image, label, (startX, startY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Save and show output
cv2.imwrite("output.jpg", image)
print("✅ Object detection complete. Output saved as 'output.jpg'")