
from sense_hat import SenseHat
sense=SenseHat()



temp = sense.get_temperature()

press = sense.get_pressure()

#sense.show_message(str(temp))
#sense.show_message(str(press))
print (temp)
print (press)
