import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

PIN_LED = 12

GPIO.setup(PIN_LED, GPIO.OUT)

p = GPIO.PWM(PIN_LED, 50)

p.start(0)
try:
    while True:
        for dc in range(0, 99, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.2)
        for dc in range(99, 0, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.2)
except KeyboardInterrupt:
    p.stop()
finally:
    GPIO.cleanup()