from machine import Pin,I2C
import utime
from time import sleep
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   lcd.blink_cursor_on()
   if distance >= 100:
       lcd.putstr("Distance: " + str("%.1f" % round(distance/100, 2))+"M")
   else :
       lcd.putstr("Distance: " + str("%.1f" % round(distance, 2))+"CM")
   print("The distance from object is ",distance,"cm")
while True:
    ultra()
    sleep(1)
    lcd.clear()