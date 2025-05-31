# this file is the main file for the program
#-----------------------------------------

# import the required modules
from game_objects import Weapon
from game_objects import Person
import random # import the random module
import time # import the time module

# create constant variables for the program
gameOver = False # create a variable to control the game loop
playerMoney = 1500 #a variable for the players money
playerWeapon = Weapon("AR15", "r", 5,0) #a class to store the players weapon
playerChar = Person("Bean", 200, Weapon("AR15", "r", 5, 0), Weapon("Gaster Blaster", "m", 18, 0)) #a class to store the players character data
playerInventory = [] #a list for the players inventory

#----------------------------------------- SET UP THE GAME BOARD -----------------------------------------
#create a custom game board. 0 = empty, 1 = player, 2 = enemy, 3 = treasure, 4 = bomb, 5 = exit, 6 = boss, 7 = visited,
#  8 = wall, 9 = bars, 10 = key, 11 = lock,12 = money 13 = Strabi, 14 = Pickle man, 15 = unwalkable door, 16 = dead body, 17 = Scott the boss
#18 = secrets of the candy caines

nonwalkableobjects = [8,9,13,14,15,17] #objects the player cant collide with
enemynonwalkableobjects = [8,9,13,14,15,2,17,18] #objects the enemy cant collide with
grabbableobjects = [10,12,18] #objects the player can put into there inventory
pickableobjects = [11] #objects the player can use a key on to unlock
playeddialogue2 = False #boolean for the second player dialogue
playeddialogue3 = False #boolean for the third dialogue

#----------------------Maps---------------------------
TutorialMap = [[8,8,8,8,8,8,8,8,8,8,8],
               [8,0,0,0,0,0,0,0,0,0,8],
               [8,0,0,0,12,12,12,0,0,0,8],
               [8,0,0,0,12,12,12,0,0,0,8],
               [8,0,0,0,12,12,12,0,0,0,8],
               [8,0,0,0,0,0,0,0,0,0,8],
               [8,8,8,8,8,11,8,8,8,8,8],
               [8,0,0,0,0,0,0,0,0,0,8],
               [8,0,0,0,0,0,0,0,0,0,8],
               [8,0,0,0,0,0,0,0,0,0,8],
               [8,8,11,8,8,8,9,8,9,8,8],
               [8,0,0,0,0,0,0,0,0,0,8],
               [8,0,0,0,0,0,0,0,0,0,8],
               [8,0,0,0,0,0,0,0,0,0,8],
               [8,0,0,0,0,13,0,0,0,0,8],
               [8,0,0,0,0,0,0,0,0,10,8],
               [8,8,8,8,8,8,8,8,8,8,8]]

TutorialMap2 = [[8,8,8,8,8,8,8,8,8,8,8],
                [8,0,0,0,0,0,0,0,0,0,8],
                [8,0,0,0,0,17,0,0,0,0,8],
                [8,0,0,0,0,0,0,0,0,0,8],
                [8,8,8,8,0,0,0,8,8,8,8],
                [8,0,0,9,0,0,0,9,0,0,8],
                [8,0,0,9,0,0,0,9,0,0,8],
                [8,8,8,8,0,0,0,8,8,8,8],
                [8,0,0,9,0,0,0,9,0,0,8],
                [8,0,0,9,0,0,0,9,0,0,8],
                [8,8,8,8,8,15,8,8,8,8,8]]

Map1 = [[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8],
        [8,0,0,0,0,0,0,8,0,0,0,0,0,0,8],
        [8,0,0,0,0,0,0,8,0,0,0,0,0,0,8],
        [8,0,0,0,0,0,0,0,0,0,0,0,18,0,8],
        [8,0,0,0,0,0,0,8,0,0,0,0,0,0,8],
        [8,0,0,0,0,0,0,8,0,0,0,0,0,0,8],
        [8,8,11,8,8,8,8,8,8,8,8,8,8,8,8],
        [8,0,0,0,0,8,0,0,0,0,0,0,0,0,8],
        [8,0,8,0,8,8,8,0,0,0,0,0,0,0,8],
        [8,0,8,0,0,0,0,0,0,0,0,0,0,0,8],
        [8,0,8,8,8,8,8,8,8,8,8,8,0,0,8],
        [8,0,0,0,0,8,0,0,0,0,0,0,0,0,8],
        [8,8,8,8,0,8,0,0,0,0,8,0,0,0,8],
        [8,10,0,0,0,8,0,0,0,0,8,0,0,0,8],
        [8,8,8,8,8,8,8,15,8,8,8,8,8,8,8]]

Map2 = [[0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0]]

currentmap = TutorialMap #sets the current map

# place the player in the game board
playerX = 5
playerY = 12
currentmap[playerY][playerX] = 1

#place the boss in the game board
bossX = 7
bossY = 3
Map1[bossY][bossX] = 6

# place the exit in a set location
exitX = 5
exitY = 0
currentmap[exitY][exitX] = 5

#Enemies
enemysX = [5,7]
enemysY = [8,8]
enemysHealth = [40,40]

