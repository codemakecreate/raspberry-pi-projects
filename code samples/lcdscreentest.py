import smbus
from time import sleep, strftime
from datetime import datetime
from LCD1602 import CharLCD1602

lcd1602 = CharLCD1602()

lcd1602.init_lcd()
count = 0
while(True):
    lcd1602.write(0, 0, "Hello World")
    lcd1602.write(0, 1, "here is line two...")
    sleep(5)
    lcd.clear()
    sleep(5)