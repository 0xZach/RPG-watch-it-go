import numpy as np
import PlayerMove

__package__ = 'Classes'

class Map:
    """
    ||==========================================================||
    || Class name: Map                                          ||
    || parent(s): aucun                                         ||
    || constructor: Map(int, int, array, str)                   ||
    || Goal:                                                    ||
    || handle maps                                              ||
    ||==========================================================||
    """
    
    
    # Constructor
    def __init__(self,argHeight: int,argWidth: int, argPath: np.array, argImage: str, x: int, y: int):
        
        # SIZE has constants (might change)
        self.__size = self.__height, self.__width = argHeight,argWidth

        # 2d table with the collisions (still need to find another way to not just need glasses for the rest of our lifes)
        self.__path = argPath

        # image file
        self.__filepath = argImage

        self.__coordinates = [self.__x, self.__y] = x,y
    
    
    # GETs & SETs
    def getSizePx(self):
        return self.__size
    
    def getMapPath(self):
        return self.__path

    def getfileImage(self):
        return self.__filepath
    
    def getCoordinates(self):
        return self.__coordinates
    
    def setCoordinates(self, x, y):
        self.__coordinates = [x,y]
    
    # Methodes
    def toString(self):
        return (str(self.__size) + "; " + self.__filepath + "\n" + str(self.__path))