print("Hello World")

import sys,os
sys.path.append(os.getcwd())

from src import game,player,batting_order

order = batting_order.batting_order(
    player.batter("test_1",400, 0.3, 0.3, 0.4, 0),
    player.batter("test_2",400, 0.3, 0.3, 0.4, 0),
    player.batter("test_3",400, 0.3, 0.3, 0.4, 0),
    player.batter("test_4",400, 0.3, 0.3, 0.4, 0),
    player.batter("test_5",400, 0.3, 0.3, 0.4, 0),
    player.batter("test_6",400, 0.3, 0.3, 0.4, 0),
    player.batter("test_7",400, 0.3, 0.3, 0.4, 0),
    player.batter("test_8",400, 0.3, 0.3, 0.4, 0),
    player.batter("test_9",400, 0.3, 0.3, 0.4, 0)
)

thisgame = game.Game(order)
thisgame.play_Game()