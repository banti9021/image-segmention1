import os
import cv2
import time
import uuid

# Define paths and labels
IMAGE_PATH = "collectimage"
labels = ['hello', 'yes', 'no', 'thanks', 'i love you', 'please']
number_image = 5

# Create directories for labels
for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)

# Open the camera
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    for label in labels:
        print(f"Collecting images for '{label}'")
        for imgnum in range(number_image):
            ret, frame = cap.read()
            if not ret:
                print(f"Error: Failed to capture image for '{label}'")
                continue
            imagename = os.path.join(IMAGE_PATH, label, f"{label}.{uuid.uuid1()}.jpg")
            cv2.imwrite(imagename, frame)
            time.sleep(2)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()


