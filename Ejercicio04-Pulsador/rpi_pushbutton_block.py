import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

PIN_BUTTON = 16

GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.wait_for_edge(PIN_BUTTON, GPIO.RISING, timeout=10000)
if PIN_BUTTON is None:
	print('Timeout: button was not pressed')
else:
	print('Button was pressed on pin #{}'.format(PIN_BUTTON))

print('Exiting execution: cleanning GPIO setup')
GPIO.cleanup()