

from sense_hat import SenseHat
sense=SenseHat()



event = sense.stick.wait_for_event()
print("The joystick was {} {}".format(event.action, event.direction))
