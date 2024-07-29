import gpiozero
import time
import signal
import turtle

buzz=gpiozero.Buzzer(15)
led=gpiozero.LED(17)
button=gpiozero.Button(2)

def pressOn():
    led.on()
    #buzz.beep()
    buzz.on()
    
def pressOff():
    led.off()
    buzz.off()

button.when_pressed = pressOn
button.when_released = pressOff

signal.pause()
    