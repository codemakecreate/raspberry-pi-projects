from gpiozero import Button, LED, TrafficLights, Buzzer
from time import sleep

button = Button(21)
#led = LED(25)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)


while True:
    #print(button.is_pressed)
    #led.blink()
    #lights.blink()
    buzzer.on()
    #button.wait_for_press()
    #print("Pressed")
    #button.wait_for_release()
    #print("Released")
    button.wait_for_press()
    print("pressed")
    lights.green.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()


