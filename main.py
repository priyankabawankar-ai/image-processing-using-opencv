import cv2
import numpy as np

# Reading image

image=cv2.imread("img/fruits.png")

cv2.imshow("window",image)

cv2.waitKey(0)

# convert RGB to Grayscale
image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


cv2.imshow("window",image_gray)

cv2.waitKey(0)

# Hstack(Horizonal Stack)

imgBlue=image[:,:,0]
imgGreen=image[:,:,1]
imgRed=image[:,:,2]

new_img=np.hstack(imgBlue,imgGreen,imgRed)


cv2.imshow("window",new_img)

cv2.waitKey(0)

# Resize an image
img_resize=cv2.resize(image,(256,256))

img_resize=cv2.resize(image,image.shape[1]//2,image.shape[0]//2)  # for resizing image to half

cv2.imshow("window",img_resize)

cv2.waitKey(0)

# Flipping an image

img_flip=cv2.flip(image,0)  # 0--vertical flip, 1--horizontal flip, -1--both horizontal and vertical

# Cropping an image

img_crop=image[100:300,200:500]

cv2.imshow("window",img_crop)

cv2.waitKey(0)
# Saving an image

cv2.imwrite("fruits_small.png",img_crop)


cv2.imshow("window",img_crop)

cv2.waitKey(0)