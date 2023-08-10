from cocdice import dice
from sys import exit
import os
os.system('clear')

enemy = {'STR':40,'DEX':50,'APP':0,'POW':20,'LUK':30,'HP':14}
en_charge = False

def load_player(termdict1 = {'STR':60,'CON':0,'DEX':50,'APP':0,'POW':20,'LUK':30},HP = 8 ):
    # Reading essential data
    player = termdict1
    player['HP'] = HP
    return player

player = load_player()
pl_charge = False

items = {'bondage':2, 'water':1, 'grenade':1}


print("\033[33m----------------------------------\033[0m")

def check_game_over(player = player, enemy = enemy):
    if player['HP'] <= 0:
        kp_line('YOU DIED')
        return True
    elif enemy['HP'] <= 0:
        kp_line('Enemy is eliminated. You won!')
        return True
    else:
        return False



def kp_line(txt):
    print("\033[31mKeeper 📖: \033[0m")
    print(txt)
    print("\033[33m----------------------------------\033[0m")

    

def attack():
    kp_line('Press ENTER to roll a 1d4')
    
    atk = input()
    dmg = dice('1d4',True)
    print('')
    
    if atk == '规则是用来打破的':
        dmg = 9999
    
    chance = dice('1d5')
    if chance == 1:
        kp_line('You miss!')
    else:
        kp_line('You cause '+ str(dmg) + ' damage to the enemy.')
        enemy['HP'] -= dmg
    input()
    
    
def item(items):
    kp_line('Check you items:')
    print(items)
    choice = input()
    # bondage
    if choice == 'bondage':
        items['bondage'] -= 1
        
        # check whether remain
        if items['bondage'] < 0:
            kp_line('You have no bondage left')
            input()
        else:
            player['HP'] += 1
            # Check exceed
            if player['HP'] > 8:
                player['HP'] = 8
                kp_line('You waste 1 bondage')
                input()
            else:
                kp_line('You recover 1 HP')
                input()
                
                kp_line('You status:')
                print(player)
                input()
    
    # useless water
    elif choice == 'water':
        kp_line('You drink one bottle of water, you feel so nice.')
        input()
        
    # explosion
    elif choice == 'grenade':
        items['grenade'] -= 1
        # check whether remain
        if items['grenade'] < 0:
            kp_line('You have no grenade left')
            input()
        else:
            
            kp_line('Press ENTER to roll a 1d2')
            cheat = input()
            if cheat == 'EXPLOSION':
                chance = 2
            else:
                chance = dice('1d2')
            
            if chance == 1:
                kp_line('The grenade slip...,you cause yourself 6 damage....')
                input()
                player['HP'] -= 6
                
                
                kp_line('You status:')
                print(player)
                input()
                
            else:
                kp_line('EXPLOSION!!!\nYou cause enemy 8 damage!')
                input()
                enemy['HP'] -= 8
            
    else:
        kp_line('You missed your chance to use item.')
        input()
                
    
def defend():
    kp_line('defend is not available')
    input()


def enemy_attack(en_charge):
    # Check charging
    if en_charge:
        kp_line('Enemy is attacking, rolling 2d3...')
        dmg = dice('2d3',True)
        en_charge = False
    else:
        kp_line('Enemy is attacking, rolling 1d3...')
        dmg = dice('1d3',True)
        
    input('')
    chance = dice('1d5')
    
    # Check defend
    if chance == 1:
        kp_line('Enemy missed')
    else:
        kp_line('You loss '+ str(dmg) + ' HP.')
        player['HP'] -= dmg
    input('')


def enemy_charge(en_charge):
    kp_line('Enemy is charging, it will cause double damage next round!')
    en_charge = True
    input()
    

def fake_option():
    
    while True:
        kp_line("Your turn, please select your option\n1.ATTACK   2.USE ITEM   3.Defend   4.CHARM   5.CAPTURE")
        choice = input()
        try:
            if int(choice) in range(1,6):
                pass
            else:
                kp_line('That is not an option')
                input()
                os.system('clear')
                continue
        except:
            if choice == '傻逼kp':
                print('')
                print("\033[31mKeeper 📖: \033[0m")
                print('你再骂！？')
                print("\033[33m----------------------------------\033[0m")
                input()
                os.system('clear')
            else:
                kp_line('瞎输些啥呢？')
                input()
                os.system('clear')
            
        # 整活
        if choice == '4':
            kp_line('你确定要魅惑这个？\nhttp://img1.gamersky.com/image2015/07/20150723lyb_8/image005.jpg')
            input()
            os.system('clear')
            
        elif choice == '5':
            kp_line('宁隔这宝可梦呢？')
            input()
            os.system('clear')
            
        # 正常选项
        elif choice == '1':
            attack()
            break
    
        elif choice == '2':
            item(items)
            break
    
        elif choice == '3':
            defend()
            break
        
        
def option():
    while True:
        kp_line("Your turn, please select your option\n1.ATTACK   2.USE ITEM   3.Defend")
        choice = input()
        try:
            if int(choice) in range(1,4):
                break
            else:
                kp_line('That is not an option')
                input()
                continue
        except:
            kp_line('You commit a wrong command, you turn has skipped')
            input()
            break
            
    if choice == '1':
        attack()
    elif choice == '2':
        item(items)
    elif choice == '3':
        defend()
    
    

def fight():
    
    kp_line('Encounter enemy:' + "\033[31m Rom the Vacuous Spider': \033[0m")
    input()
    os.system('clear')
    
    fake_option()
    os.system('clear')
    
    while True:
       
       # Enemy's turn
       if dice('1d4') == 1:
            enemy_charge(en_charge)
       else:
            enemy_attack(en_charge)
            
       if check_game_over():
           break
       
       kp_line('Your status:')
       print(player)
       input()
       os.system('clear')
       
       # Player's turn
       option()
       if check_game_over():
           break
       os.system('clear')
       
   
fight()


    
    
    
    
    
    
