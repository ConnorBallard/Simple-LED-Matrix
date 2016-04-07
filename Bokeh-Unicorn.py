from __future__ import division
from neopixel import *
import math
import time, colorsys
import numpy as np
import random
import skywriter
import signal

LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # Just leave it at this, normally works!
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 100      # from 0 to 255, keep it low, you don't want to be blinded
LED_INVERT     = False # True to invert the signal (when using NPN transistor level shift)
Width          = 20      # How ever many pixels wide your grid is
Height         = 13       # How ever many pixels wide your grid is
LED_COUNT      = 259      # Total number of LEDs
 
 
ws2812 = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
ws2812.begin()
 
_rotation = 0

#Unicorn Hat Layout
map = [
    [7 ,6 ,5 ,4 ,3 ,2 ,1 ,0 ],
    [8 ,9 ,10,11,12,13,14,15],
    [23,22,21,20,19,18,17,16],
    [24,25,26,27,28,29,30,31],
    [39,38,37,36,35,34,33,32],
    [40,41,42,43,44,45,46,47],
    [55,54,53,52,51,50,49,48],
    [56,57,58,59,60,61,62,63]
]

def xy_to_strip(x, y, strip_len):
    return x * strip_len + y
 
def rotation(r = 0):
    global _rotation
    
    '''
    Set the display rotation valid values:
    0
    90
    180
    270
    '''
    if r in [0,90,180,270]:
        _rotation = r
        return True
    else:
        raise ValueError('Rotation must be 0, 90, 180 or 270 degrees')
        return

def get_index_from_xy(x, y):
  
 #Convert an x, y value to an index on the display
 
    if x > 7 or x < 0:
        raise ValueError('X position must be between 0 and 7')
        return
    if y > 7 or y < 0:
        raise ValueError('Y position must be between 0 and 7')
        return

    y = 7-y

    if _rotation == 90:
        x, y = 7, 7-x
    if _rotation == 180:
        x, y = 7-x,7-y
    if _rotation == 270:
        x, y = 7-y,x
 
    return map[x][y]
	
def set_pixel(x, y, r, g, b):
    '''
    Set a single pixel to RGB colour
    '''
    index = get_index_from_xy(x, y)
    if index != None:
        ws2812.setPixelColorRGB(index, r, g, b)

def make_gaussian(fwhm, x0, y0):
    x = np.arange(0, 8, 1, float)
    y = x[:, np.newaxis]
    fwhm = fwhm
    gauss = np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) ** 2) / fwhm ** 2)
    return gauss

@skywriter.move()
def spot(x, y, z):
    print(x, y, z)

h = 0
@skywriter.move()
def spot(x, y, z):
    global h
    x0 = x * 7
    y0 = y * 7
    if z == 0:
        z = 0.01
    fwhm = 1/z
    gauss = make_gaussian(fwhm, x0, y0)
    for j in range(8):
        for i in range(8):
            s = 0.8
            v = gauss[i,j]
            rgb = colorsys.hsv_to_rgb(h/10000, s, v)
            r = int(rgb[0]*255.0)
            g = int(rgb[1]*255.0)
            b = int(rgb[2]*255.0)
            set_pixel(i, j, r, g, b)
    ws2812.show()
    time.sleep(0.0005)
    h += 1
    if h > 10000:
        h = 0

signal.pause()
