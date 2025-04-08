# Gesture_Recognition



```markdown
# 🖐️ Hand Gesture Controlled Desktop Interface

A powerful computer interaction system using **hand gestures** captured via webcam. This Python-based project uses **MediaPipe**, **OpenCV**, **PyAutoGUI**, **ScreenBrightnessControl**, and **PyCaw** to allow real-time control over the mouse, volume, brightness, and system operations — all with your fingers! 🧠💻

---

## 🚀 Features

| ✋ Gesture | 🧠 Feature | 🛠️ Action |
|-----------|------------|------------|
| Index Finger Up | Move Mouse | Controls mouse pointer based on index finger position |
| Thumb + Index Close | Left Click | Simulates a left mouse click |
| Thumb + Index Distance | Volume Control | Adjusts system volume |
| Thumb + Ring Distance | Brightness Control | Adjusts system screen brightness |
| All Fingers Up (Open Palm) | Launch App | Launches Notepad (configurable) |
| Thumb + Middle Close | Screenshot | Takes and saves a screenshot |
| Fist (No Fingers Up) | Lock Screen | Locks the screen instantly |
| 🗣️ Voice Feedback | Smart Confirmation | Speaks out volume, brightness level, and system actions |

---

## 📦 Requirements

Install the required libraries using pip:

```bash
pip install opencv-python mediapipe pyautogui screen_brightness_control comtypes pycaw pyttsx3
```

---

## 🧠 Tech Stack

- **Python 3.7+**
- **MediaPipe**: For real-time hand tracking
- **OpenCV**: To process video feed from the webcam
- **PyAutoGUI**: To simulate mouse/keyboard actions
- **PyCaw**: To control system volume
- **ScreenBrightnessControl**: To control screen brightness
- **pyttsx3**: To enable voice-based feedback (offline)

---

## 📸 How It Works

1. The webcam captures real-time video.
2. MediaPipe tracks hand landmarks (fingers and joints).
3. Based on finger positions and distances, the program maps gestures to:
   - Mouse pointer movement
   - Mouse click
   - Volume or brightness control
   - Launching apps or system commands
4. pyttsx3 provides voice feedback like:
   - “Volume 60%”
   - “Launching Notepad”
   - “Screenshot captured”

---

## 🧪 Demo

> 🎥 Add demo GIF or video here (Optional but recommended!)

---

## 🧭 Controls Reference

| 🧠 Control | ✋ Gesture | 🎯 Action |
|------------|-------------|-------------|
| Mouse Move | Index Up | Pointer tracks index |
| Left Click | Thumb + Index | Cursor click |
| Volume Control | Thumb + Index Distance | Adjust system volume |
| Brightness Control | Thumb + Ring Distance | Adjust brightness |
| Open App | All Fingers Up | Launch Notepad |
| Screenshot | Thumb + Middle Close | Save screenshot |
| Lock Screen | Fist | Lock PC |
| Exit Program | Press `q` | Quit program |

---

## 🧩 Configuration

Want to launch a different app instead of Notepad?  
Just edit this line in the code:

```python
os.system('start notepad.exe')
```

Replace `'notepad.exe'` with any executable of your choice (e.g., `'calc.exe'`, `'chrome'`, or full path).

---

## 🗂️ File Structure

```
📁 gesture-control-desktop
│
├── gesture_control.py          # Main code file
├── screenshot.png              # Saved screenshots
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
```

---

## ✅ To-Do / Extensions

- [ ] Add right click and scroll gestures
- [ ] Switch virtual desktops with gestures
- [ ] Integrate gesture training via custom model
- [ ] Add dark mode UI for gesture feedback

---

## 📌 Notes

- Make sure your webcam is on and placed steadily.
- Use in a well-lit environment for accurate detection.
- Compatible with Windows (some parts may require modification for Linux/macOS).

---

## 🧑‍💻 Author

**Ajay Kumar Jha**  
👨‍💻 B.Tech in AI & ML | Passionate about Computer Vision & Automation  
📫 [LinkedIn](https://www.linkedin.com/in/ajay-kumar-jha-30b612261/) (add your real profile link)

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and distribute with proper credit.

---

## 🌟 Show Your Support!

If you like this project, give it a ⭐️ on GitHub and share it with your friends!

```

---

Would you like me to help you generate the `requirements.txt` file too?
