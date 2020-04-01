import cv2
import numpy as np
cap1=cv2.VideoCapture("rtsp://admin:admin@172.19.148.68/play1.sdp")
cap2=cv2.VideoCapture("rtsp://admin:admin@172.19.148.128/play1.sdp")
 
ret1,frame1 = cap1.read()
ret2,frame2 = cap2.read()
ret2,frame3 = cap2.read()
mainimage = np.zeros((1280,720,3), np.uint8)
while ret1 and ret2 :
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()
    scale_percent = 50
    width = int(frame1.shape[1] * scale_percent / 100)
    height = int(frame1.shape[0] * scale_percent / 100) 
    dim = (width,height)
    frame1 = cv2.resize(frame1,dim,interpolation = cv2.INTER_AREA)
    frame2 = cv2.resize(frame2,dim,interpolation = cv2.INTER_AREA)
    #frame3 = cv2.resize(frame3,dim,interpolation = cv2.INTER_AREA)
    #(h,w) = frame3.shape[:2]
    #center = (w / 2, h / 2) 
    #scale = 1
    #M = cv2.getRotationMatrix2D(center, 90, scale)
    #frame3 = cv2.warpAffine(frame3, M, (h, w)) 
    #frame3 = cv2.resize(frame3,dim,interpolation = cv2.INTER_AREA)
    #numpy_vertical_concat = np.concatenate((frame1, frame3), axis=0)
    numpy_vertical_concat = np.vstack((frame1, frame2))
    cv2.imshow("frame",numpy_vertical_concat)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap1.release()
cap2.release()

