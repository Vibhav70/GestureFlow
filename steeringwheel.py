import cv2
import mediapipe as mp
import pydirectinput
import pyautogui

cap = cv2.VideoCapture(0)
cap.set(3, 300)
cap.set(4, 300)

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def write_text(img, text, x, y):
    font = cv2.FONT_HERSHEY_SIMPLEX
    pos = (x, y)
    fontScale = 1
    fontColor = (255, 255, 255)
    lineType = 2
    cv2.putText(img, text, pos, font, fontScale, fontColor, lineType)

def steering_wheel():
    prev_frame_time = 0
    new_frame_time = 0
    img_umat = None  # Initialize img_umat outside the loop
    brake_activated = False  # Variable to track brake activation

    while cap.isOpened():
        success, img = cap.read()
        cv2.waitKey(1)                    #####   wait key adjustment while playing game  #####
        img = cv2.flip(img, 1)
        img_umat = cv2.UMat(img)

        results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        landmarks = results.multi_hand_landmarks
        img_np = cv2.UMat.get(img_umat)  # Convert cv2.UMat to NumPy array

        if landmarks:
            if len(landmarks) == 2:
                left_hand_landmarks = landmarks[1].landmark
                right_hand_landmarks = landmarks[0].landmark

                shape = img.shape
                width, height = 720, 720
                left_mFingerX, left_mFingerY = int(left_hand_landmarks[11].x * width), int(left_hand_landmarks[11].y * height)
                right_mFingerX, right_mFingerY = int(right_hand_landmarks[11].x * width), int(right_hand_landmarks[11].y * height)
                
                if abs(right_mFingerX - left_mFingerX) > 1e-5:
                    slope = (right_mFingerY - left_mFingerY) / (right_mFingerX - left_mFingerX)
                    sensitivity = 0.3

                    # Check for thumbs-up gesture (thumb tip below other fingers)
                    left_thumb_tip = (left_hand_landmarks[4].x * width, left_hand_landmarks[4].y * height)
                    right_thumb_tip = (right_hand_landmarks[4].x * width, right_hand_landmarks[4].y * height)

                    left_finger_tips_y = [left_hand_landmarks[i].y * height for i in range(8, 21, 4)]
                    right_finger_tips_y = [right_hand_landmarks[i].y * height for i in range(8, 21, 4)]

                    if abs(slope) > sensitivity:
                        if slope < 0:
                            print("Turn left.")
                            pydirectinput.keyUp('s')
                            pydirectinput.keyUp("w")
                            pydirectinput.keyUp('a')
                            pydirectinput.keyDown('a')
                        if slope > 0:
                            print("Turn right.")
                            pydirectinput.keyUp('s')
                            pydirectinput.keyUp('w')
                            pydirectinput.keyUp('a')
                            pydirectinput.keyDown('d')
                            
                            
                    if abs(slope) < sensitivity:
                        if min(left_finger_tips_y) > left_thumb_tip[1] and min(right_finger_tips_y) > right_thumb_tip[1]:
                            print("Thumbs-up detected. Applying brake.")
                            brake_activated = True
                            pydirectinput.keyUp('w')
                            pydirectinput.keyUp('d')
                            pydirectinput.keyUp('a')
                            pydirectinput.keyDown('s')
                        else:
                            if brake_activated:
                                print("Releasing brake.")
                                pydirectinput.keyUp('s')
                                brake_activated = False

                            print("Keeping straight.")
                            pydirectinput.keyUp('s')
                            pydirectinput.keyUp('a')
                            pydirectinput.keyUp('d')
                            pydirectinput.keyDown('w')

            for hand_landmarks in landmarks:
                mp_drawing.draw_landmarks(img_np, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Recognition", img_np)

        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()

steering_wheel()