import random
import os
import msvcrt
playerHealth = 100
playerPositionX = 0
playerPositionY = 0
goalPositionX = 0
goalPositionY = 0
healthPositionX = 0
healthPositionY = 0
healthPositionX2 = 0
healthPositionY2 = 0
dificulty=0


enemiesX=[]
enemiesY=[]
enemySpawned=False
isThereClash=True
isGameOver = False


directionToMove = ""
isGameRunning = True
gridSymbol = "\033[1;37;40m #"
playerSymbol = "\033[1;34;40m O"
goalSymbol = "\033[1;33;40m X"
enemySymbol = "\033[1;31;40m E"
healthSymbol = "\033[1;32;40m +"






def isMoveValidUp(coord):  #checks if is out of bound in positive direction
    if coord+1 >19:
        return False
    else:
        return True

def isMoveValidDown(coord): #checks if move is out of bound in negative direction
    if coord-1 <0:
        return False
    else:
        return True
    

def isEnemyClashing(coordX,coordY,j): #Checks if enemy position is clashing with any other symbols
    global enemiesX
    global enemiesY
    global goalPositionX
    global goalPositionY
    global healthPositionX
    global healthPositionY
    global healthPositionX2
    global healthPositionY2
    if coordX==goalPositionX and coordY==goalPositionY:
        return True
    elif coordX==healthPositionX and coordY==healthPositionY:
        return True
    elif coordX==healthPositionX2 and coordY==healthPositionY2:
        return True
    for i in range(len(enemiesY)):
        if enemiesX[i]==coordX and enemiesY[i]== coordY and i!=j:
            return True
    return False





def moveEnemy():  #randomly moves the enemy one square
    global enemiesX
    global enemiesY
    for i in range(len(enemiesY)):
        movmentPosition = random.randint(1,4)
        if movmentPosition==1:
            if isMoveValidDown(enemiesY[i])==True:
                if isEnemyClashing(enemiesX[i],enemiesY[i]-1,100)==False:
                    enemiesY[i]-=1
        elif movmentPosition==2:
           if isMoveValidDown(enemiesX[i])==True:
                if isEnemyClashing(enemiesX[i]-1,enemiesY[i],100)==False:
                    enemiesX[i]-=1
        elif movmentPosition==3:
            if isMoveValidUp(enemiesY[i])==True:
                if isEnemyClashing(enemiesX[i],enemiesY[i]+1,100)==False:
                    enemiesY[i]+=1
        elif movmentPosition==4:
            if isMoveValidUp(enemiesX[i])==True:
                if isEnemyClashing(enemiesX[i]+1,enemiesY[i],100)==False:
                    enemiesX[i]+=1


def respawnEnemy(i):  #respawns enemys
    global playerHealth
    global isThereClash
    global enemiesX
    global enemiesY
    playerHealth-=10
    isThereClash = True
    while isThereClash == True:
        enemiesX[i]=random.randint(0,19)
        enemiesY[i]=random.randint(0,19)
        isThereClash = isEnemyClashing(enemiesX[i],enemiesY[i],i)

def setDificulty(): #sets the dificulty depending on input
    validDifficulty=False
    while validDifficulty==False:
        print("Please select your required dificulty")
        print("Enter 1 for easy")
        print("Enter 2 for medium")
        print("Enter 3 for hard")
        print("Enter 4 for extreme")
        dificulty = msvcrt.getch()
        if dificulty== b"1":
            spawnEverything(5)
            validDifficulty=True
        elif dificulty==b"2":
            spawnEverything(10)
            validDifficulty=True
        elif dificulty==b"3":
            spawnEverything(15)
            validDifficulty=True
        elif dificulty==b"4":
            spawnEverything(20)
            validDifficulty=True
        else:
            print("That is an invalid difficulty.")



