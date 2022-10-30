print("Imported Game Class")

class Game:
    def __init__(self):
        self.Max_ining = 9
        self.End_outcount = 3

        self.current_ining = 0

        self.current_situation = [0,0,0,0,0] #[outcount,1B,2B,3B,score]
        self.game_status = [0,0] #[countinue or End, score]

    def send_runner(self, target, send_num):
        #if(target=0){ result = self.send_runner_0(send_num) }
        #elif If(target=1){ result = self.send_runner_1(send_num) }
        #elif If(target=2){ result = self.send_runner_2(send_num) }
        #elif(target=3){ result = self.send_runner_3(send_num) }

        if(target+send_num<4):
                self.current_situation[target+send_num]=1
        else:
                self.current_situation[4] = self.current_situation[4]+1

        return self.current_situation

    def reset_runner(self):
        return [0,0,0,0,0]

    def update_outcount(self):
        self.current_situation[0] = self.current_situation[0]+1
        
        return self.current_situation

    def End_ining(self):
        self.game_status[1] = self.game_status[1] + self.current_situation[4]
        self.current_situation = self.reset_runner()
        self.current_ining = self.current_ining + 1
        if(self.current_ining > self.Max_ining):
            self.game_status[0] = 1
        return self.game_status
    
