print("Player Class")

import numpy as np
import random

result_translation_table = [
                            "out", #0
                            "4B",  #1
                            "HR",  #2
                            "3BH", #3
                            "2BH", #4
                            "1BH"  #5
                            ]
        #print(self.result_table)

class batter:
    def __init__(self,name,at_bats,avg,slg,obp,hr):
        self.name = name
        self.at_bats = at_bats #At-Bats
        self.avg = avg #batting average #打率
        self.slg = slg #slugging percentage #長打率
        self.obp = obp #on-base percentage #出塁率
        self.hr = hr

        self.table_row = 30
        self.result_table = np.zeros((self.table_row,self.table_row))

        self.result_table = self.create_result_table()

    def create_result_table(self):
        buf_result_table = np.zeros((self.table_row,self.table_row))

        frame_out = (1-self.obp)*pow(self.table_row,2)
        frame_4B = (self.obp-self.avg)/(1-self.avg)*pow(self.table_row,2)

        frame_HR = 0
        frame_2BH = 0
        frame_3BH = 0
        frame_1BH = pow(self.table_row,2) - ( frame_out + frame_4B + frame_HR + frame_2BH)

        print("==================batter's setting====================")
        print( "Out : " + str(frame_out) )
        print( "4B  : " + str(frame_4B) )
        print( "HR  : " + str(frame_HR) )
        print( "2BH : " + str(frame_2BH) )
        print( "1BH : " + str(frame_1BH) )
        print("======================================================")

        i = 0
        j = 0
        i_total = 0
        for i in range(0,self.table_row):
            for j in range(0,self.table_row):
                if(i_total < frame_out):
                    buf_result_table[i][j] = 0
                elif(i_total < ( frame_4B + frame_out ) ):
                    buf_result_table[i][j] = 1
                elif(i_total < ( frame_4B + frame_out + frame_HR ) ):
                    buf_result_table[i][j] = 2
                elif(i_total < ( frame_4B + frame_out + frame_HR + frame_3BH ) ):
                    buf_result_table[i][j] = 3
                elif(i_total < ( frame_4B + frame_out + frame_HR + frame_3BH + frame_2BH) ):
                    buf_result_table[i][j] = 4
                else:
                    buf_result_table[i][j] = 5

                i_total = i_total + 1

        return buf_result_table 

    def doplay(self):
        i = int(random.random()*self.table_row)
        j = int(random.random()*self.table_row)

        return result_translation_table[ int(self.result_table[i][j]) ]


if __name__ == "__main__" :
    a = batter("testplayer",400, 0.3, 0.3, 0.4, 0)
    
    for i in range(0,10):
        print(a.name+" : " + a.doplay())


