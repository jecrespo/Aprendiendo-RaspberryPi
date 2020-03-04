import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

PIN_BUTTON = 16

GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(PIN_BUTTON, GPIO.RISING)
for _ in range(10):
    if GPIO.event_detected(channel):
        print('Button pressed')
        break
    time.sleep(1)
else:
    print('Button was not pressed')

print('Exiting execution: cleanning GPIO setup')
GPIO.cleanup()