#---------------------PUT ENEMIES ON MAP--------------------
enemycount = 0
for i in enemysX: #goes through all the enemies and sets the location on the game board to the enemy
    y = enemysY[enemycount]
    currentmap[y][i] = 2
    enemycount += 1

#----------------------------WEAPONS-------------------------------------
Weapons = [ #Weapon name, ranged or melee, damage, Recharge
    Weapon("AR15", "r", 5, 0),
    Weapon("Heavy Kunai", "m", 25, 0),
    Weapon("Computah", "m", 10, 0),
    Weapon("Random Figurine", "m", 99999999999, 0),
    Weapon("1000%", "m", 200,5),
    Weapon("Gaster Blaster", "m", 18, 0)
           ]

#-----------------------------PEOPLE------------------------------
People = [ #name, health, Weapon, second weapon
    Person("Strabi",120, Weapon("Heavy Kunai", "m", 25, 0),("1000%", "m", 200, 5)),
    Person("Bean",200, Weapon("AR15", "r", 5, 0),("Gaster Blaster", "m", 18, 0)),
    Person("Pickle Man",200, Weapon("Computah", "m", 10, 0),("Random Figurine", "m", 99999999999, 0))
]
# ----------------------------------------- SET UP THE FUNCTIONS -----------------------------------------

#The following function prints every sublist in the currentmap list. 
def printBoard():
    count = 0
    for i in enemysX:
        currentmap[enemysY[count]][enemysX[count]] = 2
        count += 1
    
    for row in currentmap:
        newrow = "" #for every row in the game board this will check what number it is and adds the corresponding emoji to a variable and then it prints the variable after each row
        for i in row:
            if i == 1 and playerChar.name == "Bean": #Player
                newrow = newrow + "😎"
            elif i == 1 and playerChar.name == "Strabi":
                newrow = newrow + "😊"
            elif i == 1 and playerChar.name == "Pickle Man":
                newrow = newrow + "🤤" 
            elif i == 2: #Enemy
                newrow = newrow + "😠"
            elif i == 0: #Floor
                newrow = newrow + "░░" #▓▓
            elif i == 3: #Treasure -- not implemented
                newrow = newrow + "🪙"
            elif i == 4: #Bomb
                newrow = newrow + "💥"
            elif i == 5: #Exit, go to next level
                newrow = newrow + "🚪"
            elif i == 6: #Big Man
                newrow = newrow + "😡"
            elif i == 7: #Visited location
                newrow = newrow + "▓▓"
            elif i == 8: #Wall
                newrow = newrow + "⬜"
            elif i == 9: #Bars
                newrow = newrow + "II"
            elif i == 10: #key
                newrow = newrow + "🔑"
            elif i == 11: #lock
                newrow = newrow + "🔒"
            elif i == 12: #Money
                newrow = newrow + "💵" #moeny
            elif i == 13: #Strabi
                newrow = newrow + "😊"
            elif i == 14: #Pickle man
                newrow = newrow + "👨" #🧍🏽
            elif i == 15: #unwalkable door
                newrow = newrow + "🚪"
            elif i == 16: #dead body
                newrow = newrow + "💀"
            elif i == 17: #scott the boss
                newrow = newrow + "👾"
            elif i == 18: #secrets of the candy caines
                newrow = newrow + "📜"

        print(newrow)

