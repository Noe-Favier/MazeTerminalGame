#-----------Imports EXT------------#
import sys
import random as rdm
import time
import keyboard as kb

#-----------Mes Imports------------#
import src.Labyrinth as labyrinth
import src.Terminal as terminal
#-----------------------#


def main():
    
    while True:
        #os.system('mode con: cols=200 lines=49')
        time.sleep(0.1)
    
def paint():
    term.flush()   
    term.write(lab.show())


#-----------Joueur------------#

#!---!---!---!---!#
def keyEvent():
    kb.add_hotkey("up arrow", haut)
    kb.add_hotkey("down arrow", bas)
    kb.add_hotkey("right arrow", droite)
    kb.add_hotkey("left arrow", gauche)

    kb.add_hotkey("z", haut)
    kb.add_hotkey("s", bas)
    kb.add_hotkey("d", droite)
    kb.add_hotkey("q", gauche)
    kb.add_hotkey("k", resoudre)

    
#!---!---!---!---!#

def haut():
    lab.deplacer('h')
    paint()

def bas():
    lab.deplacer('b')
    paint()

def droite():
    lab.deplacer('d')
    paint()

def gauche():
    lab.deplacer('g')
    paint()

def resoudre():
    #not implemented yet
    pass

if __name__ == "__main__":
    # execute only if run as a script

    x= rdm.randint(40,100)
    y= rdm.randint(40,80)

    term = terminal.Terminal(int(x)+1,int(y)+10)
    lab  = labyrinth.Labyrinth(x,y)

    lab.build()
    term.write(lab.show())

    keyEvent()
    main()