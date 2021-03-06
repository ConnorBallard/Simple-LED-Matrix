import skywriter
import signal
from neopixel import *
import math

LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # Just leave it at this, normally works!
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50      # from 0 to 255, keep it low, you don't want to be blinded
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
WIDTH          = 12      # How ever many pixels wide your grid is
HEIGHT         = 8       # How ever many pixels wide your grid is
LED_COUNT      = 96      # Total number of LEDs

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

def xy_to_strip(x, y, strip_len):
	return x * strip_len + y

#def outputColor(red, green, blue):

def set_pixel(strip, id, Color):
	if id>-10 and id<96:
		strip.setPixelColor(id, Color)
		print 'id {}, {} '.format(id, Color)
	else:
		print 'id {}, {} out of range'.format(id, Color)

def set_shape(strip, x, y, width, height):
    for i in (-3, -2, -1, 0, 1, 2, 3):
        for j in (-3, -2, -1, 0, 1, 2, 3):
            mode = abs(i)+ abs(j)
            if mode == 0:
                Color = outputColor(250, 200, 200)
            elif mode == 1:
                Color = outputColor(250, 0, 100)
            elif mode == 2:
                Color = outputColor(100, 0, 100)
            elif mode == 3:
                Color = outputColor(50, 0, 50)
            elif mode == 4:
                Color = outputColor(25, 0, 25)
            elif mode == 5:
                Color = outputColor(10, 0, 10)
            elif 0 <= x+i <= width and 0 <= y+j <= height:
                set_pixel(strip, xy_to_strip(x+i, y+j, 8), Color)
       	else:
		print 'Problem with Bokeh'

#This prints out the location of the skywriter
@skywriter.move()
def move(x, y, z):
        print(x, y, z)
        tx = int(math.ceil(x * WIDTH))
        # if up and down are reversed remove the "grid_height - " bit
        ty = int(math.ceil(y * HEIGHT))
        print(tx, ty)
        set_shape(strip, tx, ty, WIDTH, HEIGHT)

signal.pause()