#This function facilitates movement. X is horizontal, Y is vertical.
def PlayerMove():
    global playerX, playerY, playerInventory, playerChar
    Move = input('Enter the direction you want to move (W,A,S,D),  F if you want to attack with your equiped weapon, \nOr use 1, 2 or 3 to choose between Strabi😊, Pickle Man🤤 and Bean😎 respectivly: ') #Asks player which direction they would like to move.
    Move = Move.lower()

    #W reduces the player Y by 1 to make the player go up
    if Move == 'w':
        if playerY > 0 and (currentmap[playerY - 1][playerX]) not in nonwalkableobjects: #checks if the direction the player wants to move is a collideable object
            if (currentmap[playerY - 1][playerX] in pickableobjects and 10 not in playerInventory): #checks if the direction the player wants to move is a pickable object, if it is it will check it the player has a key
                print('\nYou cannot move in that direction\n')
                time.sleep(0.5)
            else:
                checkBomb(-1, 0)
                currentmap[playerY][playerX] = 0
                playerY -= 1
                pickupObject()
                currentmap[playerY][playerX] = 1
        else:
            print('\nYou cannot move in that direction\n')
            time.sleep(0.5)
    #S increases the player Y by 1 to make the player go down
    elif Move == 's':
        if playerY < 20 and (currentmap[playerY + 1][playerX]) not in nonwalkableobjects: #checks if the direction the player wants to move is a collideable object
            if (currentmap[playerY + 1][playerX] in pickableobjects and 10 not in playerInventory): #checks if the direction the player wants to move is a pickable object, if it is it will check it the player has a key
                print('\nYou cannot move in that direction\n')
                time.sleep(0.5)
            else:
                checkBomb(1, 0)
                currentmap[playerY][playerX] = 0
                playerY += 1
                pickupObject()
                currentmap[playerY][playerX] = 1
        else:
            print('\nYou cannot move in that direction\n')
            time.sleep(0.5)
    #D increases the player Y by 1 to make the player go right
    elif Move == 'd':
        if playerX < 20 and (currentmap[playerY][playerX + 1]) not in nonwalkableobjects: #checks if the direction the player wants to move is a collideable object
            if (currentmap[playerY][playerX + 1] in pickableobjects and 10 not in playerInventory): #checks if the direction the player wants to move is a pickable object, if it is it will check it the player has a key
                print('\nYou cannot move in that direction\n')
                time.sleep(0.5)
            else:
                checkBomb(0, 1)
                currentmap[playerY][playerX] = 0
                playerX += 1
                pickupObject()
                currentmap[playerY][playerX] = 1
        else:
            print('\nYou cannot move in that direction\n')
            time.sleep(0.5)

    #A reduces the player Y by 1 to make the player go left
    elif Move == 'a':
        if playerX > 0 and (currentmap[playerY][playerX - 1]) not in nonwalkableobjects: #checks if the direction the player wants to move is a collideable object
            if (currentmap[playerY][playerX - 1] in pickableobjects and 10 not in playerInventory): #checks if the direction the player wants to move is a pickable object, if it is it will check it the player has a key
                print('\nYou cannot move in that direction\n')
                time.sleep(0.5)
            else:
                checkBomb(0, -1)
                currentmap[playerY][playerX] = 0
                playerX -= 1
                pickupObject()
                currentmap[playerY][playerX] = 1
        else:
            print('\nYou cannot move in that direction\n')
            time.sleep(0.5)
    elif Move == "1": #Switches the player to Strabi
        print("\nCharacter Switched\nSelected: Strabi\n")
        time.sleep(0.5)
        playerChar = Person("Strabi",120, Weapon("Heavy Kunai", "m", 25, 0), Weapon("1000%", "m", 200, 5))
        print(playerChar.name)
    elif Move == "2": #Switches the player to Pickle man
        print("\nCharacter Switched\nSlected: Pickle Man\n")
        time.sleep(0.5)
        playerChar = Person("Pickle Man",200, Weapon("Computah", "m", 10, 0), Weapon("Random Figurine", "m", 9999999999, 0))
        print(playerChar.name)
    elif Move == "3": #Switches the player to Bean
        print("\nCharacter Switched\nSelected: Bean\n")
        time.sleep(0.5)
        playerChar = Person("Bean",200, Weapon("AR15", "r", 5, 0), Weapon("Gaster Blaster", "m", 18, 0))
        print(playerChar.name)

    elif Move == "f": #attacks the enemy with the first index
        global enemysHealth 
        try:
            if playerChar.name == "Bean":
                if len(enemysHealth) > 0:
                    enemysHealth[0] -= playerWeapon.damage
            else:
                print("\nMove unnaccesable.\n")
                time.sleep(0.5)
        except:
            print("nuh uh")

    elif Move == "m": #prints a list of more options for the player
        time.sleep(0.7)
        print("-Press I to check Inventory\n-Press H for help\n")
        time.sleep(0.7)
    
    elif Move == "i": #prints out the players inventory
        print("\n-----Inventory-----")
        keys = 0 #stores how many keys the player has
        money = 0 #stores how much money the player has
        for i in playerInventory:
            if i == 10:
                keys += 1 #adds 1 key
            elif i == 12:
                money += 1000 #adds 1000 money
        if keys == 0 and money == 0: #if the player has no items i will print "nothing :("
            print("Nothing :(")
        if keys > 0: #checks if the player has more than 0 keys and prints how many they have
            print(f"Keys: {keys}")
        if money > 0: #checks if the player has more than 0 money and prints how much they have
            print(f"Money: {money}")
        print("-------------------\n")
        PlayerMove()

    elif Move == "h": #prints out how to play the game
        print("\n------Help-----\n\nyou can only use certain attacks to who they can be used by, so for example you can only use\nthe heavy kunai when you have Strabi selected. Some attacks such as the Computah and Gaster Blaster\nhave lasting effects where the enemy takes damage over time, other attacks such as 1000% take time to charge up.\nAlso You can only shoot people with bean as only she uses the AR15. Don’t try to be greedy if you try to get lots of damage\nby stacking Gaster Blasters it won’t work.\n---------------\n")
        PlayerMove()

    elif Move == "hack": #uhhhh
        count = 0
        for i in enemysHealth:
            enemysHealth[count] = -1
            count += 1

    # Invalid input
    else:
        print('I do not understand that direction')

#This function checks if the player has reached the exit

