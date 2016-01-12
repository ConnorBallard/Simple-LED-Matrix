#This should be a short version where i can just call functions

import functions #Hopefully this imports everything from the fuctions file.
import time
import signal
from neopixel import *
import threading
import Queue
import skywriter

# Settings for your matrix and Pins:
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # Just leave it at this, normally works!
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 50      # from 0 to 255, keep it low, you don't want to be blinded
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
WIDTH          = 12      # How ever many pixels wide your grid is
HEIGHT         = 8       # How ever many pixels high your grid is
LED_COUNT = WIDTH * HEIGHT  #Is this needed?

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)

#Take move from skywriter
#import move from skywriter and input into x,y,z co-ordinates
#Give option for mood, create an input of 3 mechanical buttons
    #Sad, Happy, excited
      #each mood has it's own colour and and key signature