def spawnEverything(enemyAmount): #sets all variables to their coordinates on the grid
    global playerPositionX
    global playerPositionY
    global goalPositionX
    global goalPositionY
    global healthPositionX
    global healthPositionY
    global healthPositionX2
    global healthPositionY2
    global enemiesX
    global enemiesY
    global isThereClash
    global playerHealth
    isThereClash=True
    enemiesX=[]
    enemiesY=[]
    playerHealth=100
    playerPositionX = random.randint(0,19)
    playerPositionY = random.randint(0,19)
    goalPositionX = random.randint(0,19)
    goalPositionY = random.randint(0,19)
    while isThereClash == True:
        if playerPositionX == goalPositionX and playerPositionY==goalPositionY:
             goalPositionX = random.randint(0,19)
             goalPositionY = random.randint(0,19)
        else:
            isThereClash=False
    isThereClash=True
    healthPositionX=random.randint(0,19)
    healthPositionY=random.randint(0,19)
    while isThereClash==True:
        if playerPositionX == healthPositionX and playerPositionY == healthPositionY:
             healthPositionX=random.randint(0,19)
             healthPositionY=random.randint(0,19)
        elif goalPositionX==healthPositionX and goalPositionY==healthPositionY:
            healthPositionX=random.randint(0,19)
            healthPositionY=random.randint(0,19)
        else:
            isThereClash=False
    isThereClash=True
    healthPositionX2=random.randint(0,19)
    healthPositionY2=random.randint(0,19)
    while isThereClash == True:    
        if playerPositionX == healthPositionX2 and playerPositionY == healthPositionY2:
             healthPositionX2=random.randint(0,19)
             healthPositionY2=random.randint(0,19)
        elif goalPositionX==healthPositionX2 and goalPositionY==healthPositionY2:
            healthPositionX2=random.randint(0,19)
            healthPositionY2=random.randint(0,19)
        elif healthPositionX==healthPositionX2 and healthPositionY==healthPositionY2:
            healthPositionX2=random.randint(0,19)
            healthPositionY2=random.randint(0,19)
        else:
            isThereClash=False
    for i in range(enemyAmount):
        enemiesX.append(random.randint(0,19))
        enemiesY.append(random.randint(0,19))
        for j in range(len(enemiesY)):
            isThereClash = True
            while isThereClash==True:
                if enemiesX[i] == playerPositionX and enemiesY[i] == playerPositionY:
                    enemiesX.pop
                    enemiesY.pop
                    enemiesX.append(random.randint(0,19))
                    enemiesY.append(random.randint(0,19))
                elif enemiesX[i] == goalPositionX and enemiesY[i] == goalPositionY:
                    enemiesX.pop
                    enemiesY.pop
                    enemiesX.append(random.randint(0,19))
                    enemiesY.append(random.randint(0,19))
                elif enemiesX[i] == healthPositionX and enemiesY[i] == healthPositionY:
                    enemiesX.pop
                    enemiesY.pop
                    enemiesX.append(random.randint(0,19))
                    enemiesY.append(random.randint(0,19))
                elif enemiesX[i] == healthPositionX2 and enemiesY[i] == healthPositionY2:
                    enemiesX.pop
                    enemiesY.pop
                    enemiesX.append(random.randint(0,19))
                    enemiesY.append(random.randint(0,19))
                elif enemiesX[i] == enemiesX[j] and enemiesY[i]==enemiesY[j] and i!=j:
                    enemiesX.pop
                    enemiesY.pop
                    enemiesX.append(random.randint(0,19))
                    enemiesY.append(random.randint(0,19))
                else:
                    isThereClash=False
            isThereClash = True
            while isThereClash == True:
                enemiesX[i]=random.randint(0,19)
                enemiesY[i]=random.randint(0,19)
                isThereClash = isEnemyClashing(enemiesX[i],enemiesY[i],i)

            
def checkForHealth(): #checks if player is on a healthpack and adds health if so
    global playerPositionX
    global playerPositionY
    global healthPositionX
    global healthPositionY
    global playerHealth
    global healthPositionX2
    global healthPositionY2
    if playerPositionX==healthPositionX and playerPositionY==healthPositionY:
        playerHealth+=10
        healthPositionX=100
    elif playerPositionX==healthPositionX2 and playerPositionY==healthPositionY2:
        playerHealth+=10
        healthPositionX2=100