def checkExit(): #checks if the player has reached the exit for the map
    global gameOver, currentmap, playerX, playerY, enemysX, enemysY, enemysHealth
    if playerX == exitX and playerY == exitY:
        if currentmap == TutorialMap: # if the map is the tutorial map it will change the map to the second tutorial map and change the "setting" for it
            currentmap = TutorialMap2
            playerX = 6
            playerY = 9
            enemysX = [1,2,8,9]
            enemysY = [9,6,5,8]
            enemysHealth = [999999,99999999,9999999,404]
            currentmap[playerY][playerX] = 1
            return
        else: #checks if the player has the required item for each ending
            hassecret = False
            for i in playerInventory: #checks if the player has the secrets of the candy caine
                if i == 18:
                    hassecret = True
            
            if hassecret == True: #normal ending
                print("\nYou: I got the paper!")
                print("\nYou: But i lost the figure...")
                print("\nScott: WHAT")
                print("\n*You all team up and go into pit to rescue the Sojo Gatoru Figurine,You researched its name.\n* Everyone : For Scott!")
                print("[-----------------------------]\n[---MISSION=====PASSED========]\n[-----------------------------]")
            else: #secret ending
                print("\nYou: I made it out alive!")
                print("\nScott: Yeah but weres the secret paper??")
                print("\nYou: oh.")
                print("\n[-----------------------------]\n[===MISSION=====FAILED========]\n[-----------------------------]")
            gameOver = True
            return
        
def pickupObject():# picks up an object
    if (currentmap[playerY][playerX]) in grabbableobjects:
            playerInventory.append((currentmap[playerY][playerX]))
            print("Picked up object!")
  

def checkBomb(y, x):#checks if the player is standing on a bomb
    global playerHealth
    if currentmap[playerY + y][playerX + x] == 4:
        playerHealth -= 50
        print("You stepped on a bomb!")


def checkEnemy():# checks if your on the same tile as an enemy to start a battle
    global gameOver, playerHealth, playerX, playerY, enemysHealth, chosenAttack, enemycount
    #set up neccesary variables
    count = 0
    hack = 0
    beam =  0
    for x in enemysX:
        if playerX == enemysX[count] and playerY == enemysY[count]:#Iterates through enemies to see which one you are fighting
            while enemysHealth[count] > 0 and playerChar.health > 0:
                time.sleep(0.3)
                print("Attacked by enemy!\n")
                playerChar.health -= 15
                time.sleep(0.7)
                print(f"Your Health: {playerChar.health}\n")
                time.sleep(0.7)
                try:
                    if beam == 1:# starts the gaster beam which does damage over time
                        beam = 2
                    chosenAttack = int(input(f"What attack would you like to use:\n1:{playerChar.attack1.name}\n2:{playerChar.attack2.name}\nChoose 1 for first attack. Choose 2 for second attack \n"))# checks which attack you want to use
                    time.sleep(0.3)
                    
                    
                    if playerChar.attack2.name == "Random Figurine":
                        if chosenAttack == 2:
                            enemysHealth[count] -= playerChar.attack2.damage# damages enemy
                            playerChar.attack2.damage = 0# makes it so attack can only be used once
                            print(f"Enemy Health: {enemysHealth[count]}\n")
                        elif chosenAttack ==1:
                            enemysHealth[count] -= playerChar.attack1.damage
                            print(f"Enemy Health: {enemysHealth[count]}\n")
                            hack = 1 #starting key to hack the enmey so it does damage over time
                    elif playerChar.attack2.name == "1000%":# attack recharges over time
                        time.sleep(0.7)
                        print(f"Your 1000% has a level {5-playerChar.attack2.recharge} charge")# show how charged this attack is
                        time.sleep(0.7)
                        if chosenAttack == 2 and playerChar.attack2.recharge < 0:
                            enemysHealth[count] -= playerChar.attack2.damage# only attacks if the attack has recharged the correct amount
                            time.sleep(0.7)
                            print(f"Enemy Health: {enemysHealth[count]}\n")
                            time.sleep(0.7)
                            playerChar.attack2.recharge = 5
                        elif chosenAttack ==1:# base attack
                            enemysHealth[count] -= playerChar.attack1.damage
                            time.sleep(0.7)
                            print(f"Enemy Health: {enemysHealth[count]}\n")
                            time.sleep(0.7)
                        else:
                            time.sleep(0.7)
                            print("\nNot enough emotion\n")
                            time.sleep(0.7)
                    elif playerChar.attack2.name == "Gaster Blaster":
                        if chosenAttack == 2: #starts a series of countdowns duw to its damage being spread over 2 rounds
                            enemysHealth[count] -= playerChar.attack2.damage
                            time.sleep(0.7)
                            print(f"Enemy Health: {enemysHealth[count]}\n")
                            time.sleep(0.7)
                            beam = 1# starts countdown
                        elif chosenAttack ==1:
                            enemysHealth[count] -= playerChar.attack2.damage
                            time.sleep(0.7)
                            print(f"Enemy Health: {enemysHealth[count]}\n")
                            time.sleep(0.7)
                    elif chosenAttack == 1:
                        enemysHealth[count] -= playerChar.attack1.damage
                        time.sleep(0.7)
                        print(f"Enemy Health: {enemysHealth[count]}\n")
                        time.sleep(0.7)
                    elif chosenAttack == 2:
                        enemysHealth[count] -= playerChar.attack2.damage
                        time.sleep(0.7)
                        print(f"Enemy Health: {enemysHealth[count]}\n")
                        time.sleep(0.7)
                    else:
                        time.sleep(0.7)
                        print("\nYou don't know that attack\n")
                        time.sleep(0.7)
                    
                except:
                    time.sleep(0.7)
                    print("Womp Womp\n")
                    time.sleep(0.7)
                playerChar.attack2.recharge -= 1 #cherges the attack by 1
                if beam < 4 and beam > 1:
                    time.sleep(0.7)
                    beam += 1 # gives a fram per round where the attack can play , stops the attack if it goes on for too long.
                    print("The Enemy took damage from you Blaster Beam\n")
                    enemysHealth[count] -= playerChar.attack2.damage
                    time.sleep(0.7)
                    print(f"Enemy Health: {enemysHealth[count]}\n")
                    time.sleep(0.7)
                elif beam > 2:
                   beam = 0
                if hack == 1:
                    enemysHealth[count] -= 5# hacks the enemy to deal damage over time.
                    time.sleep(0.7)
                    print("The enemy took 5 damage from your hacking!\n")
                    time.sleep(0.7)
                    print(f"Enemy Health: {enemysHealth[count]}\n")
                    time.sleep(0.7)

        if playerChar.health < 0:#If the player dies its gaem over.
            gameOver = True
        if enemysHealth[count] < 0:
            pass
    count += 1
