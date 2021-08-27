import cv2
import time
import os
import module as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(3, hCam)

folderPath = "img"
myList = os.listdir(folderPath)
print("Loaded: ", myList)
overlayList = []
for imPath in myList:
    img = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(img)
print(len(overlayList))

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    print(lmList)

    if len(lmList) != 0:
        fingers = []


        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)


        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)


    cv2.imshow("Image", img)
    cv2.waitKey(1)