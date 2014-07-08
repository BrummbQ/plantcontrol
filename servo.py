from RPIO import PWM
import time

servo = PWM.Servo()

pin=25
min=900
max=2300
# ??
neutral=int((max+min)/2)
settings=[min,neutral,max]

try:
        while True:
                for w in settings:
                        servo.set_servo(pin, w)
                        time.sleep(1)

except KeyboardInterrupt:
        # Clear servo on GPIO17
        servo.stop_servo(pin)
