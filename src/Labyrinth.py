import numpy as np
import random as rdm

import src.convert_W_C as c
import src.MazeBuilder as mb
class Labyrinth(object):
    """
        Noé Favier
        24/06/2021
    """

    class cell:

        def __init__(self, c, w):
            """
                c = coordonees (int[]) > [x,y]
                w = wall (int) > 1 : wall | 0 : no wall
            """
            self.coord = c
            self.type = w
            
            
        def getType(self):
            return self.type 

        def getCoord(self):
            return self.coord 

        def update(self, x):
            self.coord=x


    def __init__(self,x,y):
        """
            x = longueur du labyrinth
            y = largeur  du labyrinth
        """
        self.longueur = x
        self.largeur = y
        self.TAB = np.empty(x*y, dtype=object)
        self.vic = False

    def build(self):
        labyRaw = mb.BUILD(self.longueur, self.largeur)
        laby = labyRaw
        #conversion format du MazeBuilder sur mon format
        for i in range(0,len(laby)):
            for u in range(0,len(laby[i])):
                case = laby[i][u]
                
                if   case == 'c':
                    case = self.cell([i,u],0)
                elif case == 'w':
                    case = self.cell([i,u],1)
                elif case == 'j':
                    case = self.cell([i,u],2)
                elif case == 's':
                    case = self.cell([i,u],3)
                else :
                    case = self.cell([i,u],666)
                
                laby[i][u] = case

            
        
        self.TAB = laby      

    def show(self):
        returnal = ""
                
        trie = self.TAB

        for i in range(0,len(trie)):
            for u in range(0, len(trie[i])):
                 returnal += c.traduct(trie[i][u].getType())
            
            returnal += "\n"
        
        if self.vic is True : 
            returnal = "\n\n\n      -_-_-_-_-_-_\n\n      V I C T O R Y !!\n\n      -_-_-_-_-_-_\n"
            
        return returnal





    #PLAYER------------------------------------------------------------------------#

    def getJoueur(self):        
        for ligne in self.TAB:
            for case in ligne:
                if case.getType() == 2:
                    return case

    def getSortie(self):        
        for ligne in self.TAB:
            for case in ligne:
                if case.getType() == 3:
                    return case

    def switchCells(self,c1,c2):

        ##did he won ?

        if ( c1 == self.getJoueur() and c2 == self.getSortie() ) or ( c2 == self.getJoueur() and c1 == self.getSortie() ) :
            self.vic = True
            if c1 == self.getJoueur() :
                c2 = c1
                c1 = self.cell([0, 0],0) #we don't care about new coordonees because the game is finished
            if c2 == self.getJoueur() :
                c1 = c2
                c2 = self.cell([0, 0],0) #we don't care about new coordonees because the game is finished
            pass
        #\

        ##no, we can just move the player : 
        co1x=c1.getCoord()[0]
        co1y=c1.getCoord()[1]
        
        co2x=c2.getCoord()[0]
        co2y=c2.getCoord()[1]
        
        tmp = c1
        c2.update([co1x,co1y])
        self.TAB[co1x][co1y] = c2

        tmp.update([co2x,co2y])
        self.TAB[co2x][co2y] = tmp      

    def deplacer(self, d):
        """
        d = direction : 1 char ( b(as) ; h(aut) ; d(roite) ; g(auche) )
        """
        joueur = self.getJoueur()

        xActu = joueur.getCoord()[0]
        yActu = joueur.getCoord()[1]

        authorizedCells = [0,3]
        
        if d=='b':
            #bas
            selected = self.TAB[xActu+1][yActu]
            
            if selected.getType() in authorizedCells :
                self.switchCells(selected,self.getJoueur())

        if d=='h':
            #haut
            selected = self.TAB[xActu-1][yActu]
            
            if selected.getType() in authorizedCells :
                self.switchCells(selected,self.getJoueur())

        if d=='d':
            #droite
            selected = self.TAB[xActu][yActu+1]
            
            if selected.getType() in authorizedCells :
                self.switchCells(selected,self.getJoueur())

        if d=='g':
            #gauche
            selected = self.TAB[xActu][yActu-1]
            
            if selected.getType() in authorizedCells :
                self.switchCells(selected,self.getJoueur())
        

