#include <stdio.h>
#include <Servo.h>

int blue_led = 11;
int red_led = 12;

void setup() {
  // Start the serial communication
  Serial.begin(9600);
  pinMode(blue_led, OUTPUT);
  pinMode(red_led, OUTPUT);
  Serial.println("Arduino is ready");
}

void loop() {
  // Check if data is available to read
  if (Serial.available() > 0) {
    // Read the incoming byte
    String incomingData = Serial.readStringUntil('\n');
    
    // You can add additional logic here to handle the received data
    if (incomingData == "metal") {
      // Do something for metal
      digitalWrite(blue_led, HIGH);
      delay(500);
      digitalWrite(blue_led, LOW);
    } else if (incomingData == "plastic") {
      //Do something for plastic
      digitalWrite(red_led, HIGH);
      delay(500);
      digitalWrite(red_led, LOW);
    } else if (incomingData == "other"){
      digitalWrite(red_led, HIGH);
      digitalWrite(blue_led, HIGH);
      delay(500);
      digitalWrite(red_led, LOW);
      digitalWrite(blue_led, LOW);
    }
  }
}