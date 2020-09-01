#include <Arduino.h>

class MotorDriver {
    int right;   // Pin to controll right wheel
    int left;    // Pin to controll left wheel
public:
    MotorDriver(int &right, int &left);
};
