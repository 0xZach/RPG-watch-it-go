import numpy as np

class Map:
    """
    ||==========================================================||
    || Class name: Map                                          ||
    || parent(s): aucun                                         ||
    || constructor: Map()                                       ||
    || Goal:                                                    ||
    || handle maps                                              ||
    ||==========================================================||
    """
    
    
    # Constructor
    def __init__(self,argHeight: int,argWidth: int, argPath: np.array, argImage: str):
        
        # SIZE has constants (might change)
        self.__size = self.__height, self.__width = argHeight,argWidth

        # table 2x2 with the collisions (still need to find another way to not just need glasses for the rest of our lifes)
        self.__path = argPath

        # image file
        self.__filepath = argImage
    
    # GETs & SETs
    def getSizePx(self):
        return self.__size
    
    def getSizeTiles(self):
        return self.__path.shape

    def getfileImage(self):
        return self.__filepath
    
    
    # Methodes
    def toString(self):
        return (str(self.__size) + "; " + self.__filepath + "\n" + str(self.__path))