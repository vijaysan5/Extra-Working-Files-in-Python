import cv2
import numpy as np

# 1. Read Image
img = cv2.imread("image.png")

# 2. Resize
img = cv2.resize(img, (600, 400))

# 3. Convert to Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 4. Gaussian Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# 5. Canny Edge Detection
edges = cv2.Canny(blur, 100, 200)

# 6. Threshold
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# 7. Flip
flip = cv2.flip(img, 1)

# 8. Rotate
rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# 9. Draw Rectangle
rectangle = img.copy()
cv2.rectangle(rectangle, (50, 50), (200, 200), (0, 255, 0), 2)

# 10. Draw Circle
circle = img.copy()
cv2.circle(circle, (300, 200), 60, (255, 0, 0), 2)

# 11. Draw Line
line = img.copy()
cv2.line(line, (0, 0), (600, 400), (0, 0, 255), 2)

# 12. Put Text
text = img.copy()
cv2.putText(text, "OpenCV", (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1, (255, 255, 255), 2)

# 13. Find Contours
contours, hierarchy = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# 14. Draw Contours
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 255), 2)

# 15. Display Image
cv2.imshow("Original", img)
cv2.imshow("Gray", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)
cv2.imshow("Threshold", thresh)
cv2.imshow("Flip", flip)
cv2.imshow("Rotate", rotate)
cv2.imshow("Rectangle", rectangle)
cv2.imshow("Circle", circle)
cv2.imshow("Line", line)
cv2.imshow("Text", text)
cv2.imshow("Contours", contour_img)

cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import os

# Input video path
video_path = "input.mp4"

# Output folder for frames
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

# Open video
cap = cv2.VideoCapture(video_path)

frame_count = 0

while True:
    ret, frame = cap.read()
    
    if not ret:
        break  # End of video
    
    # Save frame as image
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)
    
    frame_count += 1

cap.release()
print(f"Extracted {frame_count} frames.")