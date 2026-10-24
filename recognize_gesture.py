import cv2
import mediapipe as mp
import joblib
import numpy as np

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

model = joblib.load('models/isl_model.pkl')
label_to_gesture = {0: 'A', 1: 'B', 2: 'C', 3: 'D'}

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)
    if results.multi_hand_landmarks:
        landmarks = []
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                landmarks.extend([landmark.x, landmark.y, landmark.z])
        prediction = model.predict([landmarks])
        gesture = label_to_gesture[prediction[0]]
        cv2.putText(frame, gesture, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()