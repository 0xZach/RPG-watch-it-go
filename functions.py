from numpy import array
import pathlib
import pygame as pg
from Classes.ClassMap import Map
from Classes.PlayerMove import Player_Moving
from Classes.WinControl import WinRoot









# this function moves the entity in parameters around depending on the direction chosen

def move(map: Map, mapImage, player: Player_Moving, direction: int, root: WinRoot, facing_sprites: array, walking_sprites: array):
    # we keep in memory the value of the original position of the entity on the map
    
    mapPath = map.getMapPath()

    row = int(player.getmapPos()[0])
    line = int(player.getmapPos()[1])

    #x = map.getCoordinates()[0]
    #y = map.getCoordinates()[1]

    # we define the collision checkers depending on the direction
    if(direction == 0):
        rowCheck = row
        lineCheck = line-1
        tileMove = (-root.getTileSize()[1])
        
    elif(direction == 1):
        rowCheck = row-1
        lineCheck = line
        tileMove = (-root.getTileSize()[0])

    elif(direction == 2):
        rowCheck = row+1
        lineCheck = line
        tileMove = (root.getTileSize()[0])

    elif(direction == 3):
        rowCheck = row
        lineCheck = line+1
        tileMove = (root.getTileSize()[1])
    

    # when the entity can walk
    if mapPath[lineCheck][rowCheck] == 0:
        
        # we change the position of the entity on the map depending on the direction
        if(direction == 0 or direction == 3):
            player.setmapPosY(lineCheck)
        elif(direction == 1 or direction == 2):
            player.setmapPosX(rowCheck)

    # against a wall or later an object the animation plays but withouth changing position


    print(tileMove/player.getVel())

    for i in range(10):

        # updating the real position this time (for the map too now), and only if there is no collision ahead
        if mapPath[lineCheck][rowCheck] == 0:

            if(direction == 0 or direction == 3):
                map.setCoordinates(map.getCoordinates()[0],map.getCoordinates()[1]+(-tileMove)/player.getVel())
                print(map.getCoordinates()[1],player.getrealPos()[1])

            elif(direction == 1 or direction == 2):
                map.setCoordinates(map.getCoordinates()[0]+ (-tileMove)/player.getVel(),map.getCoordinates()[1])
                print(map.getCoordinates()[0],player.getrealPos()[0])
        
        # animating until the end of the loop
        if i == 0 :
            root.fill(array([0,0,0]))
            root.getRoot().blit(mapImage,map.getCoordinates())
            root.getRoot().blit(facing_sprites[direction], (player.getrealPos()[0],player.getrealPos()[1]))
        elif i >= 2 and i < 9 :
            root.fill(array([0,0,0]))
            root.getRoot().blit(mapImage,map.getCoordinates())
            if player.getLastMove() == True :
                root.getRoot().blit(walking_sprites[direction][0], (player.getrealPos()[0],player.getrealPos()[1]))
                
            elif player.getLastMove() == False :
                root.getRoot().blit(walking_sprites[direction][1], (player.getrealPos()[0],player.getrealPos()[1]))
        elif i == 9 :
            root.fill(array([0,0,0]))
            root.getRoot().blit(mapImage,map.getCoordinates())
            root.getRoot().blit(facing_sprites[direction], (player.getrealPos()[0],player.getrealPos()[1]))

        pg.display.flip()
        root.ticking(root.getFPS())

    # don't forget to switch the last move to the opposite, 
    # to keep a fluid animation from on tile to the other
    if player.getLastMove() == True :
        player.setLastMove(False)

    elif player.getLastMove() == False :
        player.setLastMove(True)
           








# this function loads an image past in parameters

def loadImages(imagePath, width, height):

    # get absolute path to /RPG
    file_absolutePath = str(pathlib.Path('RPG').absolute())

    return pg.transform.scale(pg.image.load(file_absolutePath + imagePath).convert_alpha(), (width,height))
