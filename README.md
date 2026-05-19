# 🟦 Arduino-Based Real-Time Color Identification System

## 📌 Overview
This project is a calibrated embedded color recognition system that integrates Arduino-based sensor acquisition with Python-based classification and bidirectional serial communication.

It features real-time RGB normalization, nearest-color matching using Euclidean distance, and an accessibility-focused color description layer designed for color-blind users.

The system uses a state machine architecture to manage calibration, scanning, processing, and display phases.

---

## ⚙️ System Architecture

### Block Diagram
![Block Diagram](assets/01_block_diagram_system_overview.png)

### Flowchart
![Flowchart](assets/02_flowchart_color_detection_logic.png)

### Circuit Diagram
![Circuit Diagram](assets/03_circuit_diagram_tcs3200_arduino_uno.png)

---

## 🔧 Hardware Components
- Arduino Uno
- TCS3200 Color Sensor
- 16x2 LCD (I2C Module)
- Push Button (for input/control)
- Breadboard
- Jumper wires

---

## 💻 Software Tools
- Arduino IDE
- Python 3.x
- PySerial (for serial communication)
- LiquidCrystal_I2C library (Frank de Brabander)
- NumPy (optional for processing)
  
---

## 🚀 Key Features

- Real-time color detection using TCS3200 sensor
- Calibration system using black/white reference
- RGB normalization (0–255 scaling)
- Nearest HTML color matching (Euclidean distance)
- Bidirectional Arduino ↔ Python communication
- 16x2 LCD real-time display with scrolling text
- Color-blind friendly output descriptions

---

## 🔄 System Workflow

1. System calibrates using black and white reference values
2. User triggers scanning via push button
3. Arduino reads RGB sensor values
4. Arduino normalizes RGB (0–255 scale)
5. Data is sent to Python via serial communication
6. Python processes and classifies color
7. Python sends formatted result back to Arduino
8. Arduino displays output on 16x2 LCD
   
---

## 📊 Output Display Format

The system displays detected color information in the following format:

**Family Group | HTML Color | Color Description (for color-blind users)**

Example:
Red Family | Crimson | Dark, strong
Green Family | Forest Green | Medium, soft

---

## 🔄 System Interaction

- Arduino acts as the **main controller**
  - Handles calibration
  - Manages sensor readings
  - Controls LCD display
  - Runs system state machine

- Python acts as the **processing unit**
  - Receives RGB values from Arduino
  - Performs color classification using Euclidean distance
  - Maps RGB → HTML color → family group → description
  - Sends formatted result back

- Communication is handled via **bidirectional Serial protocol**
  - Arduino → Python: `RGB:R,G,B`
  - Python → Arduino: `OK|Family|HTML Color|Description`

- LCD acts as the **user interface layer**
  - Displays processed results
  - Handles scrolling text for long outputs
 
---

## 📂 Project Structure

```
arduino/
│── color_sensor.ino        # Arduino code for sensor data acquisition  

python/
│── color_processor.py      # Python script for processing and classification  

assets/
│── 01_block_diagram_system_overview.png  
│── 02_flowchart_color_detection_logic.png  
│── 03_circuit_diagram_tcs3200_arduino_uno.png  
