import gpiozero
import time
import signal
import turtle

t=turtle.Turtle()
led=gpiozero.LED(17)
button=gpiozero.Button(2)

button.wait_for_press()

button.when_pressed = t.goto(100,100)
button.when_released = t.goto(0,0)

signal.pause()