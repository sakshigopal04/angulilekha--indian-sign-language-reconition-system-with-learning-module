import cv2
import mediapipe as mp
import csv
import os

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

def collect_landmarks(gesture_name, num_samples=100):
    # Open the webcam
    cap = cv2.VideoCapture(0)
    data = []
    while len(data) < num_samples:
        ret, frame = cap.read()
        if not ret:
            continue
        # Convert the frame to RGB (MediaPipe requires RGB input)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Process the frame to detect hand landmarks
        results = hands.process(rgb_frame)
        if results.multi_hand_landmarks:
            landmarks = []
            # Extract landmarks for each detected hand
            for hand_landmarks in results.multi_hand_landmarks:
                for landmark in hand_landmarks.landmark:
                    # Save x, y, z coordinates of each landmark
                    landmarks.extend([landmark.x, landmark.y, landmark.z])
            # Append the landmarks to the data list
            data.append(landmarks)
        # Display the webcam feed
        cv2.imshow('Collect Data', frame)
        # Press 'q' to stop data collection
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()
    # Save the collected data to a CSV file
    with open(f'data/train/{gesture_name}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == '__main__':
    # Prompt the user to enter the gesture name
    gesture_name = input("Enter gesture name: ")
    # Collect data for the specified gesture
    collect_landmarks(gesture_name)