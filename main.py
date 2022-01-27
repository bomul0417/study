import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

with mp_hands.Hands(
    max_num_hands = 2,
    min_detection_confidence=0.8,
    min_tracking_confidence=0.8) as hands:

    while True:
        ret, img = cap.read()
        img = cv2.cvtColor(cv2.flip(img, 1), cv2.COLOR_BGR2RGB)
        results = hands.process(img)

        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                h1 = hand_landmarks.landmark[8]
                h2 = hand_landmarks.landmark[5]

                dif = abs(h1.x - h2.x)

        cv2.imshow("Image", img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cap.release()