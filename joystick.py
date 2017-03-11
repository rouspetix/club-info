

from sense_hat import SenseHat
sense=SenseHat()


affichage='image'

while(True):

    
    event = sense.stick.wait_for_event()
    
    if event.action=='released': #condition relachement
        if affichage=='texte':
            print (sense.pressure)
            print(sense.temperature)
            print(sense.humidity)
            temp = str(round (sense.get_temperature(),0))

            pressure=str(round (sense.get_pressure(),0))
            humidity=str(round (sense.get_humidity(),2))
            



            
            sense.show_message("temperature: ",0.15)
            sense.show_message(temp+"C",0.15,[0,0,255])
            sense.show_message("humidite:",0.15)
            sense.show_message(humidity+"%",0.15,[0,0,255])
            sense.show_message("pression:",0.15)
            sense.show_message(pressure+"hPa",0.15,[0,0,255])

        print("bouton relaché")
        
        if affichage=='image': #condition de l'affichage
            affichage='texte'
        elif affichage=='texte': #condition du texte
            affichage='image'

            print(affichage)

    






#(==) comparaison
#(=) affectation se qui est a droite, on le met a gauche
#print("The joystick was {} {}".format(event.action, event.direction))
