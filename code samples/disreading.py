from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DistanceSensor
from time import sleep

#sensor = DistanceSensor(trigger=18, echo=24, pin_factory=PiGPIOFactory())
sensor = DistanceSensor(trigger=18, echo=24)
print(sensor.distance)
while True:
    sensor.wait_for_in_range()
    print("in range")
    print(sensor.distance * 100)
    sleep(1)
    sensor.wait_for_out_of_range()
    print("in range")
