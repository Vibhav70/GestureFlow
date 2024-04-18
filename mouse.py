import cv2
import numpy as np
import handtrackinmodule as htm
import time 
import mouse
import pyautogui
import pydirectinput

def mouse():
    wCam , hCam = 640, 480
    frameR = 150
    smoothening = 7

    pTime = 0
    plocX, plocY = 0,0
    clocX, clocY = 0,0

    cap = cv2.VideoCapture(0)
    cap.set(3,wCam)
    cap.set(4,hCam)

    detector = htm.handDetector(maxHands=1)
    wScr, hScr  = pyautogui.size()


    while True:
        #hand landmarks
        success, img = cap.read()
        img = detector.findHands(img)
        lmList,bbox = detector.findPosition(img)

        # tip of index and middle fingers
        if len(lmList) !=0:
            x1,y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]

        #which fingers are up
        fingers = detector.fingersUp()
        cv2.rectangle(img,(frameR,frameR),(wCam-frameR, hCam-frameR),
                    (255,0,255),2)
        
        # only index finger moving mode
        if fingers[0] == 1 and fingers[1] == 0:
            x3 = np.interp(x1,(frameR,wCam-frameR),(0,wScr))
            y3 = np.interp(y1, (frameR,hCam-frameR),(0,hScr))

            clocX=plocX+(x3-plocX) / smoothening
            clocY=plocY+(y3-plocY) / smoothening


            pyautogui.moveTo(wScr-clocX,clocY)
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            plocX,plocY=clocX,clocY

        if fingers[0]==1 and fingers[1] == 1:
            length, img, lineInfo = detector.findDistance(8,12,img)
            print(length)
        # Find distance b/w index and middle  
            if length<40:
                cv2.circle(img,(lineInfo[4],lineInfo[5]),
                        15, (0,255,0), cv2.FILLED)
                pyautogui.click()
        
        if fingers[0] == 0 and fingers[1] ==0  and fingers[2]==0 and fingers[3]==0:
            pyautogui.press("down")
        
        if fingers[0] == 0 and fingers[1] ==0  and fingers[2]==0 and fingers[3]==1:
            pyautogui.press("up")
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN ,3,(255,0,255),3)
        cv2.imshow("Image",img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

mouse()
