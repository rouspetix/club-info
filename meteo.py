import math

from sense_hat import SenseHat
sense=SenseHat()



temp = sense.get_temperature()

press = sense.get_pressure()


#sense.show_message(str(temp))
#sense.show_message(str(press))
#print (temp)
print (sense.pressure)
print(sense.temperature)
print(sense.humidity)

if sense.pressure >= 1023: 
    sense.load_image("soleil.png")
elif sense.pressure >= 1013:
    sense.load_image("variable.png")
elif sense.pressure >= 1000:
    sense.load_image("nuage.png")
else:
    sense.load_image ("pluie.png")
    

sense.set_pixel(0,7,0,255,0)
    
nbpix=sense.humidity/100*6+1
print (nbpix)
nbpixint=math.floor (nbpix)
print(nbpixint)
sense.set_pixel(nbpixint,7,0,255,0)
