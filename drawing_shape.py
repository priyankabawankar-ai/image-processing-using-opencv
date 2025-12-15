import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), dtype=np.uint8)

drawing = False
ix, iy = -1, -1

def draw(event, x, y, flags, param):
    global ix, iy, drawing, img

    # Left mouse button down
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    # Mouse move
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            temp_img = img.copy()
            cv2.rectangle(temp_img, (ix, iy), (x, y), (0, 255, 255), -1)
            cv2.imshow("window", temp_img)

    # Left mouse button up
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 255), -1)

cv2.namedWindow("window")
cv2.setMouseCallback("window", draw)

while True:
    cv2.imshow("window", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cv2.destroyAllWindows()
