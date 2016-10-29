import math

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
        elif affichage=='image':
            if sense.pressure >= 1023: 
                sense.load_image("soleil.png")
            elif sense.pressure >= 1013:
                sense.load_image("variable.png")
            elif sense.pressure >= 1000:
                sense.load_image("nuage.png")
            else:
                sense.load_image ("pluie.png")
                

            sense.set_pixel(0,7,0,255,0)
                
                
            sense.set_pixel(0,7,0,255,00);
            nbpix=sense.humidity/100*6+1;
            print (nbpix)
            nbpixint=math.floor(nbpix)
            print(nbpixint)
            sense.set_pixel(nbpixint,7,0,255,0);

            counter = 0;
            while (counter <= nbpixint):
                print (counter)
                sense.set_pixel(counter,7,0,255,0);
                counter = counter +1;


        print("bouton relaché")
        
        if affichage=='image': #condition de l'affichage
            affichage='texte'
        elif affichage=='texte': #condition du texte
            affichage='image'

            print(affichage)

    






#(==) comparaison
#(=) affectation se qui est a droite, on le met a gauche
#print("The joystick was {} {}".format(event.action, event.direction))
