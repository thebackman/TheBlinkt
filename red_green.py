""" red or green """

import sys
from blinkt import set_pixel, set_brightness, show, clear
import time

set_brightness(0.1)


# get the color 
color = sys.argv[1]

if color == "red":
    r = 190
    g = 0
    b = 0
if color == "green":
    r = 45
    g = 175
    b = 20 

# print(color)

clear()
for i in range(8):
    # print(i)
    set_pixel(i, r, g, b)
show()
time.sleep(1)
clear()





