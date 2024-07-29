from gpiozero import LED, Button
from time import sleep
from signal import pause
import turtle

led = LED(17)
button = Button(2)
mike = turtle.Turtle()

while True:
    led.on
    mike.forward(1)
    button.wait_for_press()
    print("Pressed!")
    button.when_pressed = led.on
    button.when_released = led.off
    if mike.xcor()==100:
        led.on

