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
- Breadboard
- Jumper wires

---

## 💻 Software Tools
- Arduino IDE
- Python 3.x
- PySerial
- NumPy (optional for processing)

---

## 🔄 System Workflow
1. Color sensor detects reflected light intensity
2. Arduino converts signals into RGB frequency values
3. Data is sent via Serial communication
4. Python receives and processes incoming data
5. System classifies and outputs detected color in real time

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
