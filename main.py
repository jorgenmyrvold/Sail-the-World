Encoderleft_pin = 23


from GPIO import DigitalInputDevice
import math
import signal   #muligens overflødig  ----Vurdert slettet              
import sys
import RPi.GPIO as GPIO
from encoder import Encoder




def main():
    #settup
    encoder_l = Encoder(23,left)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, 
            callback=encoder_callback, bouncetime=50)

    #test part
    i == 2
    while i> 1
        sleep(500)
        i = i + 1
    return 0


if __name__ == "__main__":
    main()