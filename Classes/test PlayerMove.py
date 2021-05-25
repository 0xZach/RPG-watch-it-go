import PlayerMove
import numpy as np

zePlayerMove = PlayerMove.Player_Moving(np.array([100*1,1]),np.array([100*1,1]),"left")

print(zePlayerMove.getLastMove())

print(zePlayerMove.getmapPos()[1]+1)
