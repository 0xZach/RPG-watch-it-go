
__package__ = 'Classes'

from numpy import array


class Player_Moving:

    def __init__(self, posX:array, posY:array, lastMove:bool):
    
        self.__posX = posX
        self.__posY = posY
        self.__lastMove = lastMove
    
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