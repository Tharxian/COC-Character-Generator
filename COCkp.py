import pandas as pd
import csv

def make_char(char_name ='player',termdict1 = {},termdict2 = {}, HP = 0, MOV = 0):
    # Combine character data into one dict
    
    termdict1.update(termdict2)      
    char = {'Name':char_name}
    char.update(termdict1)
    
    char['HP'] = HP
    char['MOV'] = MOV
    return char


def initialise(char = {},csvname = 'playerdata/new.csv'):
    key = char.keys()
    value = char.values()
    rows = zip(key,value)
    with open(csvname,'w',newline='') as f:     
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)
            
            
def char_log(char_name ='player',termdict1 = {},termdict2 = {}, HP = 0, MOV = 0):
    character = make_char(char_name,termdict1,termdict2, HP, MOV)
    
    with open('playerdata/data.txt', 'a') as file:
        writer = file.write
        # 如果CSV文件为空文件，则写入标题行
        if file.tell() == 0:
            writer('NAME,STR,CON,DEX,APP,SAN,LUK,SIZ,EDU,INT,HP,MOV\n')
        for key in character:
            if key == 'MOV':
                writer(str(character[key])+'\n')
            else:
                writer(str(character[key])+',')
   


  