def checkBoss():# does the same thing as the enemy but for the boss.
    global bossHealth, bossX, bossY
    global gameOver, playerChar, playerX, playerY, chosenAttack
    hack = 0
    beam =  0
    bossHealth = 1500
    if playerX == bossX and playerY == bossY:
        while playerChar.health > 0 and bossHealth > 0:
            time.sleep(0.3)
            print("Attacked by enemy!\n")
            playerChar.health -= 12
            time.sleep(0.7)
            print(f"Your Health: {playerChar.health}\n")
            time.sleep(0.7)
            try:
                if beam == 1:
                    beam = 2
                chosenAttack = int(input(f"What attack would you like to use:\n1:{playerChar.attack1.name}\n2:{playerChar.attack2.name}\nChoose 1 for first attack. Choose 2 for second attack \n"))
                time.sleep(0.3)        
                if playerChar.attack2.name == "Random Figurine":
                    if chosenAttack == 2:
                        bossHealth -= playerChar.attack2.damage
                        playerChar.attack2.damage = 0
                        print(f"Enemy Health: {bossHealth}\n")
                    elif chosenAttack ==1:
                        bossHealth -= playerChar.attack1.damage
                        print(f"Enemy Health: {bossHealth}\n")
                        hack = 1
                elif playerChar.attack2.name == "1000%":
                    time.sleep(0.7)
                    print(f"Your 1000% has a level {5-playerChar.attack2.recharge} charge")
                    time.sleep(0.7)
                    if chosenAttack == 2 and playerChar.attack2.recharge < 0:
                        bossHealth -= playerChar.attack2.damage
                        time.sleep(0.7)
                        print(f"Enemy Health: {bossHealth}\n")
                        time.sleep(0.7)
                        playerChar.attack2.recharge = 5
                    elif chosenAttack ==1:
                        bossHealth -= playerChar.attack1.damage
                        time.sleep(0.7)
                        print(f"Enemy Health: {bossHealth}\n")
                        time.sleep(0.7)
                    else:
                        time.sleep(0.7)
                        print("\nNot enough emotion\n")
                        time.sleep(0.7)
                elif playerChar.attack2.name == "Gaster Blaster":
                    if chosenAttack == 2:
                        bossHealth -= playerChar.attack2.damage
                        time.sleep(0.7)
                        print(f"Enemy Health: {bossHealth}\n")
                        time.sleep(0.7)
                        beam = 1
                    elif chosenAttack ==1:
                        bossHealth -= playerChar.attack2.damage
                        time.sleep(0.7)
                        print(f"Enemy Health: {bossHealth}\n")
                        time.sleep(0.7)
                elif chosenAttack == 1:
                    bossHealth -= playerChar.attack1.damage
                    time.sleep(0.7)
                    print(f"Enemy Health: {bossHealth}\n")
                    time.sleep(0.7)
                elif chosenAttack == 2:
                    bossHealth -= playerChar.attack2.damage
                    time.sleep(0.7)
                    print(f"Enemy Health: {bossHealth}\n")
                    time.sleep(0.7)
                else:
                    time.sleep(0.7)
                    print("\nYou don't know that attack\n")
                    time.sleep(0.7)
                    
            except:
                time.sleep(0.7)
                print("Womp Womp\n")
                time.sleep(0.7)
            playerChar.attack2.recharge -= 1
            if beam < 4 and beam > 1:
                time.sleep(0.7)
                beam += 1
                print("The Enemy took damage from you Blaster Beam\n")
                bossHealth -= playerChar.attack2.damage
                time.sleep(0.7)
                print(f"Enemy Health: {bossHealth}\n")
                time.sleep(0.7)
            elif beam > 2:
                beam = 0
            if hack == 1:
                bossHealth -= 5
                time.sleep(0.7)
                print("The enemy took 5 damage from your hacking!\n")
                time.sleep(0.7)
                print(f"Enemy Health: {bossHealth}\n")
                time.sleep(0.7)
        # if the player dies they do one last attack which setsup dialogue for a later game, if the boss dies it will output the same dialgue.
        print("You Threw the random figurine")
        time.sleep(2)
        print("Big Man: WHAT HOW , YOULL NEVER TAKE ME, I'LL COME BACK, EVEN IF IT TAKES EVERYONE YOU LOVE, YOU'LL NEVER KILL ME I AM INEVITABLE, \nAND FOR YOU SCOTT THE BOSS, YOU DONT THINK I KNOW ABOUT YOUR LAST JOB!\n")
        time.sleep(4)            
        print("Scott the Boss: No...")
        time.sleep(2)
        print("Big Man: I KILLED THEM, BLASTED MOLTEN CANDY CANE ON THEIR HEAD, THEY'D NEVER SURVIVE THAT...\n YOULL NEVER BE ACCCEPTED OH AND THIS RANDOM FIGURINE... \n")
        time.sleep(4)
        print("ITS GOING IN THE PIT AND SO AM I...")
        time.sleep(4)
        bossX = 0
        bossy = 0

