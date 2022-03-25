import sys, pygame
from pygame.constants import KEYDOWN, KEYUP, QUIT
import pygame.locals
import numpy as np
import pathlib

__package__ = 'RPG'

from Classes.ClassMap import Map
from Classes.PlayerMove import Player_Moving
from Classes.WinControl import WinRoot
from maps import path_BrickTiles
from functions import move,loadImages
from character.Images_paths import player_face, player_walk, map_n1, map_n2

file_absolutePath = str(pathlib.Path(__file__).parent.absolute())

# creates the window with the width, height, and ratio of one tile
root = WinRoot(1000,1000,10)

root.setFPS(30) # sets the max frames of actions per second

# size of the player
PLAYER_SIZE = PLAYER_HEIGHT,PLAYER_WIDTH = 100,74

# load the facing animations
player_face_loaded = np.array([loadImages(i,PLAYER_WIDTH,PLAYER_HEIGHT) for i in player_face])

# load the walking animations since it's a 2D array
player_walk_loaded = []

for i in player_walk: # we get the first dimension/array
    second_dimension = []
    for j in range(len(i)):
        # and we load into a temp variable the images from the second dimension
        second_dimension.append(loadImages(i[j],PLAYER_WIDTH,PLAYER_HEIGHT))
    player_walk_loaded.append(second_dimension) # we add the loaded images to the right variable
player_walk_loaded = np.array(player_walk_loaded) # we finally convert the python.list into a numpy.array


# the movement of the player is setup in an instance of the Class Player_Moving
# we need an array with the real position and the map position, and then the boolean of the last move
player = Player_Moving(
    np.array([(root.getSize()[1] - PLAYER_WIDTH)/2,1]),     # X position
    np.array([(root.getSize()[0] - PLAYER_HEIGHT)/2,1]),    # Y position
    True,                                                   # last move
    10                                                      # velocity
    )



# the map is setup in an instance of the Class Map
zeMap = Map(
    int(len(path_BrickTiles.PATH_N1[1])*root.getTileSize()[0]),  # width
    int(len(path_BrickTiles.PATH_N1[0])*root.getTileSize()[1]),  # height
    path_BrickTiles.PATH_N1,                                     # map walkable path
    file_absolutePath + map_n1,                                  # file path to the map image
    (root.getSize()[0] - PLAYER_WIDTH)/2 - root.getTileSize()[0] * player.getmapPos()[0],
    (root.getSize()[0] - PLAYER_WIDTH)/2 - root.getTileSize()[1] * player.getmapPos()[1]
    ) # calculate the position of the map to the player's original tile placement
# ||-----------------------------------------------------------------||
# || here's the math as i recall it:                                 ||
# ||                                                                 ||
# || (width or height to the player's place)                         ||
# ||                                                                 ||
# || minus                                                           ||
# ||                                                                 ||     
# || (size of a tile multiplied by the number of tiles to the player)||
# ||-----------------------------------------------------------------||

# How to load an image and scale it
mapImage = pygame.image.load(zeMap.getfileImage()).convert()
mapImage = pygame.transform.scale(mapImage,(zeMap.getSizePx()[0],zeMap.getSizePx()[1]))



# adds the image of the map **on top** of the other image(s), here it's only on top of the background
root.getRoot().blit(mapImage,zeMap.getCoordinates())

# Display the character **after** the background, so it will be **on top**
root.getRoot().blit(player_face_loaded[3], (player.getrealPos()[0], player.getrealPos()[1]))


while True:
    key_pressed = pygame.key.get_pressed()


    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    # with pygame.key.get_pressed() the walking animation repeats itself while the key isn't released
    # providing a smoother walk
    if pygame.key.get_pressed()[pygame.K_UP]:     
        move(zeMap, mapImage, player, 0, root, player_face_loaded, player_walk_loaded)
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        move(zeMap, mapImage, player, 1, root, player_face_loaded, player_walk_loaded)
    
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        move(zeMap, mapImage, player, 2, root, player_face_loaded, player_walk_loaded)
    
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        move(zeMap, mapImage, player, 3, root, player_face_loaded, player_walk_loaded)
    
    pygame.display.update()
    root.ticking(root.getFPS())
