import numpy as np

PATH = np.array([
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,1,1,1,1,1],
    [1,0,1,1,0,0,1,1,1,1,1],
    [1,0,1,1,0,0,1,1,1,1,1],
    [1,0,0,0,0,0,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,2,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1]
]) # path of the map


# TODO: this is gonna get time consuming very quickly, find another way to make the path