def moveEnemies():# Moves enemies
    count = 0
    for i in enemysX: #in short every enemy checks if there is a wall in the direction it wants to go, if not it will add 1 to the corresponding variable, the variable with the highest number will be the directiont he enemy moves in
        try: 
            enemyup = 0
            enemydown = 0
            enemyleft = 0 
            enemyright = 0

            currentmap[enemysY[count]][enemysX[count]] = 0

            #pain |
            #     V

            #Just a bunch of checks to make sure the enemy doesnt go through a wall
            if enemysX[count] > playerX and currentmap[enemysY[count]][enemysX[count] - 1] not in enemynonwalkableobjects and currentmap[enemysY[count]][enemysX[count] - 1] not in pickableobjects and currentmap[enemysY[count]][enemysX[count] - 1] != 5:
                enemyleft = 1
            elif enemysX[count] < playerX and currentmap[enemysY[count]][enemysX[count] + 1] not in enemynonwalkableobjects and currentmap[enemysY[count]][enemysX[count] + 1] not in pickableobjects and currentmap[enemysY[count]][enemysX[count] + 1] != 5:
                enemyright = 1
            else:
                enemyleft = 0
                enemyright = 0

            if enemysY[count] > playerY and currentmap[enemysY[count] - 1][enemysX[count]] not in enemynonwalkableobjects and currentmap[enemysY[count] - 1][enemysX[count]] not in pickableobjects and currentmap[enemysY[count] - 1][enemysX[count]] != 5:
                enemyup = 1
            elif enemysY[count] < playerY and currentmap[enemysY[count] + 1][enemysX[count]] not in enemynonwalkableobjects and currentmap[enemysY[count] + 1][enemysX[count]] not in pickableobjects and currentmap[enemysY[count] + 1][enemysX[count]] != 5:
                enemydown = 1
            else:
                enemyup = 0
                enemydown = 0

            #if two variable are the same then it will randomly choose one
            if enemyleft == 1 and enemyup != 1 and enemydown != 1:
                if currentmap[enemysY[count]][enemysX[count] - 1] not in enemynonwalkableobjects and currentmap[enemysY[count]][enemysX[count - 1]] not in pickableobjects and currentmap[enemysY[count]][enemysX[count - 1]] != 5:
                    enemysX[count] -= 1
            elif enemyright == 1 and enemyup != 1 and enemydown != 1:
                if currentmap[enemysY[count]][enemysX[count] + 1] not in enemynonwalkableobjects and currentmap[enemysY[count]][enemysX[count + 1]] not in pickableobjects and currentmap[enemysY[count]][enemysX[count + 1]] != 5:
                    enemysX[count] += 1
            elif enemyup == 1 and enemyleft != 1 and enemyright != 1:
                if currentmap[enemysY[count] - 1][enemysX[count]] not in enemynonwalkableobjects and currentmap[enemysY[count] - 1][enemysX[count]] not in pickableobjects and currentmap[enemysY[count] - 1][enemysX[count]] != 5:
                    enemysY[count] -= 1
            elif enemydown == 1 and enemyleft != 1 and enemyright != 1:
                if currentmap[enemysY[count] + 1][enemysX[count]] not in enemynonwalkableobjects and currentmap[enemysY[count] + 1][enemysX[count]] not in pickableobjects and currentmap[enemysY[count] + 1][enemysX[count]] != 5:
                    enemysY[count] += 1
            elif enemyleft == 1 and enemyup == 1:
                i = random.randint(0,1)
                if i == 0:
                    if currentmap[enemysY[count]][enemysX[count] - 1] not in enemynonwalkableobjects and currentmap[enemysY[count]][enemysX[count - 1]] not in pickableobjects and currentmap[enemysY[count]][enemysX[count - 1]] != 5:
                        enemysX[count] -= 1
                else:
                    if currentmap[enemysY[count] - 1][enemysX[count]] not in enemynonwalkableobjects and currentmap[enemysY[count] - 1][enemysX[count]] not in pickableobjects and currentmap[enemysY[count] - 1][enemysX[count]] != 5:
                        enemysY[count] -= 1
            elif enemyright == 1 and enemyup == 1:
                i = random.randint(0,1)
                if i == 0:
                    if currentmap[enemysY[count]][enemysX[count] + 1] not in enemynonwalkableobjects and currentmap[enemysY[count]][enemysX[count + 1]] not in pickableobjects and currentmap[enemysY[count]][enemysX[count + 1]] != 5:
                        enemysX[count] += 1
                else:
                    if currentmap[enemysY[count] - 1][enemysX[count]] not in enemynonwalkableobjects and currentmap[enemysY[count] - 1][enemysX[count]] not in pickableobjects and currentmap[enemysY[count] - 1][enemysX[count]] != 5:
                        enemysY[count] -= 1
            elif enemyleft == 1 and enemydown == 1:
                i = random.randint(0,1)
                if i == 0:
                    if currentmap[enemysY[count]][enemysX[count] - 1] not in enemynonwalkableobjects and currentmap[enemysY[count]][enemysX[count - 1]] not in pickableobjects and currentmap[enemysY[count]][enemysX[count - 1]] != 5:
                        enemysX[count] -= 1
                else:
                    if currentmap[enemysY[count] + 1][enemysX[count]] not in enemynonwalkableobjects and currentmap[enemysY[count] + 1][enemysX[count]] not in pickableobjects and currentmap[enemysY[count] + 1][enemysX[count]] != 5:
                        enemysY[count] += 1
            elif enemyright == 1 and enemydown == 1:
                i = random.randint(0,1)
                if i == 0:
                    if currentmap[enemysY[count]][enemysX[count] + 1] not in enemynonwalkableobjects and currentmap[enemysY[count]][enemysX[count + 1]] not in pickableobjects and currentmap[enemysY[count]][enemysX[count + 1]] != 5:
                        enemysX[count] += 1
                else:
                    if currentmap[enemysY[count] - 1][enemysX[count]] not in enemynonwalkableobjects and currentmap[enemysY[count] - 1][enemysX[count]] not in pickableobjects and currentmap[enemysY[count] - 1][enemysX[count]] != 5:
                        enemysY[count] -= 1
            else:
                return
        except:
            pass
        count += 1

