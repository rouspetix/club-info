

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

        print("bouton relaché")
        
        if affichage=='image': #condition de l'affichage
            affichage='texte'
        elif affichage=='texte': #condition du texte
            affichage='image'

            print(affichage)

    






#(==) comparaison
#(=) affectation se qui est a droite, on le met a gauche
#print("The joystick was {} {}".format(event.action, event.direction))
