import random
import time as t
import Info as i
import Save as s

# make enemies harder, but still survivable / add difficulty scaler?
#update saves
"""
ideas:

rename potions to other things for more depth

add a longer description of fights
"""

# prints item name, charges, how many times it can recharges, whether it is being used or not, and its damage boost
def readItemStats():
    if i.playerItems["name"] == None:
        print("You do not have an item equipped at this time.")
    else:
        print(f"You currently have a {i.playerItems["name"]} equipped.\nCharges: {i.playerItems["charge"]}\nRecharges: {i.playerItems["recharges"]}\nCurrently using?: {i.playerItemsState}\nDamage:{i.ItemPowers[int(i.playerItemModifier)]["damage"]}\n")

# resets user's chosen item to none
def itemReset():
    i.playerItems["charge"] = None
    i.playerItems["recharges"] = None
    i.playerItems["name"] = None
    i.playerItemsState = False
    i.playerItemModifier = None

# allows the item to be used to fight
def equipItem():
    i.playerItemsState = True
    print(f"You equipped your {i.playerItems["name"]}!\n\n")

# disables the usage of the item to fight
def unequipItem():
    i.playerItemsState = False
    print(f"You unequipped your {i.playerItems["name"]}!\n\n")

# finds the item and stores it in the user's info
def findItem(itemNumber):
    i.playerItems["charge"] = i.Items[itemNumber]["charge"]
    i.playerItems["recharges"] = i.Items[itemNumber]["recharges"]
    i.playerItems["name"] = i.Items[itemNumber]["name"]
    i.playerItemModifier = random.randint(1,4)

# returns the damage boost
def pwr():
    return i.ItemPowers[int(i.playerItemModifier)]["damage"]

# adds a degrading feature to the item, after a certain amount of time the item will have to recharge and lose a useage level
# also adds a feature to make the item break, using itemReset
def itemDegrade():
    i.playerItems["charge"] -= 1
    if i.playerItems["charge"] == 0:
        i.playerItems["recharges"] -= 1
        if i.playerItems["recharges"] <= 0:
            print(f"Your {i.playerItems["name"]} broke!\n")
            itemReset()
        print("Your item has run out of charges and is now in a recharging state.")
        i.playerItemsState = False
        
# when dormant, the item will recharge. Once recharged, a message will be printed.
def itemRecharge():
    i.playerItems["charge"] += 1
    if i.playerItems["charge"] == 20:
        print(f"Your {i.playerItems["name"]} has reached its charge limit, with {i.playerItems["recharges"]} recharges left.\n")
        print("1. Re-equip\n2. Continue the fight\n")
        choice = input("Your choice: ")
        if choice == "1":
            i.playerItemsState = True
            print("Equipped item.\n")
        elif choice == "2":
            pass
        else:
            print("Please enter a valid choice.\n")
            itemRecharge()

# the function for getting an item from killing an enemy
def replaceItem(a=random.randint(1,4)):
    itemNumber = a
    print(f"You found a {i.Items[itemNumber]["name"]}! It has {i.Items[itemNumber]["charge"]} charges left and {i.Items[itemNumber]["recharges"]} recharges left!")
    print("1. Take it\n2. Leave it\n3. Check your current item's stats\n\nNOTE: If you take the item and you already have an item, the new item will replace the old one.")
    choice = input("Your choice: ")
    if choice == "1":
        findItem(itemNumber)
    elif choice == "2":
        pass
    elif choice == "3":
        
        readItemStats()
        replaceItem(a)
    else:
        print("Please enter a valid choice.\n")
        replaceItem(a)

