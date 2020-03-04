import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

PIN_BUTTON = 16

GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
	while True:
		time.sleep(0.05)
	
		if GPIO.input(PIN_BUTTON):
			print('Button is pushed')
except KeyboardInterrupt:
	print('Script execution interrupted')
finally:		
	GPIO.cleanup()
	print('Exiting execution: cleanning GPIO setup')