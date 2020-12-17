# importing libraries
import cv2
import pyautogui as pag
import numpy as np

# changing these parameters will affect the triggers,
# more MAGNITUDE, more SWIFT movement of hand
Y_DOWN_DIFF = 20
Y_UP_DIFF = -20

# selecting the webcam
# 0 traditionally, 1 if 0 is not working for you
capture = cv2.VideoCapture(0)

# selecting the yellow color range for detecting in the video
yellowLower = np.array([22, 93, 0])
yellowUpper = np.array([45, 255, 255])

# for storing the previous location of the image
prev_y = 0

# for streaming webcam
while True:
    ret, frame = capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, yellowLower, yellowUpper)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for item in contours:
        area = cv2.contourArea(item)
        # checking only if area is bigger than 300 units, to remove noise
        if area > 300:
            x, y, w, h = cv2.boundingRect(item)
            # cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            if (y - prev_y) > Y_DOWN_DIFF:
                pag.press('pagedown')
                print('pressing pageDown key')

            if (y - prev_y) < Y_UP_DIFF:
                pag.press('pageup')
                print('pressing pageUp key')

            # setting up current location to previous location
            prev_y = y
    
    # display the webcam frame
    cv2.imshow('frame', frame)

    # display the masked frame
    cv2.imshow('mask', mask)

    # exit the stream
    if cv2.waitKey(10) == ord('q'):
        break

# release the webcam
capture.release()
# destroy all the windows
cv2.destroyAllWindows()