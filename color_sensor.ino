#include <Wire.h>
#include <LiquidCrystal_I2C.h>

#define s0 8
#define s1 9
#define s2 10
#define s3 11
#define outPin 12
#define BUTTON_PIN 2

LiquidCrystal_I2C lcd(0x27, 16, 2);

// ---------- SCROLL ----------
String line1 = "";
String line2 = "";

int scrollIndex1 = 0;
int scrollIndex2 = 0;

unsigned long lastScroll = 0;
const int scrollDelay = 250;

// ---------- STATES ----------
enum ScannerState {
  STATE_WAIT_CALIBRATE,
  STATE_WAIT_START,
  STATE_SCANNING_DELAY,
  STATE_SCAN,
  STATE_SEND,
  STATE_WAIT_REPLY,
  STATE_SHOW_STATIC,
  STATE_SCROLL_RESULT,
  STATE_PAUSE
};

ScannerState state = STATE_WAIT_CALIBRATE;

// ---------- TIMING ----------
unsigned long stateStart = 0;
const unsigned long SCAN_DELAY_TIME = 1000;
const unsigned long RESPONSE_TIMEOUT = 2000;
const unsigned long STATIC_TIME = 3000;
const unsigned long SCROLL_TIME = 3000;

// ---------- RGB ----------
int R = 0, G = 0, B = 0;

// ---------- CALIBRATION ----------
int rWhite, gWhite, bWhite;
int rBlack, gBlack, bBlack;

bool calibrated = false;

// ---------- BUTTON ----------
bool buttonPressed() {
  if (digitalRead(BUTTON_PIN) == LOW) {
    delay(20);
    if (digitalRead(BUTTON_PIN) == LOW) {
      while (digitalRead(BUTTON_PIN) == LOW);
      delay(20);
      return true;
    }
  }
  return false;
}

// ---------- RESET ----------
void clearDisplayData() {
  line1 = "";
  line2 = "";
  scrollIndex1 = 0;
  scrollIndex2 = 0;
}

// ---------- DISPLAY SET ----------
void setDisplay(String family, String name, String desc) {
  clearDisplayData();
  line1 = family + " | " + name + "                ";
  line2 = desc + "                ";
}

// ---------- UI ----------
void showWaitCalibrate() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Press button");
  lcd.setCursor(0, 1);
  lcd.print("to calibrate");
}

void showWaitStart() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Cal done");
  lcd.setCursor(0, 1);
  lcd.print("Press to start");
}

