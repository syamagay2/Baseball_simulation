print("Hello World")

import sys,os
sys.path.append(os.getcwd())

from src import Game

thisgame = Game.Game()
thissituation = thisgame.send_runner(0,2)
print(thisgame.current_situation)

thissituation = thisgame.send_runner(2,2)
thissituation = thisgame.send_runner(0,2)
print(thisgame.current_situation)

thissituation = thisgame.End_ining()
print(thisgame.current_situation)
print(thisgame.game_status)
