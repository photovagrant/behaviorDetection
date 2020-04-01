import cv2
import numpy as np
cap1=cv2.VideoCapture("rtsp://admin:admin@172.19.148.68/play1.sdp")
cap2=cv2.VideoCapture("rtsp://admin:admin@172.19.148.71/play1.sdp")
#cap3=cv2.VideoCapture("rtsp://admin:admin@172.19.148.71/play1.sdp")
cap1.set(cv2.CAP_PROP_BUFFERSIZE, 2) 
cap2.set(cv2.CAP_PROP_BUFFERSIZE, 2) 
#cap3.set(cv2.CAP_PROP_BUFFERSIZE, 2) 
ret1,frame1 = cap1.read()
ret2,frame2 = cap2.read()
#ret2,frame3 = cap3.read()
mainimage = np.zeros((1920,1080,3), np.uint8)
cv2.namedWindow("MAIN")

while ret1 and ret2 :
    ret1,frame1 = cap1.read()
    ret2,frame2 = cap2.read()
    #ret3,frame3 = cap3.read()
    if ( ret1 and ret2 ):
        scale_percent = 50
        width = int(frame1.shape[1] * scale_percent / 100)
        height = int(frame1.shape[0] * scale_percent / 100) 
        dim = (width,height)
        frame1 = cv2.resize(frame1,dim,interpolation = cv2.INTER_AREA)
        frame2 = cv2.resize(frame2,dim,interpolation = cv2.INTER_AREA)
        #frame3 = cv2.resize(frame2,dim,interpolation = cv2.INTER_AREA)
        #frame3 = cv2.resize(frame3,dim,interpolation = cv2.INTER_AREA)
        #(h,w) = frame3.shape[:2]
        #center = (w / 2, h / 2) 
        #scale = 1
        #M = cv2.getRotationMatrix2D(center, 90, scale)
        #frame3 = cv2.warpAffine(frame3, M, (h, w)) 
        #frame3 = cv2.resize(frame3,dim,interpolation = cv2.INTER_AREA)
        #frame3 = cv2.rotate(frame3, cv2.ROTATE_90_CLOCKWISE)
        #(h,w) = frame3.shape[:2]
        #print (w)
        #print (h)
        #numpy_vertical_concat = np.concatenate((frame1, frame3), axis=0)
        #numpy_vertical_concat = np.vstack((frame1, frame2))
        #w,h,result=frame3.shape
        #print ("Width:",w,"heisht:",h)
        #frame2.shape
        mainimage[0:360,0:640]=frame1
        mainimage[360:720,0:640]=frame2
        #mainimage[40:680,680:1040]=frame3
        #mainimage[720:1080,0:640]=frame3
        cv2.imshow("MAIN",mainimage)
        #cv2.imshow("MAIN",frame2)
    else:
        print("ret FAIL")
    if cv2.waitKey(12) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap1.release()
cap2.release()

