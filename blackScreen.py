import cv2  
import numpy as np  
  
# create the video object from cv2.VideoCapture
# create image from cv2.imread and pass the image ("xyz.jpeg") 
  
while True: 
  
    # use ret and frame to read video
    print(frame)
    # use cv2.resize(frame, (640, 480))  and assign it to frame var
    image = cv2.resize(image, (640, 480)) 
  
  
    u_black = np.array([104, 153, 70]) 
    l_black = np.array([30, 30, 0]) 
  
    #create the mask from cv2.inRange(frame, l_black, u_black) 

    #create the res using cv2.bitwise_and(frame, frame, mask = mask) 
  
    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
#release the video
# destroy All Windows
