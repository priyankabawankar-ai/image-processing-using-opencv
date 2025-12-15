import cv2
import numpy as np
import time


#  capture=cv2.VideoCapture('output.avi')  # play existing video
capture=cv2.VideoCapture(0)   # 0 is primary webcam no.
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
write=cv2.VideoWriter()

while True:
    ret, frame=capture.read()

    # video_gray=cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)

   # time.sleep(1/20)


    cv2.imshow("webcam",frame)

    out.write(frame)     # saving a video

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

    out.release()

    cv2.destroyAllWindows()
