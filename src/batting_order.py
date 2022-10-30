print ("Imported batting_order")

import sys,os
sys.path.append(os.getcwd())

from src import player

class batting_order:
    def __init__(self, bat_1,bat_2,bat_3,bat_4,bat_5,bat_6,bat_7,bat_8,bat_9):
        self.batting_order = [bat_1,bat_2,bat_3,bat_4,bat_5,bat_6,bat_7,bat_8,bat_9]
        self.current_batter = 0
    def next_batter(self):
        return_batter = self.batting_order[self.current_batter]
        self.current_batter = self.current_batter + 1
        if(self.current_batter >= 9):
            self.current_batter = 0
        return return_batter


if __name__ == "__main__":
    order = batting_order(
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
    i = 0
    for i in range(0,16):
        a = order.next_batter()
        print(a.name+" : " + a.doplay())