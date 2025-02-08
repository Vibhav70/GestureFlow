# GestureFlow  
A Hand Gesture Control System using OpenCV, MediaPipe, and PyAutoGUI  

## Introduction  
**GestureFlow** is an innovative project that enables users to control various applications using hand gestures. By leveraging computer vision and machine learning, it allows users to interact with their devices in real time through a webcam. The system supports controlling a mouse, playing a car racing game, and managing media playback using natural hand movements.  

Additionally, as part of this project, a **custom racing game was developed in Unity**, featuring a map of my college. This game integrates gesture-based controls, allowing users to steer their vehicle using hand motions for an immersive experience.  

## Features  
- **Mouse Control**: Move the cursor, click, and scroll using hand gestures.  
- **Car Racing Game Control**: Steer and accelerate a vehicle in a Unity-based racing game using hand movements.  
- **Media Player Control**: Play, pause, adjust volume, and skip tracks using predefined gestures.  
- **Web-Based Interface**: Integrated into a Flask-powered web application for a seamless user experience.  

## Technologies Used  
- **OpenCV**: Real-time image processing and computer vision for detecting hand movements.  
- **MediaPipe**: Google's AI-based framework for hand tracking and gesture recognition.  
- **PyAutoGUI**: Automates mouse and keyboard actions based on recognized gestures.  
- **Flask**: Enables web-based interaction with gesture recognition features.  
- **Unity**: Used to design and develop a custom racing game featuring my college’s map.  

## Installation  

### Prerequisites  
- Python 3.x  
- Unity (for the racing game)  
- Webcam for real-time gesture detection  

### Setup Instructions  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/GestureFlow.git
   cd GestureFlow
   ```  
2. Install dependencies:  
   ```bash
   pip install opencv-python mediapipe pyautogui flask numpy
   ```  
3. Run the Flask application:  
   ```bash
   python app.py
   ```  
4. Open the application in your web browser and start using gesture controls!  

## Usage  
- **Mouse Control**:  
  - Move your hand to control the cursor.  
  - Pinch gesture for clicking.  
  - Scroll by tilting your hand up or down.  
- **Racing Game**:  
  - Tilt hand left or right to steer.  
  - Forward motion to accelerate.  
  - Open palm to brake.  
- **Media Player Controls**:  
  - Thumbs-up: Play/Pause  
  - Swipe left/right: Previous/Next track  
  - Two-finger up/down: Volume control  

## Future Enhancements  
- Adding AI-based gesture customization for personalized controls.  
- Enhancing the Unity racing game with more maps and multiplayer support.  
- Expanding gesture support for additional applications like presentations and smart home controls.  

## Acknowledgments  
- OpenCV and MediaPipe for their robust computer vision and tracking capabilities.  
- Flask for enabling a seamless web-based interface.  
- Unity for providing an excellent game development environment.  
