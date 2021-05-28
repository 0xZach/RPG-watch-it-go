
__package__ = 'Classes'

from numpy import array


class Player_Moving:
    """
    ||==========================================================||
    || Class name: Player_Moving                                ||
    || parent(s): aucun                                         ||
    || constructor: Player_Moving(array,array,bool)             ||
    || Goal:                                                    ||
    || Handle the player's coordinates                          ||
    || Handle the walking animations                            ||
    ||==========================================================||
    """


    # Constructor
    def __init__(self, posX:array, posY:array, lastMove:bool):
        
        # array that contains the real and map coordinates of the player (real,map)
        self.__posX = posX

        self.__posY = posY

        # boolean that alternates between true and false to handle smooth walking animations
        self.__lastMove = lastMove
    

    # GETs & SETs
    def getrealPos(self):
        return (self.__posX[0],self.__posY[0])
    
    def getmapPos(self):
        return (self.__posX[1],self.__posY[1])
    
    def getLastMove(self):
        return self.__lastMove
    
    def setrealPosX(self,newRealX:float):
        self.__posX = [newRealX,self.__posX[1]]

    def setmapPosX(self,newmapX:float):
        self.__posX = [self.__posX[0],newmapX]
    
    def setrealPosY(self,newRealY:float):
        self.__posY = [newRealY,self.__posY[1]]

    def setmapPosY(self,newmapY:float):
        self.__posY = [self.__posY[0],newmapY]
    
    def setLastMove(self, newMove):
        self.__lastMove = newMove
    

    # Methods