# full dungeon function, including:
#   - Enemy information
#   - Enemy choosing
#   - potions drinking and obtaining obtaining
#   - attack process for player and enemy
#   - restoring health if lower than 15 health
#   - dungeon check in after every action
#   - function to turn saved information back to integers
def dungeonRun():
    
		# list of enemies, including its health, damage, dodge chance, double hit chance, double loot (will eventually use or remove) and chance of encountering
    enemy = {
        "undead": {"health": random.randint(23,32), "damage": random.randint(2,5), "dodge chance": 13, "double hit chance": 3, "double loot": random.randint(1,4), "chance": 16, "find": 7},
        "bandit": {"health": random.randint(15, 35), "damage": random.randint(4,7), "dodge chance": random.randint(10,23), "double hit chance": random.randint(12,17), "double loot": random.randint(1,3), "chance": 30, "find": 6}, 
        "snake": {"health": random.randint(10,15), "damage": random.randint(1,3), "dodge chance": 35, "double hit chance": 18, "double loot": random.randint(1,4), "chance": 45, "find": 10},
        "undead guard": {"health": random.randint(32,40), "damage": random.randint(6,11), "dodge chance": 17, "double hit chance": random.randint(11,15), "double loot": random.randint(1,2), "chance": 57, "find": 4},
        "giant spider": {"health": random.randint(20,35), "damage": random.randint(3,6), "dodge chance": random.randint(24,34), "double hit chance": random.randint(11,18), "double loot": random.randint(1,2), "chance": 68, "find": 5},
        "giant armored spider": {"health": random.randint(28,40), "damage": random.randint(3,7), "dodge chance": random.randint(19,31), "double hit chance": random.randint(11,16), "double loot": random.randint(1,1), "chance": 77, "find": 4},
        "goblin": {"health": random.randint(10,15), "damage": random.randint(2,5), "dodge chance": random.randint(13,23), "double hit chance": random.randint(13,16), "double loot": random.randint(1,4), "chance": 90, "find": 7},
        "wizard": {"health": random.randint(32,45), "damage": random.randint(7,14), "dodge chance": random.randint(13,16), "double hit chance": random.randint(11,15), "double loot": random.randint(1,1), "chance": 97, "find": 2},
        "King's Guard": {"health": random.randint(45,60), "damage": random.randint(13,17), "dodge chance": random.randint(3,7), "double hit chance": random.randint(11,15), "double loot": random.randint(1,1), "chance": 100, "find": 1},
    }
    baddie = random.randint(1, 100)


    # enemy chooser
    if i.between(baddie, 1, enemy["undead"]["chance"]) ==  True:
        baddieOne = enemy["undead"]
        baddieName = "Zombie"
        drops = 1
    elif i.between(baddie, enemy["undead"]["chance"]+1, enemy["bandit"]['chance']) == True:
        baddieOne = enemy["bandit"]
        baddieName = "Bandit"
        drops =  2
    elif i.between(baddie, enemy["bandit"]["chance"]+1, enemy["snake"]['chance']) == True:
        baddieOne = enemy["snake"]
        baddieName = "Snake"
        drops = 1
    elif i.between(baddie, enemy["snake"]["chance"]+1, enemy["undead guard"]['chance']) == True:
        baddieOne = enemy["undead guard"]
        baddieName = "Undead Guard"
        drops = 3
    elif i.between(baddie, enemy["undead guard"]["chance"]+1, enemy["giant spider"]['chance']) == True:
        baddieOne = enemy["giant spider"]
        baddieName = "Giant Spider"
        drops = 2
    elif i.between(baddie, enemy["giant spider"]["chance"]+1, enemy["giant armored spider"]['chance']) == True:
        baddieOne = enemy["giant armored spider"]
        baddieName = "Giant Armored Spider"
        drops = 3
    elif i.between(baddie, enemy["giant armored spider"]["chance"]+1, enemy["goblin"]['chance']) == True:
        baddieOne = enemy["goblin"]
        baddieName = "Goblin"
        drops = 2
    elif i.between(baddie, enemy["goblin"]["chance"]+1, enemy["wizard"]['chance']) == True:
        baddieOne = enemy["wizard"]
        baddieName = "Wizard"
        drops = 3
    elif i.between(baddie, enemy["wizard"]["chance"]+1, enemy["King's Guard"]['chance']) == True:
        baddieOne = enemy["King's Guard"]
        baddieName = "King's Guard"
        drops = 4
    print(f"You came across a {baddieName}!\n")
    s.updateSave()
    # general dungeon function
    
    dungeonGoing = True
    while dungeonGoing == True:
        # checks if player has enough potions
        def potionChecker(ones, twos):
            if twos > 0:
                twos -=  1
                print(f"You drank 1 {ones}! You have {twos} {ones}s left!\n")
                return twos
            print(f"You're out of {ones}s!\n")

        def check(point):
            num = 0
            for _ in range(4):
                if str(num) == point:
                    return num
                else:
                    num += 1

        # checks if player is out of potions (can merge with potionChecker)
        
        def potionOut(potionName):
            if i.playerPotions[potionName] == "0":
                return False
            return True
        # function for the enemy's attack, including chance of dodging. b is dodge chance boost
        def enemyAttack(b):
            dodgeChance = random.randint(1,100)
            if dodgeChance <= 31 + b:
                print(f"The {baddieName} swung at you, but you dodged!\n")
            else:
                # if the player has 0 or less health and enemy has more than 0 health, the fight will end, player's health will be set to 0 if less than 0
                if i.playerHealth['hp'] > 0 and baddieOne['health'] > 0:
                    i.playerHealth["hp"] -= baddieOne["damage"]

                    if i.playerHealth['hp'] <= 0:
                        i.playerHealth['hp'] = 0
                        print(f"The {baddieName} hit you for {baddieOne['damage']} hp! You died!\n")
                        i.playerHealth['hp'] = 40
                        i.playerPotions["damage-pot"] = 0
                        i.playerPotions["dodge"] = 0
                        i.playerPotions["restoration"] = 5
                        itemReset()
                        s.died()
                        exit()
                    else:
                        print(f"The {baddieName} hit you for {baddieOne['damage']} hp! You have {i.playerHealth['hp']} hp left!")
        
        # same concept as enemyAttack, except the opposite for the fight-end condition. a is damage boost
        
        def playerAttack(a):
            dodgeChance = random.randint(1,100)
            if dodgeChance <= baddieOne['dodge chance']:
                print(f'You swung at the {baddieName}, but it dodged! It has {baddieOne['health']} hp left!')
            else:
                if i.playerHealth['hp'] > 0 and baddieOne['health'] > 0:
                    if i.playerItems["recharges"] == None or i.playerItemsState == False:
                        if i.playerItems["recharges"] is not None and i.playerItemsState == False:
                            itemRecharge()
                        extraDamage = 0 #have it already set to 0 at the beginning, change if anything changes, find a way to take the item name then find its damage
                    else:
                        extraDamage = pwr()
                        itemDegrade()
                    
                    totalDamage = i.playerDamage['damage'] + a + extraDamage

                    baddieOne['health'] -= totalDamage
                    if baddieOne['health'] <= 0:
                        baddieOne['health'] = 0
                        drop = i.findAPotion(drops)
                        if baddieOne["double loot"] == 1:
                            drop2 = i.findAPotion(drops)
                            # stack potions if needed, if second part of message is the same, just add the two, seperate them into their seperate words, then do that
                            drop.split()
                            drop2.split()
                            if drop[1] is drop2[1]:
                                drop = check(drop[0])
                                drop1 = check(drop2[0])
                                drop = str(drop+drop1)+" "+drop2[2:]
                                print(f'You killed the {baddieName}! You got {drop}s!')
                            else:
                                print(f'You killed the {baddieName}! You got {drop} and {drop2}!')
                        else:
                            print(f'You killed the {baddieName}! You got {drop}!')
                        find = random.randint(1, baddieOne["find"])
                        if find == 1:
                            replaceItem()
                        
                        i.playerHealth['hp'] = 40
                        dungeonRun()
                    else:
                        print(f"You hit the {baddieName} for {totalDamage} hp! It now has {baddieOne['health']} hp left!")
        
        
        # fix so you can say no
        # appears if player is at 10 or lower HP
        def restoreHealth():
            if i.playerHealth['hp'] <= 15:
                print("\nYou are at low health.\n1. Drink a restoration potion\n2.Continue the fight\n")
                playerChoice = input("Your choice: ")
                if playerChoice == "1":
                    restor = random.randint(5,15)
                    if restor >= 13:
                        restor += random.randint(0,5)
                    i.playerHealth['hp'] += restor
                    
                    print(f"You restored {restor} hp! You now have {i.playerHealth['hp']} hp!\n")
                    i.playerPotions['restoration'] = potionChecker("Restoration Potion", i.playerPotions['restoration'])
                elif playerChoice == "2":
                    pass
                else:
                    print("Please enter a valid choice\n")
                    restoreHealth()
                    
        # turned the process for drinking potions into a function, checks to see if player has the potions then adds the bonus to
        # the player's stats, then prints the usage of the potions
        def drinkPotions():
            
            print(f"You have {i.playerPotions["damage-pot"]} Damage Up potions, {i.playerPotions["dodge"]} Dodge Chance Up potions, and {i.playerPotions["restoration"]} Restoration potions")
            print("1. Drink a Damage Up Potion\n2. Drink a Dodge Chance Up Potion\n3. Drink a Restoration Potion\n4. Go back to the Attack Menu\n")   
            print("Note that boosting potions last for 1 attack.\n")
            playerChoice = input("\n")
            
            if playerChoice == "1":
                if potionOut(i.potionNamesReal[0]) == True:
                    i.playerBoosts["damage up"] = random.randint(3,6)
                    print("You boosted your damage by "+str(i.playerBoosts["damage up"])+" points!\n")
                i.playerPotions['damage-pot'] = int(potionChecker("Damage Potion", i.playerPotions['damage-pot']))

            elif playerChoice == "2":
                if potionOut(i.potionNamesReal[1]) == True:
                    i.playerBoosts["dodge up"] = random.randint(5,9)
                    print("You boosted your dodge stat by "+str(i.playerBoosts["dodge up"])+" points!\n")
                i.playerPotions['dodge'] = int(potionChecker("Dodge Up Potion", i.playerPotions['dodge']))

            elif playerChoice == "3": 
                if potionOut(i.potionNamesReal[2]) == True:
                    restor = random.randint(5,15)
                    if restor >= 13:
                        restor += random.randint(0,5)
                    i.playerHealth['hp'] += restor
                    print(f"You restored {restor} hp! You now have {i.playerHealth['hp']} hp!\n")
                i.playerPotions['restoration'] = int(potionChecker("Restoration Potion", i.playerPotions['restoration']))
                
            elif playerChoice == "4":
                dungeonCheckIn()

            else:
                print("Please enter a valid choice.\n")
                drinkPotions()
        
        # turns information saved from loading the save file
        def turnInt():
            i.playerPotions["damage-pot"] = int(i.playerPotions["damage-pot"])
            i.playerPotions["dodge"] = int(i.playerPotions["dodge"])
            i.playerPotions["restoration"] = int(i.playerPotions["restoration"])
            if i.playerItems["name"] == "None" or i.playerItems["name"] is None:
                pass
            else:
                i.playerItems["charge"] = int(i.playerItems["charge"])
                i.playerItems["recharges"] = int(i.playerItems["recharges"])
                i.playerItemModifier = int(i.playerItemModifier)

        # appears after each instance of attacking, options are to drink a potion or to attack
        def dungeonCheckIn():
            turnInt()
            print("1. Attack\n2. Drink a potion\n3. Equip or unequip your weapon\n4. Check item\n5. Go to menu\n")
            playerChoice = input("Your choice: ")
            # resets boosts to 0
            i.playerBoosts["damage up"] = 0
            i.playerBoosts["dodge up"] = 0
            if playerChoice == "2": #wont allow u to attack
                drinkPotions()
            # attack just goes through both enemy and player attacks   
            elif playerChoice == "1":
                print()
                def attackStuff (x, y):
                    for _ in range(x):
                        playerAttack(i.playerBoosts["damage up"])
                    for _ in range(y):
                        enemyAttack(i.playerBoosts["dodge up"])
                    print()
                    dungeonCheckIn()
                    
                doubleHit = random.randint(1,100)
                
                restoreHealth()
                
                #chooses whether player or enemy will have double attacks
                if i.playerDoubleHitRate["double hit chance"] <= doubleHit and baddieOne["double hit chance"] > doubleHit:
                    attackStuff(2, 1)
                elif baddieOne["double hit chance"] <= doubleHit and i.playerDoubleHitRate["double hit chance"] > doubleHit:
                    attackStuff(1, 2)
                elif baddieOne["double hit chance"] >= doubleHit and i.playerDoubleHitRate["double hit chance"] >= doubleHit:
                    attackStuff(2, 2)
                else:
                    attackStuff(1, 1)
            elif playerChoice == "3":
                if i.playerItemsState == False:
                    equipItem()
                else:
                    unequipItem()
            elif playerChoice == "4":
                readItemStats()
                dungeonCheckIn()
            elif playerChoice == "5":
                print()
                mainScreen()
            else:
                print("Please enter a valid choice.\n")
                dungeonCheckIn()
                    
        
        dungeonCheckIn()

                
# main menu function
def mainScreen():
    print()
    print("1. Load a save\n2. Create a new save\n3. Continue\n4. Open guide menu\n5. Exit\n\nNOTE: Making a new save will overwrite your old save. It will delete all progress made.")
    choice = input("Your choice: ")
    if choice == "1":
        s.loadSave()
        print(f"You loaded the previous save.\n")
        
        dungeonRun()
    elif choice == "2":
        s.newSave()
        
        dungeonRun()
    elif choice == "3":
        
        dungeonRun()
    elif choice == "4":
        i.guideMenu()
        mainScreen()
    elif choice == "5":
        exit()
    else:
        print("Please enter a valid choice.\n")
        mainScreen()

mainScreen()
