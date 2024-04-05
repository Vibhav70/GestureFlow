import mediapipe as mp
import cv2
import autopy

# Initialize mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Set up the screen size for mouse control
screen_width, screen_height = autopy.size()

# Initialize hand tracking
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.5)

# Main loop
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)

    # Convert the image from BGR color to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image to find hands
    results = hands.process(image_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmarks
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

            # Convert coordinates to pixel values
            ih, iw, _ = image.shape
            index_px = int(index_tip.x * iw)
            index_py = int(index_tip.y * ih)
            middle_px = int(middle_tip.x * iw)
            middle_py = int(middle_tip.y * ih)

            # Map finger positions to screen width and height
            mapped_x = int(index_px * screen_width / iw)
            mapped_y = int(index_py * screen_height / ih)

            # Move the mouse according to the mapped finger positions
            autopy.moveTo(mapped_x, mapped_y)

            # Perform left click if the middle finger tip is very close to the index finger tip
            dist = ((middle_px - index_px) ** 2 + (middle_py - index_py) ** 2) ** 0.5
            if dist < 30:  # Adjust this threshold as needed
                autopy.click()

            # Draw landmarks on the image
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Display the image
    cv2.imshow('Virtual Mouse', image)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()