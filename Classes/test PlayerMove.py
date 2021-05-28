import PlayerMove
import numpy as np

player = PlayerMove.Player_Moving(np.array([100*1,1]),np.array([100*1,1]),"left")

print(player.getLastMove())

print(player.getmapPos()[1]+1)
