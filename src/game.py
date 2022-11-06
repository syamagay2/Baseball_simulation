print("Imported Game Class")

import sys,os
import numpy as np
sys.path.append(os.getcwd())
from src import batting_order, player

class Game:
    def __init__(self):
        self.Max_ining = 9
        self.End_outcount = 3

        self.current_ining = 1

        self.current_situation = np.array([0,0,0,0,0]) #[outcount,1B,2B,3B,score]
        self.game_status = np.array([0,0]) #[countinue or End, score]
    def __init__(self, order):
        self.Max_ining = 9
        self.End_outcount = 3

        self.current_ining = 1

        self.current_situation = np.array([0,0,0,0,0]) #[outcount,1B,2B,3B,score]
        self.game_status = np.array([0,0]) #[countinue or End, score] 
        self.batting_order = order 

    def Set_batting_order(self,order):
        self.batting_order = order 
    def send_runner(self, buf_situation, target, send_num):
        #if(target=0){ result = self.send_runner_0(send_num) }
        #elif If(target=1){ result = self.send_runner_1(send_num) }
        #elif If(target=2){ result = self.send_runner_2(send_num) }
        #elif(target=3){ result = self.send_runner_3(send_num) }
        if(target+send_num<4):
                buf_situation[target+send_num]=1
        else:
                buf_situation[4] = buf_situation[4]+1
        buf_situation[target] = 0
        return buf_situation

    def reset_runner(self):
        return np.array([0,0,0,0,0])

    def update_outcount(self, outcount, buf_situation):
        buf = buf_situation
        buf[0] = buf[0]+outcount
        
        return buf

    def End_ining(self, buf_situation):
        self.game_status[1] = self.game_status[1] + buf_situation[4]
        buf_situation = self.reset_runner()
        self.current_ining = self.current_ining + 1
        if(self.current_ining > self.Max_ining):
            self.game_status[0] = 1
        return buf_situation

    def restart_game(self):
        self.__init__()

    def update_situation(self,bat_result):
        result_situation = self.current_situation.copy()
        if(bat_result=="out"):
            result_situation = self.update_situation_out(result_situation)
        elif(bat_result=="4B"):
            result_situation = self.update_situation_4B(result_situation)
        elif(bat_result=="HR"):
            result_situation = self.update_situation_HR(result_situation)
        elif(bat_result=="3BH"):
            result_situation = self.update_situation_3BH(result_situation)
        elif(bat_result=="2BH"):
            result_situation = self.update_situation_2BH(result_situation)
        elif(bat_result=="1BH"):
            result_situation = self.update_situation_1BH(result_situation)
        else :
            print(bat_result + " : Not Registration")

        return result_situation

    def update_situation_out(self, buf_situation):
        return self.update_outcount(1,buf_situation)

    def update_situation_4B(self,buf_situation):
        if(buf_situation[1]==1):
            if(buf_situation[2]==1):
                if(buf_situation[3]==1):
                    buf_situation = self.send_runner(buf_situation,3,1)
                buf_situation = self.send_runner(buf_situation,2,1)
            buf_situation = self.send_runner(buf_situation,1,1)
        buf_situation[1] = 1
        return buf_situation

    def update_situation_HR(self,buf_situation):
        for i in reversed(range(1,3)):
            if buf_situation[i]==1 :
                buf_situation = self.send_runner(buf_situation,i,4)
        buf_situation[4] = buf_situation[4]+1
        return buf_situation

    def update_situation_3BH(self,buf_situation):
        for i in reversed(range(1,3)):
            if buf_situation[i]==1 :
                buf_situation = self.send_runner(buf_situation,i,3)
        buf_situation[3] = 1
        return buf_situation

    def update_situation_2BH(self,buf_situation):
        for i in reversed(range(1,3)):
            if buf_situation[i]==1 :
                buf_situation = self.send_runner(buf_situation,i,2)
        buf_situation[2] = 1
        return buf_situation

    def update_situation_1BH(self,buf_situation):
        for i in reversed(range(1,3)):
            if buf_situation[i]==1 :
                buf_situation = self.send_runner(buf_situation,i,1)
        buf_situation[1] = 1
        return buf_situation

    def play_Game(self):
        #print(self.current_situation)
        print("======================== Game Start ====================================")
        while(self.game_status[0] == 0):
            ini_situation = self.current_situation
            batter = self.batting_order.next_batter()
            result = batter.doplay()
            result_situation = self.update_situation(result)

            print(batter.name + " : "+result + " | " )
            print( str(self.current_ining) + "Ining, "+ str(ini_situation[0]) + "Out, "+ str(ini_situation[1]) +"-"+ str(ini_situation[2])+"-"+str(ini_situation[3])+", Score :"+str(ini_situation[4]) + " -> "+ str(result_situation[0]) + "Out, "+ str(result_situation[1]) +"-"+ str(result_situation[2])+"-"+str(result_situation[3])+", Score :"+str(result_situation[4]) )

            if(result_situation[0] == self.End_outcount):
                result_situation = self.End_ining(result_situation)
                #print(result_situation)
            self.current_situation = result_situation.copy()

        print("Final Score : "+str(self.game_status[1]))

