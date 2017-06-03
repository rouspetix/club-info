from sense_hat import SenseHat

sense = SenseHat ()

sense.set_imu_config(False, False, False)  # compass only

north = sense.get_compass()
print("North: %s" % north)


raw = sense.get_compass_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))


# Reinitialisation de la matrice

x = 0
while (x <= 7):
    y = 0
    while (y <= 7):
        sense.set_pixel(x, y, 0,0,0)
        y = y + 1
    x = x + 1



# initalisation axes
counter = 0
while (counter <= 6):
    sense.set_pixel(counter, 6, 48, 48, 48)
    sense.set_pixel(counter, 0, 48, 48, 48)
    sense.set_pixel(0, counter, 48, 48, 48)
    sense.set_pixel(6, counter, 48, 48, 48)

    counter = counter+1

sense.set_pixel(3, 0, 255, 48, 48)
        
    
