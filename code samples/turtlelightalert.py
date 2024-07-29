import turtle
import gpiozero
import time

t=turtle.Turtle()
led=gpiozero.LED(17)
button=gpiozero.Button(2)
limit=100
led.off()


while True:
    t.forward(1)
    pos=t.xcor()
    print(pos)
    if pos > limit:
        print("greater")
        led.on()
        time.sleep(1)