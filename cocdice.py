import math
import random

def dice(cmd = '1d6',display = False):
    '''
    默认返回一次六面骰子的值，输入 xdy 即使 y面骰子roll x次
    '''    

    time = int(cmd.split('d')[0]) #roll的次数
    dinum = int(cmd.split('d')[1]) #骰子最大数
    roll = []
    result = 0
    
    for i in range(time):
        roll.append(math.ceil(random.uniform(0,dinum)))
        
    if display and time > 1:
        print('Roll result: ',roll)
        print("\033[33m----------------------------------\033[0m")
    
    result = sum(roll)
    
    if display:
        print('Your dice outcome is:',str(result))
    return result

