import skywriter
import signal

#This prints out the location of the skywriter
@skywriter.move()
    def move(x, y, z):
        print(x, y, z)

signal.pause()
