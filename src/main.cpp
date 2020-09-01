#include <Arduino.h>
#include <blink.h>

#define ONBOARD 13

void setup() {
  pinMode(ONBOARD, OUTPUT);
  // put your setup code here, to run once:
}

void loop() {
  // put your main code here, to run repeatedly:
  blinkOnboardLED(ONBOARD);
}