import gpiozero
from colorzero import Color
rgb=gpiozero.RGBLED(red=9, green=10, blue=11)
c=input("What is 2+2")
if c==("4"):
    rgb.color=Color("green")
else:
    rgb.color=Color("red")





