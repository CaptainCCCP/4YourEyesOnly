import cv2
cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()  # 读取每一帧
    cv2.imshow('摄像头', frame)  # 显示每一帧
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
