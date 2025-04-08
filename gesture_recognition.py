import cv2
import mediapipe as mp
import numpy as np
import pyautogui
import pyttsx3
import screen_brightness_control as sbc
import subprocess
import os
import ctypes
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Initialize media pipe and utilities
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Finger tips (Thumb to Pinky)
finger_tips = [4, 8, 12, 16, 20]
finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]

# Start webcam
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

# Text-to-speech
engine = pyttsx3.init()
engine.say("Gesture control ready!")
engine.runAndWait()

# Audio control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
vol_range = volume.GetVolumeRange()
min_vol, max_vol = vol_range[0], vol_range[1]

# Distance calculation
def calc_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

# Finger status check
def fingers_up(hand_landmarks):
    fingers = []
    if hand_landmarks.landmark[finger_tips[0]].x < hand_landmarks.landmark[finger_tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)
    for tip in finger_tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

# Main loop
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmark, mp_hands.HAND_CONNECTIONS)

            lm = hand_landmark.landmark
            finger_status = fingers_up(hand_landmark)

            # Get coordinates
            x1, y1 = int(lm[8].x * w), int(lm[8].y * h)  # Index
            x2, y2 = int(lm[4].x * w), int(lm[4].y * h)  # Thumb
            x3, y3 = int(lm[12].x * w), int(lm[12].y * h)  # Middle
            x4, y4 = int(lm[16].x * w), int(lm[16].y * h)  # Ring

            # ------------------ Mouse Control ------------------
            if finger_status == [0, 1, 0, 0, 0]:
                pyautogui.moveTo(x1 * screen_width // w, y1 * screen_height // h)
                cv2.putText(frame, "🖱️ Mouse Move", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 255, 100), 2)

            # ------------------ Left Click ------------------
            if calc_distance((x1, y1), (x2, y2)) < 40 and finger_status[1] == 1:
                pyautogui.click()
                cv2.putText(frame, "👆 Left Click", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            # ------------------ Volume Control ------------------
            vol_distance = calc_distance((x1, y1), (x2, y2))
            vol_level = np.interp(vol_distance, [30, 200], [0.0, 1.0])
            volume.SetMasterVolumeLevelScalar(vol_level, None)
            vol_percent = int(vol_level * 100)
            cv2.putText(frame, f"🔊 Volume: {vol_percent}%", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
            if vol_percent % 10 == 0:
                engine.say(f"Volume {vol_percent} percent")
                engine.runAndWait()

            # ------------------ Brightness Control ------------------
            bright_dist = calc_distance((x2, y2), (x4, y4))
            brightness = int(np.interp(bright_dist, [30, 200], [0, 100]))
            sbc.set_brightness(brightness)
            cv2.putText(frame, f"💡 Brightness: {brightness}%", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 200, 0), 2)
            if brightness % 25 == 0:
                engine.say(f"Brightness {brightness} percent")
                engine.runAndWait()

            # ------------------ Launch Notepad ------------------
            if finger_status == [1, 1, 1, 1, 1]:
                subprocess.Popen(["notepad.exe"])
                cv2.putText(frame, "📝 Launching Notepad", (10, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 255), 2)
                engine.say("Launching Notepad")
                engine.runAndWait()

            # ------------------ Screenshot ------------------
            if calc_distance((x2, y2), (x3, y3)) < 40:
                pyautogui.screenshot("screenshot.png")
                cv2.putText(frame, "📷 Screenshot Taken", (10, 190), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                engine.say("Screenshot captured")
                engine.runAndWait()

            # ------------------ Lock Screen ------------------
            if finger_status == [0, 0, 0, 0, 0]:
                ctypes.windll.user32.LockWorkStation()
                engine.say("System Locked")
                engine.runAndWait()

    # Show the video feed
    cv2.imshow("AI Hand Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
