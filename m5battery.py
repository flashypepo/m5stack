"""
m5Battery.py hosted with ❤ by GitHub

Run the code and voila! you can now get battery statistics on the screen.
© 2026 K for Kunal | My Pen My Voice
Built with Hugo
Theme Stack designed by Jimmy

How to Get M5Stack Battery Status with UIFlow 1.3.2 MicroPython
Sep 19, 2019
2 minute read

URL: https://blog.ikunal.in/kunal/2019/09/19/how-to-get-m5stack-battery-status-with-uiflow-1-3-2-micropython/

2026-0326 PP original code from URL
"""

from m5stack import *
from m5ui import *
from uiflow import *
import machine

# Battery management for M5Stack Fire using IP5306 PMU:
IP5306_ADDR = const(0x75)
IP5306_REG_READ0 = const(0x78)  #PP modified: const(0x70)

# i2c
I2C_SCL = const(22)
I2C_SDA = const(21)

CHARGE_100 = '0x00'
CHARGE_75 = '0x80'
CHARGE_50 = '0xC0'
CHARGE_25 = '0xE0'
CHARGE_0 = '0xF0'

buf = bytearray(1)
value = 1

i2c = machine.I2C(
    scl=machine.Pin(I2C_SCL),
    sda=machine.Pin(I2C_SDA)
)
# devices = i2c.scan()
# if len(devices) == 0:
#  text = "No Devices Found"
# else :
#  for device in devices:
#    text = device

#setScreenColor(lcd.LIGHTGREY)  # PP modified: (0x222222)
setScreenColor(lcd.BLACK)  # PP modified: (0x222222)

#label3 = M5TextBox(14, 140, str(value),
#                   str(value), lcd.FONT_Default,
#                   0xFFFFFF, rotate=0)
label3 = M5TextBox(14, 14,
                   str(value), lcd.FONT_DejaVu24,
                   lcd.GREEN, rotate=0)

while True:
    #data = i2c.readfrom_mem(IP5306_ADDR,
    #                      IP5306_REG_READ0, 1)
    #print("Data: {0:02X}".format(data[0]))  # Debug: print raw register
    i2c.readfrom_mem_into(IP5306_ADDR,
                          IP5306_REG_READ0,
                          buf)

    if bytearray([int(CHARGE_100)]) == buf:
        value = 100
    else:
        value = 2

    if bytearray([int(CHARGE_75)]) == buf:
        value = 75

    if bytearray([int(CHARGE_50)]) == buf:
        value = 50

    if bytearray([int(CHARGE_25)]) == buf:
        value = 25

    if bytearray([int(CHARGE_0)]) == buf:
        value = 0

    label3.setText("Battery Level: {0} %".format(str(value)))

    wait_ms(2)