from numpy import array
import pygame


# arrays to contain the different sprites
player_face = array([

    '\character\Sprite 1-1.png',  # face north

    '\character\Sprite 1-2.png', # face left

    '\character\Sprite 1-3.png', # face right

    '\character\Sprite 1-4.png' # face south
])

player_walk = array([
    [
    '\character\Sprite 2-1.png',
    
    '\character\Sprite 2-2.png' 
    ], # up walk
    
    [
    '\character\Sprite 2-4.png',
    
    '\character\Sprite 2-3.png' 
    ], # left walk

    [
    '\character\Sprite 2-5.png',
    
    '\character\Sprite 2-6.png'
    ], # right walk
    
    [
    '\character\Sprite 2-7.png',
    
    '\character\Sprite 2-8.png'
    ] # down walk
])


map_n1 = '\maps\BrickTiles_surface_test.png'