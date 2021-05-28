from numpy import tile
import pygame as pg


class WinRoot:
    """
    ||==========================================================||
    || nom de classe: WinRoot                                   ||
    || parent(s): aucun                                         ||
    || constructeur: WinRoot()                                  ||
    || But:                                                     ||
    ||                                                          ||
    ||==========================================================||
    """
    
    
    # Constructor
    def __init__(self, width, height, tilesSize):
        
        # initialize the window
        pg.init()

        # determinates the size of the window in pixels
        self.__size = [self.__width, self.__height] = [width, height]
        
        # configurates the window to the size desired
        self.__root = pg.display.set_mode(self.__size)
        
        # fills the background with black
        self.__root.fill((0,0,0))


        # keep in memory the size of a tile
        self.__tileSize = self.__width/tilesSize, self.__height/tilesSize

        self.__clock = pg.time.Clock()
    
    def getSize(self):
        return self.__size
    
    def getTileSize(self):
        return self.__tileSize
    
    def getFPS(self):
        return self.__MAXfps

    def setFPS(self, MAXfps):
        self.__MAXfps = MAXfps
    
    def getRoot(self):
        return self.__root
    

    # Methods
    def ticking(self, ticking):
        self.__clock.tick(ticking)
    




        
    
    
    
    # GETs & SETs
    
    
    
    
    # Methods
    