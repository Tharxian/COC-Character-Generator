'''Yifan Ge (Tharxian) all rights reserved'''
print('©tharxian 2023')
print('Source code available at:')

import random
import math

def dice6(num = [0,0,0],time = 1):
    roll = []
    result = 0
    for i in range(10):
        roll.append(math.ceil(random.uniform(0,6)))
    for x in range(time):
        result += roll[num[x]]
    return result
        
# 角色名字
print("\033[33m----------------------------------\033[0m")
print("\033[31mKeeper 📖: \033[0m")
print("Welcome to COC dearest investigator!")
char_name = input('May I Have you name please? ')
print("\033[33m----------------------------------\033[0m")
print("\033[31mKeeper 📖: \033[0m")


# 选数字
print("Very well, " + "\033[36m" + char_name + "\033[0m")
print("Now I need you to close your eyes, and tell me the first 3 numbers (0 to 9) that come into your mind.")
input('Press ENTER key to continue.')
print("\033[33m----------------------------------\033[0m")

while True:
    print("\033[36m" + char_name + " 🎲:\033[0m")
    num1 = input('My first number is: ')
    if num1 == 'skip':
        num1 = num2 = num3 = 0
        print("\033[33m----------------------------------\033[0m")
        break
    num2 = input('My second number is: ')
    num3 = input('My third number is: ')
    print("\033[33m----------------------------------\033[0m")
    try:
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
        if num1 in range(0,10) and num2 in range(0,10) and num3 in range(0,10):
            break
        else:
            print("\033[31mKeeper 📖: \033[0m")
            print('Your number is out of 0 to 9')
            print("\033[33m----------------------------------\033[0m") 
    except:
        print("\033[31mKeeper 📖: \033[0m")
        print("Remember, integer only!")
        print("\033[33m----------------------------------\033[0m")

num = [num1, num2, num3]

#开roll
print("\033[35mUnknown voice ❓: \033[0m")
input("Processing...")
print("\033[33m----------------------------------\033[0m")
print("\033[31mKeeper 📖: \033[0m")
print("Your fate is destinied!")
input("Press ENTER to continue.")
print("\033[33m----------------------------------\033[0m")

# Output
print('Name: ' + "\033[36m" + char_name + "\033[0m")
age = math.ceil(random.uniform(10,90))
print('Age: ' + "\033[36m" + str(age) + "\033[0m")
print('')

termset1 = ['STR','CON','DEX','APP','POW','LUK']
termdict1 = {'STR':0,'CON':0,'DEX':0,'APP':0,'POW':0,'LUK':0}

for things in termset1:
    outcome = dice6(num,3)*5
    termdict1[things] = str(outcome)
    print(things + ":___/" "\033[32m" + termdict1[things] + "\033[0m") 
    
termset2 = ['SIZ','EDU','INT']
termdict2 = {'SIZ':0,'EDU':0,'INT':0}
for things in termset2:
    outcome = (dice6(num,2)+6)*5
    termdict2[things] = str(outcome)
    print(things + ":___/" "\033[32m" + termdict2[things] + "\033[0m") 

HP = math.ceil((int(termdict2['SIZ'])+int(termdict1['CON']))/10)

print(' ')
print(' HP:___/' + "\033[32m" + str(HP) + "\033[0m")
print('SAN:___/' + "\033[32m" + termdict1['POW'] + "\033[0m")

# 判断movement，比较STR，DEX和SIZ
case1 = termdict1['STR'] > termdict2['SIZ']
case2 = termdict1['DEX'] > termdict2['SIZ']

if case1:
    if case2:
        MOV = 8
    else:
        MOV = 7
elif case2:
    MOV = 7
else:
    MOV = 6
    
print('MOV：' + "\033[32m" + str(MOV) + "\033[0m")
print(' ')
goon = input('Press ENTER to end  ')

if goon == 'ENTER':
    print("\033[33m----------------------------------\033[0m")
    print("\033[35mUnknown voice ❓: \033[0m")
    input("Initiating simulating fight...")
    print("\033[33m----------------------------------\033[0m")
    print("\033[35mUnknown voice ❓: \033[0m")
    input("Simulating fight is still under develop😊, thank you for testing.")
    print("\033[33m----------------------------------\033[0m")
    
    











