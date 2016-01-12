#This file contains the functions needed to use the LED matrix with the Skywriter PCB
from neopixel import Color

def set_pixel(strip, id, colour):
	if id>-10 and id<96:
		strip.setPixelColor(id, colour)
		print 'id {}, {} '.format(id, colour)
	else:
		print 'id {}, {} out of range'.format(id, colour)

def set_shape(strip, x, y, width, height):
    for i in (-3, -2, -1, 0, 1, 2, 3):
        for j in (-3, -2, -1, 0, 1, 2, 3):
            mode = abs(i)+ abs(j)
            if mode == 0:
                color = Color(250, 200, 200)
            if mode == 1:
                color = Color(250, 0, 100)
            if mode == 2:
                color = Color(100, 0, 100)
            if mode == 3:
                color = Color(50, 0, 50)
            if mode == 4:
                color = Color(25, 0, 25)
            if mode == 5:
                color = Color(10, 0, 10)
            if 0 <= x+i <= width and 0 <= y+j <= height:
                set_pixel(strip, xy_to_strip(x+i, y+j, 8), color)
                #No idea if this will work ----- set_shape(x, y) ----- needs to be input from skywriter

def pulse(q, strip, width, height):
    forward = 1
    brightness = 0
    loc = [0, 0, 0] #loc[0] = X, loc[1] = Y, loc[2] = STEP
    color = Color(0, 0, 0)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
    strip.show()

    while True: #This loops every 10ms, so led matrix is updated smoothly.
        if q.empty() is False:
            loc = q.get_nowait()
            #print loc
        if forward is 1:
            brightness = brightness + loc[2]
        else:
            brightness = brightness - loc[2]
        if brightness <= 0:
            forward = 1
            brightness = 0
        if brightness >= 255:
            forward = 0
            brightness = 255

        #Do Bokeh stuff here instead of setting all the pixels the same.
        set_shape(strip, loc[0], loc[1], width, height)

def xy_to_strip(x, y, strip_len):
    return x * strip_len + y
