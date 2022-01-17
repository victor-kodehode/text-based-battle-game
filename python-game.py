# used to randomize the enemy's properties and attacks
from random import randint

battles = 0 # total battles fought
wonBattles = 0 # total battles won
battleTurn = 0
hasDied = False # player alive/dead status

# the player
class Player:
    # properties of the player
    def __init__(self,health,maxHealth,defense,attack,magic,maxMagic):
        self.health = health
        self.maxHealth = maxHealth
        self.defense = defense
        self.attack = attack
        self.magic = magic
        self.maxMagic = maxMagic
    # if you want to do nothing
    def nothing(self):
        pass
    # if you want to recover
    def recover(self):
        newHealth = self.health
        newHealth += 5
        if (newHealth > self.maxHealth):
            return self.maxHealth
        else:
            return newHealth
    # if you want to use physical attack
    def physicalAttack(self,enemy):
        if (enemy.defense >= self.attack):
            return 1
        else:
            return (self.attack - enemy.defense)
    # if you want to use magic attack
    def magicAttack(self,enemy):
        return int(0.25*enemy.health)
    # if you want to run away
    def runAway(self):
        if (randint(1,2) == 1):
            return True
        else:
            return False

# the enemy
class Enemy:
    # properties of the enemy
    def __init__(self,health,maxHealth,defense,attack,magic,maxMagic):
        self.health = health
        self.maxHealth = maxHealth
        self.defense = defense
        self.attack = attack
        self.magic = magic
        self.maxMagic = maxMagic
    # sometimes it chooses to do nothing
    def nothing(self):
        pass
    # sometimes it chooses to recover health before continuing the fight
    def recover(self):
        newHealth = self.health
        newHealth += 5
        if (newHealth > self.maxHealth):
            return self.maxHealth
        else:
            return newHealth
    # sometimes it chooses to attack
    def physicalAttack(self,player):
        if (player.defense >= self.attack):
            return 1
        else:
            return (self.attack - player.defense)
    # sometimes it chooses to attack with magic
    def magicAttack(self,player):
        return int(0.25*player.health)
    # sometimes it chooses to run away
    def runAway(self):
        if (randint(1,2) == 1):
            return True
        else:
            return False

def newEnemy(): # creates a new enemy
    randomHealth = randint(1,10) # can't spawn an enemy with 0 health
    randomMaxHealth = randomHealth # max health is the same as health to begin with
    randomDefense = randint(0,10) # some enemies are defenseless
    randomAttack = randint(1,10) # can't spawn an enemy with 0 attack
    randomMagic = randint(0,10) # some enemies don't use magic
    randomMaxMagic = randomMagic # max magic is the same as magic to begin with
    randomEnemy = Enemy(randomHealth,randomMaxHealth,randomDefense,randomAttack,randomMagic,randomMaxMagic) # enemy created
    return randomEnemy

# creating player and enemy
# health, maxHealth, defense, attack, magic, maxMagic
player = Player(10,10,10,10,10,10)
enemy = newEnemy() # create a new enemy

# enemy drawings
def enemyState(state):
    if (state == 0):
        print("       ___  ")
        print("      |o_o| ")
        print("   ___|___| ") # normal
        print("  /____/    ")
        print(" / \ / \    ")
    elif (state == 1):
        print("      _\_/_ ")
        print("      |O_O| ")
        print("   ___|___| ") # aggressive
        print("  /____/    ")
        print(" / \ / \    ")
    elif (state == 2):
        print("    *  ___  ")
        print("   *  |x_x| ")
        print("*  ___|___| ") # hurt
        print("  /____/  * ")
        print(" / \ / \    ")
    elif (state == 3):
        print("             ")
        print("       ___   ")
        print("  ____/x_x\  ") # dead
        print(" /___/_____\ ")
    else:
        print("       ___  ")
        print("      |o_o| ")
        print("   ___|___| ") # normal (default if "state" is some other number)
        print("  /____/    ")
        print(" / \ / \    ")

# simple functions to print out text
def mainMenu():
    print("\nMAIN MENU")
    print("[1] game progress   [2] player stats")
    print("[3] continue game   [4] end game    ")

def gameProgress():
    print("\nPROGRESS")
    print(f"Number of battles: {battles}")
    print(f"Number of won battles: {wonBattles}")

def playerStats():
    print("\nPLAYER STATS")
    print(f"health: {player.health}/{player.maxHealth}") # example: "health: 42/100"
    print(f"defense: {player.defense}")
    print(f"attack: {player.attack}")
    print(f"magic: {player.magic}/{player.maxMagic}")

def enemyStats():
    print("\nENEMY STATS")
    print(f"health: {enemy.health}/{enemy.maxHealth}")
    print(f"defense: {enemy.defense}")
    print(f"attack: {enemy.attack}")
    print(f"magic: {enemy.magic}/{enemy.maxMagic}")

def battleMenu():
    print("\nBATTLE MENU")
    print("[1] player stats    [2] enemy stats   ")
    print("[3] do nothing      [4] recover health")
    print("[5] physical attack [6] magic attack  ")
    print("[7] run away                          ")

