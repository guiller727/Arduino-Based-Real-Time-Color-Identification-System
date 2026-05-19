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

## 🔄 System Interaction

1. System starts in calibration mode
   - Arduino measures **white reference and black reference**
   - Values are normalized to a 0–255 range

2. User presses push button to start scanning

3. TCS3200 sensor captures raw frequency values for RGB channels

4. Arduino processes and normalizes RGB values (0–255 scale)

5. Arduino sends RGB data to Python via Serial communication

6. Python performs:
   - HTML color matching
   - Color family classification
   - Color-blind friendly description lookup

7. Python sends formatted result back to Arduino:
   `OK|Family|HTML Color|Description`

8. Arduino receives data and displays it on:
   - 16x2 LCD display (I2C)
   - Includes scrolling UI for long text

9. System pauses briefly before returning to standby mode

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