#-------------------------------------Check enemy health------------------
def checkEnemyHealth():
    global enemysHealth

    count = 0
    for i in enemysHealth:
        if i <= 0: #if the enemy health is below 1 then it removes it
            currentmap[enemysY[count]][enemysX[count]] = 16
            enemysHealth.pop(count)
            enemysX.pop(count)
            enemysY.pop(count)
            print("Enemy killed!")
        else: #displays the enemies health
            print(f"Enemy Health: {enemysHealth[count]}")
        
        count += 1


#--------------------------------------------Ask Questions---------------------------------------------
def askquestion(question, answer1, answer2, answer3, answer4): #Question asking function
    answer = 1
    answers = 0
    print(f"\n{question}") #prints the question and each answer, but it the answer is "none" then it wont print it
    if answer1 == "none":
        pass
    else:
        print(f"1. {answer1}")
        answers += 1
    
    if answer2 == "none":
        pass
    else:
        print(f"2. {answer2}")
        answers += 1
    
    if answer3 == "none":
        pass
    else:
        print(f"3. {answer3}")
        answers += 1
    
    if answer4 == "none":
        pass
    else:
        print(f"4. {answer4}")
        answers += 1
    
    try:
        answer = int(input("Option? (say 5 for a random option!) ")) #if the answer isnt one of the options it will choose one at random
    except:
        print("picking random option!")
        answer = random.randint(1,answers)
    
    if answer > answers:
        print("picking random option!")
        answer = random.randint(1,answers)
    
    return(answer)
    