// ---------- SETUP ----------
void setup() {
  Serial.begin(9600);

  pinMode(s0, OUTPUT);
  pinMode(s1, OUTPUT);
  pinMode(s2, OUTPUT);
  pinMode(s3, OUTPUT);
  pinMode(outPin, INPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  digitalWrite(s0, HIGH);
  digitalWrite(s1, LOW);

  lcd.init();
  lcd.backlight();

  showWaitCalibrate();
}

// ---------- RAW READ ----------
unsigned long readRaw(bool s2v, bool s3v) {
  digitalWrite(s2, s2v);
  digitalWrite(s3, s3v);

  delay(5);

  unsigned long readings[7];

  for (int i = 0; i < 7; i++) {
    readings[i] = pulseIn(outPin, LOW);
    delay(2);
  }

  for (int i = 0; i < 6; i++) {
    for (int j = i + 1; j < 7; j++) {
      if (readings[j] < readings[i]) {
        unsigned long t = readings[i];
        readings[i] = readings[j];
        readings[j] = t;
      }
    }
  }

  return readings[3];
}

// ---------- CALIBRATION ----------
void calibrateSensor() {

  calibrated = false;

  lcd.clear(); lcd.print("Get Ready");
  lcd.setCursor(0, 1); lcd.print("WHITE");
  delay(4000);

  lcd.clear(); lcd.print("Scanning...");
  lcd.setCursor(0, 1); lcd.print("WHITE");
  delay(1500);

  rWhite = readRaw(LOW, LOW);
  gWhite = readRaw(HIGH, HIGH);
  bWhite = readRaw(LOW, HIGH);

  lcd.clear(); lcd.print("Get Ready");
  lcd.setCursor(0, 1); lcd.print("BLACK");
  delay(4000);

  lcd.clear(); lcd.print("Scanning...");
  lcd.setCursor(0, 1); lcd.print("BLACK");
  delay(1500);

  rBlack = readRaw(LOW, LOW);
  gBlack = readRaw(HIGH, HIGH);
  bBlack = readRaw(LOW, HIGH);

  lcd.clear(); lcd.print("Calibrated!");
  delay(1500);

  calibrated = true;
}

// ---------- SCAN ----------
void scanRGB() {

  if (!calibrated) return;

  const int samples = 10;

  float rSum = 0, gSum = 0, bSum = 0;

  for (int i = 0; i < samples; i++) {

    int rRaw = readRaw(LOW, LOW);
    int gRaw = readRaw(HIGH, HIGH);
    int bRaw = readRaw(LOW, HIGH);

    float rNorm = (float)(rRaw - rBlack) / (rWhite - rBlack);
    float gNorm = (float)(gRaw - gBlack) / (gWhite - gBlack);
    float bNorm = (float)(bRaw - bBlack) / (bWhite - bBlack);

    rNorm = constrain(rNorm, 0.0, 1.0);
    gNorm = constrain(gNorm, 0.0, 1.0);
    bNorm = constrain(bNorm, 0.0, 1.0);

    rSum += rNorm;
    gSum += gNorm;
    bSum += bNorm;

    delay(10);
  }

  float rVal = (rSum / samples) * 255;
  float gVal = (gSum / samples) * 255;
  float bVal = (bSum / samples) * 255;

  float brightness = (rVal + gVal + bVal) / 3.0;

  float total = rVal + gVal + bVal;
  if (total > 0) {
    rVal = (rVal / total) * 255;
    gVal = (gVal / total) * 255;
    bVal = (bVal / total) * 255;
  }

  float maxVal = max(rVal, max(gVal, bVal));
  if (maxVal > 0) {
    rVal = (rVal / maxVal) * 255;
    gVal = (gVal / maxVal) * 255;
    bVal = (bVal / maxVal) * 255;
  }

  // ---------- BROWN ----------
  bool isBrown = (brightness < 115) &&
                (rVal > 150) &&
                (gVal > 70 && gVal < 180) &&
                (bVal < 120);

  if (isBrown) {
      R = 165;
      G = 100;
      B = 40;
      return;
  }
   
  // ---------- NORMAL ----------
  R = (int)rVal;
  G = (int)gVal;
  B = (int)bVal;
}  

// ---------- LOOP ----------
void loop() {

  switch (state) {

    case STATE_WAIT_CALIBRATE:
      if (buttonPressed()) {
        calibrateSensor();
        showWaitStart();
        state = STATE_WAIT_START;
      }
      break;

    case STATE_WAIT_START:
      if (buttonPressed()) {
        clearDisplayData();
        lcd.clear();
        lcd.print("Scanning...");
        stateStart = millis();
        state = STATE_SCANNING_DELAY;
      }
      break;

    case STATE_SCANNING_DELAY:
      if (millis() - stateStart > SCAN_DELAY_TIME) {
        state = STATE_SCAN;
      }
      break;

    case STATE_SCAN:
      scanRGB();
      state = STATE_SEND;
      break;

    case STATE_SEND:
      Serial.print("RGB:");
      Serial.print(R); Serial.print(",");
      Serial.print(G); Serial.print(",");
      Serial.println(B);

      stateStart = millis();
      state = STATE_WAIT_REPLY;
      break;

    case STATE_WAIT_REPLY:
      if (Serial.available()) {
        String reply = Serial.readStringUntil('\n');
        reply.trim();

        if (reply.startsWith("OK|")) {

          int p1 = reply.indexOf('|');
          int p2 = reply.indexOf('|', p1 + 1);
          int p3 = reply.indexOf('|', p2 + 1);

          String family = reply.substring(p1 + 1, p2);
          String name   = reply.substring(p2 + 1, p3);
          String desc   = reply.substring(p3 + 1);

          setDisplay(family, name, desc);

          lcd.clear();
          lcd.setCursor(0, 0);
          lcd.print(line1.substring(0, 16));
          lcd.setCursor(0, 1);
          lcd.print(line2.substring(0, 16));

          stateStart = millis();
          state = STATE_SHOW_STATIC;
        }
      }

      if (millis() - stateStart > RESPONSE_TIMEOUT) {
        lcd.clear();
        lcd.print("Timeout");
        stateStart = millis();
        state = STATE_SHOW_STATIC;
      }
      break;

    case STATE_SHOW_STATIC:
      if (millis() - stateStart > STATIC_TIME) {
        stateStart = millis();
        state = STATE_SCROLL_RESULT;
      }
      break;

    case STATE_SCROLL_RESULT:
      if (millis() - lastScroll > scrollDelay) {
        lastScroll = millis();

        lcd.setCursor(0, 0);
        lcd.print(line1.substring(scrollIndex1, scrollIndex1 + 16));
        lcd.setCursor(0, 1);
        lcd.print(line2.substring(scrollIndex2, scrollIndex2 + 16));

        scrollIndex1++;
        scrollIndex2++;

        if (scrollIndex1 > line1.length() - 16) scrollIndex1 = 0;
        if (scrollIndex2 > line2.length() - 16) scrollIndex2 = 0;
      }

      if (millis() - stateStart > SCROLL_TIME) {
        state = STATE_PAUSE;
        stateStart = millis();
      }
      break;

    case STATE_PAUSE:
      if (millis() - stateStart > 500) {
        showWaitStart();
        state = STATE_WAIT_START;
      }
      break;
  }
}