def checkEnemyAttack(): #checks if enemy is within one square of player and attacks if so
    global playerPositionX
    global playerPositionY
    global enemiesX
    global enemiesY
    global playerHealth
    for i in range(len(enemiesY)):
        if playerPositionX == enemiesX[i] and playerPositionY==enemiesY[i]:
            respawnEnemy(i)

        elif playerPositionX == enemiesX[i]+1 and playerPositionY==enemiesY[i]:
            
            respawnEnemy(i)
        elif playerPositionX==enemiesX[i]-1 and playerPositionY==enemiesY[i]:
            
            respawnEnemy(i)
        elif playerPositionX==enemiesX[i] and playerPositionY==enemiesY[i]+1:
            
            respawnEnemy(i)
        elif playerPositionX==enemiesX[i] and playerPositionY==enemiesY[i]-1:
            
            respawnEnemy(i)

def restart():  #restarts the game if the player chooses
    global isGameOver
    print("Would you like to play again? y/n")
    validInput = False
    while validInput == False:
        playAgain = msvcrt.getch()
        if playAgain == b"y":
            isGameOver = False
            validInput = True
        elif playAgain == b"n":
            isGameOver = True
            validInput = True
        else:
            print("Input invalid please enter y/n")

def checkForWin(): #Checks to see if player has reached the goal
    global playerPositionX
    global playerPositionY
    global goalPositionX
    global goalPositionY
    global isGameRunning
    if playerPositionX==goalPositionX and playerPositionY==goalPositionY:
        print("\033[1;37;40m GAME OVER")
        print("Congratulations, You have won!")
        restart()
        isGameRunning = False

def checkForDeath(): #checks to see if players health is brlow 0 and ends game if so
    global playerHealth
    global isGameRunning
    if playerHealth<=0:
        print("\033[1;37;40m GAME OVER")
        print("YOU LOST")
        restart()
        isGameRunning=False


def movePlayer(): #Moves the player based on input
    global playerHealth
    global playerPositionX
    global playerPositionY
    directionToMove = msvcrt.getch()
    if directionToMove == b"w" and isMoveValidDown(playerPositionX) == True:
        playerPositionX -=1
        playerHealth -= 1
    elif directionToMove == b"s" and isMoveValidUp(playerPositionX) == True:
        playerPositionX +=1
        playerHealth -= 1
    elif directionToMove == b"a" and isMoveValidDown(playerPositionY) == True:
        playerPositionY -= 1
        playerHealth -= 1
    elif directionToMove == b"d" and isMoveValidUp(playerPositionY) == True:
        playerPositionY +=1
        playerHealth -= 1

def printGrid(): #prints the grid with the symbols in correct coordinates
    global enemySpawned
    global enemiesX
    global enemiesY
    global enemySymbol
    global playerPositionY
    global playerPositionX
    global playerSymbol
    global goalPositionX
    global goalPositionY
    global goalSymbol
    global healthPositionX
    global healthPositionY
    global healthPositionX2
    global healthPositionY2
    global healthSymbol
    global gridSymbol
    
    for x in range(20):
        for y in range (20):
            enemySpawned=False
            for i in range(len(enemiesY)):
                if enemiesX[i] == x and enemiesY[i] == y:
                    print(enemySymbol,end=" ")
                    enemySpawned=True
            if enemySpawned==False:

                if x == playerPositionX and y == playerPositionY:
                    print(playerSymbol,end=" ")
                elif x == goalPositionX and y == goalPositionY:
                     print(goalSymbol,end=" ")
                elif x == healthPositionX and y == healthPositionY:
                     print(healthSymbol,end=" ")
                elif x == healthPositionX2 and y == healthPositionY2:
                     print(healthSymbol,end=" ")
                else:
                    print(gridSymbol,end=" ")
        print()      
        enemySpawned=False   

    
def main():
    global isGameRunning
    global playerHealth
    global isGameOver
    while isGameOver == False:
        isGameRunning=True
        os.system("cls")
        setDificulty()
        while isGameRunning == True:
            os.system("cls")
            print("\033[1;37;40m Please use wasd to move")
            printGrid()
            print("\033[1;37;40m Player health: " + str(playerHealth))
            movePlayer()
            moveEnemy()
            checkEnemyAttack()
            checkForHealth()
            checkForDeath()
            checkForWin()



main()