# the battle itself
def battleSequence():
    turn = -1 # will be 0 or higher inside the battle loop

    # variables for the runAway function
    hasEscaped = False # used to break out of the battle loop
    escapeValid = True # can only attempt to run away once, second time it will not be valid
    enemyValidEscape = True # same is true for the enemy
    while(True): # the battle loop
        turn += 1 # turn 0 ... turn 1 ...
        enemyState(0) # see drawings above
        if (turn == 0):
            print("enemy draws near")
        else:
            print("enemy respectfully awaits your move") # enemies in turn based battles are very polite
        while(True): # the player decision loop
            battleMenu()
            choice = input("choose: ")
            if (choice == "1"): # player stats, still the same turn
                enemyState(0)
                playerStats()
                continue
            if (choice == "2"): # enemy stats, still the same turn
                enemyState(0)
                enemyStats()
                continue
            if (choice == "3"): # do nothing, go to enemy turn
                enemyState(0)
                player.nothing() # doesn't do anything
                print("\nplayer did nothing...")
                break
            if (choice == "4"): # recover health, go to enemy turn
                enemyState(0)
                oldHealth = player.health # saving health before recovery, to get the difference
                player.health = player.recover()
                print("\nplayer recovered health!")
                print(f"regained {player.health - oldHealth} health") # print the difference "regained 5 health" for example
                break
            if (choice == "5"): # physical attack, go to enemy turn
                enemyState(2)
                oldHealth = enemy.health # same here, old health used to get the difference
                enemy.health -= player.physicalAttack(enemy) # enemy loses health
                print("\nplayer attacked the enemy!")
                print(f"enemy lost {oldHealth - enemy.health} health")
                break
            if (choice == "6"): # magic attack, go to enemy turn
                if (player.magic > 0):
                    enemyState(2)
                    oldHealth = enemy.health
                    enemy.health -= player.magicAttack(enemy)
                    print("\nplayer attacked the enemy with magic!")
                    print(f"enemy lost {oldHealth - enemy.health} health")
                    break
                else: # can't use magic attack without magic
                    enemyState(0)
                    print("\nplayer attemps to attack the enemy with magic, but the player has no magic!")
                    break
            if (choice == "7"): # run away, go to main menu
                print("\nplayer attempts to run away!")
                if (escapeValid == False): # can't fool the enemy twice, you are no longer allowed to run
                    enemyState(1)
                    print("enemy is angered by your repeated attempts to escape...")
                    print("your only option is to fight")
                    break
                elif (player.runAway() == False): # failed attempt to run away
                    enemyState(1)
                    print("enemy catches up to you...")
                    escapeValid = False # escape no longer allowed
                    break
                else: # successfully runs away
                    print("player successfully runs away!")
                    hasEscaped = True # you have escaped
                    break
            else: # invalid input
                print("\n Invalid input.")
                continue
        if (hasEscaped == True): # if you ran away, end the battle loop
            return 1 # "1" means battle forfeit, no win for you
        if (enemy.health <= 0):
            enemyState(3)
            return 0 # "0" means victory, yay!
        input("press enter to continue...")

        # enemy's turn
        randomEnemyChoice = randint(1,5)
        if (randomEnemyChoice == 1): # nothing, go to player turn
            enemyState(0)
            enemy.nothing()
            print("\nenemy does nothing...")
        elif (randomEnemyChoice == 2): # recover health, go to player turn
            enemyState(0)
            oldHealth = enemy.health # same as for the player, old value saved to get the difference
            enemy.health = enemy.recover()
            print("\nenemy recovered health!")
            print(f"regained {enemy.health - oldHealth} health")
        elif (randomEnemyChoice == 3): # physical attack, go to player turn
            enemyState(1)
            oldHealth = player.health
            player.health -= enemy.physicalAttack(player)
            print("\nenemy attacks you!")
            print(f"player lost {oldHealth - player.health} health")
        elif (randomEnemyChoice == 4): # magic attack, go to player turn
            if (enemy.magic > 0):
                enemyState(1)
                oldHealth = player.health
                player.health -= enemy.magicAttack(player)
                enemy.magic -= (oldHealth - player.health)
                if (enemy.magic < 0):
                    enemy.magic = 0
                print("\nenemy uses magic attack!")
                print(f"player lost {oldHealth - player.health} health")
            else: # can't use magic attack if it doesn't have magic
                enemyState(0)
                print("\nenemy attempts to use magic attack, but it has no magic!")
        elif (randomEnemyChoice == 5): # enemy tries to run away
            print("\nenemy attempts to run away!")
            if (enemy.runAway() == True and enemyValidEscape == True): # chance to run away is 50%, and only valid 1st attempt
                print("enemy escaped!")
                return 0
            else: # enemy couldn't run away
                enemyValidEscape = False
            print("enemy failed to run away...")
        if (player.health <= 0): # if player is dead, stop the battle loop
            return -1 # "-1" means game over
        input("press enter to continue...")


print("\nGAME START")
print("rule of the game: survive as many enemies as you can")

# main game loop
while(True):
    mainMenu()
    choice = input("choose: ").upper()
    if (choice == "1"): # game progress, battles fought, battles won
        gameProgress()
        continue
    elif (choice == "2"): # player stats
        playerStats()
        continue
    elif (choice == "3"): # continue game, start the battle loop
        enemy = newEnemy() # create a new enemy
        print("\n!!! BATTLE !!!")
        battleResult = battleSequence() # store the result of the battle in a variable
        if (battleResult == 0): # you win the battle, +1 battle, +1 win!
            print("\nplayer has won the battle!")
            wonBattles += 1
            battles += 1
        elif (battleResult == 1): # you ran away from the battle, +1 battle
            battles += 1
        elif (battleResult == -1): # you died, game over
            hasDied = True
            break
        continue
    elif (choice == "4"): # end game
        print("\nPlayer has chosen to stop the fighting.")
        break
    else: # invalid input, try again
        print("\nInvalid input.")
        continue
print("\n") # just some spacing
if (hasDied == True): # if you died, print this (because you can stop the game without dying too)
    print("You have died.")

print("final stats:")
print(f"battles: {battles}")
print(f"victories: {wonBattles}")
print("Thank you for playing.")