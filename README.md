# 🟦 Arduino-Based Real-Time Color Identification System

## 📌 Overview
This project is a real-time embedded system that detects and identifies colors using an Arduino Uno and a TCS3200 color sensor. It captures raw sensor data, transmits it via serial communication, and processes it using a Python-based classification system.

The system demonstrates integration between hardware-level sensing and software-level data processing.

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

## 🔄 System Workflow
1. Color sensor detects reflected light intensity
2. Arduino converts signals into RGB frequency values
3. Data is sent via Serial communication
4. Python receives and processes incoming data
5. System classifies and outputs detected color in real time

---

## 📊 Output Display Format

The system displays detected color information in the following format:

**Family Group | HTML Color | Color Description (for color-blind users)**

Example:
Red Family | Crimson | Dark, strong
Green Family | Forest Green | Medium, soft

---

## 🔄 System Workflow

1. System initializes and enters calibration mode
   - Reads black and white reference values
   - Normalizes sensor range to improve accuracy (0–255 scale)

2. User presses push button to start scanning

3. TCS3200 sensor captures raw RGB frequency values

4. Arduino processes and normalizes RGB values

5. Arduino sends data to Python in format:
   RGB:R,G,B

6. Python processes incoming data:
   - Finds closest HTML color using Euclidean distance
   - Determines color family grouping
   - Retrieves accessibility-friendly description

7. Python sends formatted response:
   OK|Family|HTML Color|Description

8. Arduino receives response and displays it on:
   - 16x2 I2C LCD
   - Includes scrolling text for long outputs

9. System returns to standby state until next scan
    
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
