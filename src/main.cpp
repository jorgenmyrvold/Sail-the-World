#include <Arduino.h>
#define ONBOARD 13

void setup() {
  pinMode(ONBOARD, OUTPUT);
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(ONBOARD, LOW);
  delay(1000);
  digitalWrite(ONBOARD, HIGH);
  delay(1000);
}