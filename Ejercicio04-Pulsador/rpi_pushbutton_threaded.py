import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

PIN_BUTTON = 16

GPIO.setup(PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def callback_button(PIN_BUTTON):
    print('This callback is executing in another processing thread')
    print('Rissing edge detected in pin #{}'.format(PIN_BUTTON))

GPIO.add_event_detect(PIN_BUTTON, GPIO.RISING, callback=callback_button, bouncetime=200)
print('Executing script: sleeping for 10 s')
time.sleep(10)
print('Script execution finished')

print('Exiting execution: cleanning GPIO setup')
GPIO.cleanup()