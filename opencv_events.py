import cv2
import numpy as np

img=np.zeros(512,512,3)

def draw(event,x,y,flags,params):
   if event == 1:       # 0---mouse move,1--- mouse down click, 4--- mouse up click
      cv2.circle(img,center=(x,y),radius=50,color=(0,255,0),thickness=-1)


cv2.namedWindow(winname="window")
cv2.setMouseCallback('window',draw)



while True:

    cv2.imshow("window",img)
    
    if cv2.waitKey(1) & 0xFF== ord('x'):
     break

cv2.destroyAllWindows()