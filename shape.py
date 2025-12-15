import cv2
import numpy as np

img=np.zeros(512,512,3)

# Rectangle
cv2.rectangle(img,pt1=(100,100),pt2=(300,300),color=(0,255,0),thickness=1)    # thickness= -1 for fully filled rectangle

# Circle
cv2.circle(img,center=(100,400),radius=60,color=(0,0,255),thickness=-1)

# Line
cv2.line(img,pt1=(0,0),pt2=(512,512),color=(255,0,0),thickness=3)

# Text
cv2.putText(img,text="Hello",org=(100,100),fontFace=cv2.FONT_HERSHEY_PLAIN,fontScale=4,color=(0,255,0),thickness=2,lineType=cv2.LINE_AA)