#--------------------------------------------------PRINT-TUTORIAL/BACKSTORY or skip the tutorial level.-------------------------------------------
def tutorial():
    global currentmap, playerX, playerY, playeddialogue2, enemysX, enemysY, enemysHealth
    playtutorial = askquestion("Do you wish to play the tutorial/backstory?","yes","no","none","none")
    if playtutorial == 1: #alot of talking
        print("\nStarting tutorial!")
        time.sleep(1)
        print("\n13|5|2006")
        time.sleep(2)
        print("\n*A van stops in front of a bank*")
        time.sleep(2)
        print("\nStrabi: We all know the plan yeah?")
        time.sleep(2)
        print("\nYou: Yup")
        time.sleep(2)
        print("\nPickle Man: Yeah I think, nevermind can you go over it again")
        time.sleep(3)
        print("\nStrabi: Seriously man, we went over this at least 10 times, whatever")
        time.sleep(3)
        print("\nStrabi: Okay so Pickle, you stay in the van and watch out for cops, theres a walkie and some guns in the back just in case")
        time.sleep(5)
        print("\nStrabi: Then me and Bean go in the bank, 2 minutes max, just in and out as fast as we can")
        time.sleep(2)
        print("\nStrabi: Alright, we all good now?")
        time.sleep(2)
        print("\nPickle Man: Yep")
        time.sleep(2)

    else:
        print("\nOk, skipping tutorial!") #skips the first part of the game
        playeddialogue2 = True
        currentmap = TutorialMap2 #changes the map and its "settings"
        playerX = 5
        playerY = 9
        enemysX = [1,2,8,9]
        enemysY = [9,6,5,8]
        enemysHealth = [999999,99999999,9999999,404]
        currentmap[playerY][playerX] = 1
        time.sleep(1)
        return
#Dialouge which oc
def dialogue2(): #more talking
    global playeddialogue2
    print("\n*You and Strabi get into the van and Pickle Man drives away*")
    time.sleep(2)
    print("\nStrabi: Quick and easy!")
    time.sleep(2)
    print("\nYou: Yep, now we just have to hide for a while and then the cops wont even remember that this happened")
    time.sleep(5)
    print("\n*The van stops and you all get out and run towards your hidden humble aboad*")
    time.sleep(4)
    print("\n20|12|2016")
    time.sleep(2)
    print("\n*Your phone rings*")
    time.sleep(2)
    answer = askquestion("Pickup?","yes","yes","yeah","yehe")
    time.sleep(1)
    print("\nYou: Hey who's this?")
    time.sleep(2)
    print("\nUnkown Person: I'll tell you in a bit, but do you remember the robbery you did a couple of years ago?")
    time.sleep(5)
    print("\nYou: Yeah. Wait, how do you know about that?")
    time.sleep(3)
    print("\nUnkown Person: I know because I work for the company that you robbed, in fact I dont just work for the company, I own the company")
    time.sleep(5)
    print("\nYou: Ohhh, uhhh")
    time.sleep(2)
    print("\nUnkown Person: Listen, I know this sounds a bit stupid but we want you to work for us,\n we have the most high tech security and the most trained guards and somehow you still got past them. And by the way my name is Scott, Scott the Boss")
    time.sleep(8)
    answer = askquestion("\nJoin Scotts company?","Yeah","YES!","nope (yes)","yehe yehe")
    time.sleep(1)
    print("\nYou: Alright then")
    time.sleep(2)
    print("\nScott: Ok then i'll message you the location of the company building")
    time.sleep(2)
    print("\nThe next day...")
    time.sleep(2)
    playeddialogue2 = True

def dialogue3(): #more talking
    global playeddialogue3, currentmap, playerX, playerY, playeddialogue2, enemysX, enemysY, enemysHealth, playerInventory, exitX, exitY, bossX, bossY
    print("*Scott the boss escorts you to his helicopter*")
    time.sleep(2)
    print("*Helicopter flies over Tokyo*")
    time.sleep(2)
    print("Scott the Boss: I'll drop you three into the enemy base.") 
    time.sleep(2)
    print("Pickle Man: Wait don't we need to pla-")
    time.sleep(2)
    print("Bean: Shut it Pickle we need to focus on our mission")
    time.sleep(2)
    print("Strabi: Bean, I think you need to become nicer")
    time.sleep(2)
    print("Scott the Boss: Ok We're here")
    time.sleep(2)
    print("*Helicopter lands...*")
    time.sleep(3)
    playeddialogue3 = True
    currentmap = Map1 #changes the map and its settings
    playerInventory = []
    playerX = 8
    playerY = 13
    enemysX = [12,13,8,7,6]
    enemysY = [11,12,8,8,8]
    enemysHealth = [50,60,50,50,80]
    exitX = 14
    exitY = 3
    currentmap[exitY][exitX] = 5
    currentmap[playerY][playerX] = 1
    time.sleep(1)

def checkdialogue2(): #checks if the dialogue has been played yet
    if playeddialogue2 == False and currentmap == TutorialMap2:
        dialogue2()

def checkdialogue3(): #same thing
    if playerY == 5 and playeddialogue3 == False and currentmap == TutorialMap2:
        dialogue3()
    
# ----------------------------------------- MAIN LOOP -----------------------------------------
# create the main loop for the program here
tutorial()

while not gameOver:
    checkdialogue2()
    checkdialogue3()
    printBoard()
    PlayerMove()
    checkEnemyHealth()
    moveEnemies()
    checkEnemy()
    checkBoss()
    checkExit()
print('╔══╗                   \n║╔═╬═╗╔══╦═╗╔═╦═╦═╦═╦╦╗\n║╚╗║╬╚╣║║║╩╣║╬╠╗║╔╣╩╣╔╝\n╚══╩══╩╩╩╩═╝╚═╝╚═╝╚═╩╝ ') #prints "GAME OVER"