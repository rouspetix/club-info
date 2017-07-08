from sense_hat import SenseHat
from math import *
from time import sleep

sense = SenseHat ()

sense.set_imu_config(True, True, True)  # compass only

x = 0
while (x <= 7):
    y = 0
    while (y <= 7):
        sense.set_pixel(x, y, 0,0,0)
        y = y + 1
        x = x + 1



x = 0
y = 0
# Reinitialisation de la matrice
while True:

    sense.set_pixel(x,y, 0,0,0)

    # initalisation bordures
    counter = 0
    while (counter <= 6):
        sense.set_pixel(counter, 6, 48, 48, 48)
        sense.set_pixel(counter, 0, 48, 48, 48)
        sense.set_pixel(0, counter, 48, 48, 48)
        sense.set_pixel(6, counter, 48, 48, 48)

        counter = counter+1


    north = sense.get_compass()

    x=cos(north/180*pi+pi/2)*3+3
    y=sin(north/180*pi+pi/2)*3+3
    sense.set_pixel(x,y, 255,48, 48)

    print("north:",north)
    #sleep(0.5)
