#include <Arduino.h>

void blinkOnboardLED(int pin){
    digitalWrite(pin, LOW);
    delay(500);
    digitalWrite(pin, HIGH);
    delay(2000);
}