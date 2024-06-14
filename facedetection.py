import cv2

face=cv2.CascadeClassifier('face.xml')

cap =cv2.VideoCapture(0)
c=0
while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,0)
    font=cv2.FONT_HERSHEY_COMPLEX_SMALL

    count=0
    detect= face.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
    for (x,y,w,h) in detect:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        count=count+1
        
        cv2.putText(frame,"Face count: "+str(count),(x-12,y-12),font,1,(100,255,255),1)
        print(count)
    
    cv2.imshow("face",frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()