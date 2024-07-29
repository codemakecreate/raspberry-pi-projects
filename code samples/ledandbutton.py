from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(17)
button = Button(2)

while True:
    button.wait_for_press()
    print("Pressed!")
    button.when_pressed = led.on
    button.when_released = led.off


