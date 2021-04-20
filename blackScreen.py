import cv2
import time
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

cap = cv2.VideoCapture(0)

time.sleep(2)

vg = 0

for i in range(60):
    frame,bg = cap.read()

bg = np.flip(bg, axis = 1)

while(cap.isOpened()):
    frame,image = cap.read()
    if not frame:
        break

    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])
    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    f = frame - res
    f = np.where(f == 0, image, f)

    output_file.write(f)

    cv2.imshow("Magic!",f)
    cv2.waitKey(1)

cat.release()
out.release()
cv2.destroyAllWindows()