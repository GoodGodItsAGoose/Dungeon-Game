import random
import time as t
import Info as i
import Save as s

# make enemies harder, but still survivable / add difficulty scaler?
#update saves

"""

if [armorName] == None:
	print("no armor")
else:
	print(armorName)

"""

"""
ideas:


RUN THROUGH LEGGINGS, ARMBANDS, AND CHESTPLATES AND PRINT WHAT IS THERE AND WHAT IS NOT
TEST LEVELING UP
TEST ARMOR RATING
TEST GATHERING ARMOR AND USING IT



rename potions to other things for more depth

story bits "You traveled further down the tunnels and turned a corner, coming across a {enemyname}!"

attack > menu > continue creates a new enemy (make it so it doesnt)

add a longer description of fights

level up system with benefited health, damage, dodge up, but also stronger enemies (can add level locked items)
"""

# prints item name, charges, how many times it can recharges, whether it is being used or not, and its damage boost
def readItemStats(a, armorType=1, armorNumber=1):
    t.sleep(0.1)
    if a == 1:
        if i.playerItems["name"] == None:
            print()
            print("You do not have an item equipped at this time.\n")
        else:
            print()
            print(f"You currently have a {i.playerItems["name"]} equipped.\nCurrent Charge Level: {i.playerItems["charge"]}\nRecharges: {i.playerItems["recharges"]}\nCurrently using?: {i.playerItemsState}\nDamage: {i.ItemPowers[int(i.playerItemModifier)]["damage"]}\nMax Charge Level: {i.playerItems["max charges"]}\n")
    else:
        if i.playerStats[s.armor[armorType-1]]["name"] == None:
            print()
            print(f"You are not currently wearing any {s.armor[armorType-1]} at this time.\n")
        else:
            print()
            print(f"You currently are wearing a {i.playerStats[s.armor[armorType-1]]["name"]}.\nArmor Durability: {i.playerStats[s.armor[armorType-1]]["durability"]}\nArmor Rating: {i.playerStats[s.armor[armorType-1]]["rating"]}")

# resets user's chosen item to none
def itemReset(armor=1):
    if armor == 1:
        i.playerItems["charge"] = None
        i.playerItems["recharges"] = None
        i.playerItems["name"] = None
        i.playerItems["max charges"] = None
        i.playerItemsState = False
        i.playerItemModifier = None
    else:
        s.armorCheck(2)

# allows the item to be used to fight
def equipItem():
    if i.playerItems["name"] == None:
        print()
        print("You do not have an item able to be equipped or unequipped at this time.\n")
    else:
        t.sleep(0.1)
        i.playerItemsState = True
        print(f"You equipped your {i.playerItems["name"]}!\n\n")

# disables the usage of the item to fight
def unequipItem():
    if i.playerItems["name"] == None:
        print()
        print("You do not have an item able to be equipped or unequipped at this time.\n")
    else:
        t.sleep(0.1)
        i.playerItemsState = False
        print(f"You unequipped your {i.playerItems["name"]}!\n\n")

# finds the item and stores it in the user's info
def findItem(itemNumber=None, itemModifier=random.randint(1,4), armor=1, armorType=1, armorNumber=1):
    if armor == 1:
        i.playerItems["charge"] = i.Items[itemNumber]["charge"]
        i.playerItems["recharges"] = i.Items[itemNumber]["recharges"]
        i.playerItems["name"] = i.Items[itemNumber]["name"]
        i.playerItems["max charges"] = i.Items[itemNumber]["max charges"]
        i.playerItemModifier = itemModifier
    else:
        if i.Armor[armorType][armorNumber]["level req"] <= i.playerLevel:
            pass
        else:
            num = 0
            for _ in range(3):
                s.armorCheck(i.playerStats[s.armor[num]])

# returns the damage boost
def pwr():
    return i.ItemPowers[int(i.playerItemModifier)]["damage"]

# adds a degrading feature to the item, after a certain amount of time the item will have to recharge and lose a useage level
# also adds a feature to make the item break, using itemReset
def itemDegrade(armor=1, armorType=1, armorNumber=1):
    if armor == 1:
        t.sleep(0.1)
        i.playerItems["charge"] -= 1
        if i.playerItems["charge"] == 0:
            i.playerItems["recharges"] -= 1
            if i.playerItems["recharges"] <= 0:
                print("\n-------\n")
                t.sleep(0.2)
                print(f"Your {i.playerItems["name"]} broke!\n")
                t.sleep(0.5)
                print("-------\n")
                t.sleep(0.3)
                itemReset()
            else:
                print("Your item has run out of charges and is now in a recharging state.")
                i.playerItemsState = False
    else:
        i.playerStats[s.armor[armorType-1]]["durability"] -= 1
        if i.playerStats[s.armor[armorType-1]]["durability"] <= 0:
            print("\n-------\n")
            t.sleep(0.2)
            print(f"Your {i.playerStats[s.armor[armorType-1]]["name"]} broke!\n")
            t.sleep(0.5)
            print("-------\n")
            t.sleep(0.3)
            itemReset()
        
# when dormant, the item will recharge. Once recharged, a message will be printed.
def itemRecharge():
    i.playerItems["charge"] += 1
    t.sleep(0.1)
    if i.playerItems["charge"] == i.playerItems["max charges"]:
        print()
        print(f"Your {i.playerItems["name"]} has reached its max charge level of {i.playerItems["max charges"]} charges. It has {i.playerItems["recharges"]} recharges left.\n")
        print("1. Re-equip\n2. Continue the fight\n")
        choice = input("Your choice: ")
        if choice == "1":
            t.sleep(0.1)
            i.playerItemsState = True
            print("Equipped item.\n")
        elif choice == "2":
            pass
        else:
            t.sleep(0.1)
            print("Please enter a valid choice.\n")
            itemRecharge()

# the function for getting an item from killing an enemy
def replaceItem(a=random.randint(1,4), armorType=random.randint(1,3), armorNumber=random.randint(1,5), armor=1):
    if armor == 1:
        itemNumber = a
        itemModifier = random.randint(1,4)

    t.sleep(0.1)
    if armor == 1:
        print(f"You found a {i.Items[itemNumber]["name"]}! It has {i.Items[itemNumber]["charge"]} charges left and {i.Items[itemNumber]["recharges"]} recharges left. It does {i.ItemPowers[itemModifier]["damage"]} extra damage.")
    else:
        if i.Armor[armorType][armorNumber]["level req"] <= i.playerStats["level"]:
            print(f"You found a {i.Armor[armorType][armorNumber]["name"]}! It has {i.Armor[armorType][armorNumber]["rating"]} armor rating and {i.Armor[armorType][armorNumber]["durability"]} durability left.")
        else:
            pass
    print("1. Take it\n2. Leave it\n3. Check your current item's stats\n\nNOTE: If you take the item and you already have an item, the new item will replace the old one.")
    choice = input("Your choice: ")
    print()
    if choice == "1":
        t.sleep(0.1)
        print("Collected item.")
        print()
        t.sleep(0.1)
        findItem(itemNumber, itemModifier)
    elif choice == "2":
        pass
    elif choice == "3":
        t.sleep(0.1)
        readItemStats()
        if armor == 1:
            replaceItem(a)
        else:
            replaceItem(None, None, 2, armorType, armorNumber)
    else:
        t.sleep(0.1)
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
        "undead": {"health": random.randint(23,32), "damage": random.randint(2,5), "dodge chance": 13, "double hit chance": 3, "double loot": random.randint(1,4), "chance": 16, "find": 7, "exp": random.randint(7,17)},
        "bandit": {"health": random.randint(15, 35), "damage": random.randint(6,8), "dodge chance": random.randint(10,23), "double hit chance": random.randint(12,17), "double loot": random.randint(1,3), "chance": 30, "find": 6, "exp": random.randint(10,20)}, 
        "snake": {"health": random.randint(10,15), "damage": random.randint(2,4), "dodge chance": 35, "double hit chance": 18, "double loot": random.randint(1,4), "chance": 45, "find": 10, "exp": random.randint(3,7)},
        "undead guard": {"health": random.randint(32,40), "damage": random.randint(6,11), "dodge chance": 17, "double hit chance": random.randint(11,15), "double loot": random.randint(1,2), "chance": 57, "find": 4, "exp": random.randint(15,25)},
        "giant spider": {"health": random.randint(20,35), "damage": random.randint(6,8), "dodge chance": random.randint(24,34), "double hit chance": random.randint(11,18), "double loot": random.randint(1,2), "chance": 68, "find": 5, "exp": random.randint(10,20)},
        "giant armored spider": {"health": random.randint(28,40), "damage": random.randint(6,10), "dodge chance": random.randint(19,31), "double hit chance": random.randint(11,16), "double loot": random.randint(1,1), "chance": 77, "find": 4, "exp": random.randint(13,22)},
        "goblin": {"health": random.randint(10,15), "damage": random.randint(3,6), "dodge chance": random.randint(13,23), "double hit chance": random.randint(13,16), "double loot": random.randint(1,4), "chance": 92, "find": 7, "exp": random.randint(3,7)},
        "wizard": {"health": random.randint(32,45), "damage": random.randint(7,14), "dodge chance": random.randint(13,16), "double hit chance": random.randint(11,15), "double loot": random.randint(1,1), "chance": 98, "find": 2, "exp": random.randint(35,47)},
        "King's Guard": {"health": random.randint(48,60), "damage": random.randint(13,17), "dodge chance": random.randint(3,7), "double hit chance": random.randint(11,15), "double loot": random.randint(1,1), "chance": 100, "find": 1, "exp": random.randint(55,63)},
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
    t.sleep(0.1)
    print(f"You came across a {baddieName}!\n")
    s.updateSave()
    # general dungeon function
    
    base = 0

    def levelUpEnemyBoost():
        base = 10 * i.playerLevel // 2
        baddieOne["health"] += base
        baddieOne["damage"] += base // 5
    
    def levelUp():
        bonus = 0
        for _ in range(i.playerLevel):
            bonus =+ random.randint(1,3)
        i.playerHealth["health"] = 40 + bonus * 3
        i.playerDamage["damage"] = random.randint(4,8) + bonus
        if i.playerDodge["dodge chance"] <= 60:
            i.playerDodge["dodge chance"] = 20 + bonus // 2
        if i.playerDoubleHitRate["double hit chance"] <= 55:
            i.playerDoubleHitRate["double hit chance"] = 16 + bonus // 2

    def nextLevel():
        level = i.playerLevel + 1
        expNeededBonus = (random.randint(10,(15*level)//3) // level) // 2
        expNeeded = 50 * level + expNeededBonus
        return expNeeded

    def printLevelUp():
        expNeeded = nextLevel()
        if i.playerExp >= expNeeded:
            i.playerLevel += 1
            expNeeded = nextLevel()
            print("\n-<()>- ! Level Up ! -<()>-\n")
            print(f"Congratulations! You leveled up to level {i.playerLevel}! You need {expNeeded} EXP until the next level.")
            print("\n-----     -----     -----\n")
            levelUp()

    def printLevelStatus():
        expNeeded = nextLevel() - i.playerExp
        print(f"Exp needed for the next level: {expNeeded}. Your current Exp: {i.playerExp} Current player level: {i.playerLevel}.")
        print()

    dungeonGoing = True
    while dungeonGoing == True:
        # checks if player has enough potions
        def potionChecker(ones, twos):
            t.sleep(0.1)
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
        def enemyAttack(b, armorType=1, armorNumber=1):
            t.sleep(0.1)
            dodgeChance = random.randint(1,100)
            if dodgeChance <= 31 + b:
                print(f"The {baddieName} swung at you, but you dodged!")
            else:
                # if the player has 0 or less health and enemy has more than 0 health, the fight will end, player's health will be set to 0 if less than 0
                if i.playerHealth['hp'] > 0 and baddieOne['health'] > 0:
                    if i.playerStats[s.armor[armorType-1]]["rating"] != None:
                        damage = baddieOne["damage"] - (i.playerStats[s.armor[armorType-1]]["rating"]//2)
                    else:
                        damage = baddieOne["damage"]
                    i.playerHealth["hp"] -= damage

                    if i.playerHealth['hp'] <= 0:
                        i.playerHealth['hp'] = 0
                        print(f"The {baddieName} hit you for {damage} hp! You died!\n")
                        i.playerHealth['hp'] = 40
                        i.playerPotions["damage-pot"] = 0
                        i.playerPotions["dodge"] = 0
                        i.playerPotions["restoration"] = 5
                        itemReset()
                        s.died()
                        exit()
                    else:
                        print(f"The {baddieName} hit you for {damage} hp! You have {i.playerHealth['hp']} hp left!")
        
        # same concept as enemyAttack, except the opposite for the fight-end condition. a is damage boost

        if i.playerLevel > 1:
            levelUpEnemyBoost()

        def playerAttack(a):
            t.sleep(0.1)
            dodgeChance = random.randint(1,100)
            if dodgeChance <= baddieOne['dodge chance']:
                print(f'You swung at the {baddieName}, but it dodged! It has {baddieOne['health']} hp left!')
            else:
                if i.playerHealth['hp'] > 0 and baddieOne['health'] > 0:
                    if i.playerItemsState == False or i.playerItems["recharges"] == None:
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
                                drop2 = str(drop+drop1)+" "+drop2[2:]
                                print(f'You killed the {baddieName}! You got {drop2}s!')
                            else:
                                drop = "".join(drop)
                                drop2 = "".join(drop2)
                                print(f'You killed the {baddieName}! You got {drop} and {drop2}!')
                        else:
                            print(f'You killed the {baddieName}! You got {drop}!')
                        find = random.randint(1, baddieOne["find"])
                        if find == 1:
                            replaceItem()
                        find = random.randint(1,5)
                        if find == 3:
                            replaceItem(armor=2)

                        
                        i.playerExp += baddieOne["exp"]
                        printLevelUp()

                        if i.playerItems["recharges"] is not None and i.playerItemsState == False and i.playerItems["charge"] <= i.playerItems["max charges"]:
                            itemRecharge()
                        
                        i.playerHealth['hp'] = 40
                        dungeonRun()
                    else:
                        print(f"You hit the {baddieName} for {totalDamage} hp! It now has {baddieOne['health']} hp left!")
                        if i.playerItems["recharges"] is not None and i.playerItemsState == False and i.playerItems["charge"] <= i.playerItems["max charges"]:
                            itemRecharge()
        
        
        # fix so you can say no
        # appears if player is at 10 or lower HP
        def restoreHealth():
            t.sleep(0.1)
            if i.playerHealth['hp'] <= 15:
                print("\nYou are at low health.\n1. Drink a restoration potion\n2.Continue the fight\n")
                playerChoice = input("Your choice: ")
                t.sleep(0.1)
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
            t.sleep(0.1)
            print()
            t.sleep(0.1)
            print(f"You have {i.playerPotions["damage-pot"]} Damage Up potions, {i.playerPotions["dodge"]} Dodge Chance Up potions, and {i.playerPotions["restoration"]} Restoration potions")
            print("\n1. Drink a Damage Up Potion\n2. Drink a Dodge Chance Up Potion\n3. Drink a Restoration Potion\n4. Go back to the Attack Menu\n")
            t.sleep(0.1)
            print("Note that boosting potions last for 1 attack.\n")
            playerChoice = input("Your choice: ")
            t.sleep(0.5)
            print()
            
            if playerChoice == "1":
                if potionOut(i.potionNamesReal[0]) == True:
                    i.playerBoosts["damage up"] += random.randint(3,6)
                    print("You boosted your damage to "+str(i.playerBoosts["damage up"]+i.playerStats["stats"]["damage"])+" points!")
                i.playerPotions['damage-pot'] = int(potionChecker("Damage Potion", i.playerPotions['damage-pot']))

            elif playerChoice == "2":
                if potionOut(i.potionNamesReal[1]) == True:
                    i.playerBoosts["dodge up"] += random.randint(5,9)
                    print("You boosted your dodge stat to "+str(i.playerBoosts["dodge up"]+i.playerStats["stats"]["dodge chance"])+" points!")
                i.playerPotions['dodge'] = int(potionChecker("Dodge Up Potion", i.playerPotions['dodge']))

            elif playerChoice == "3": 
                if potionOut(i.potionNamesReal[2]) == True:
                    restor = random.randint(5,15)
                    if restor >= 13:
                        restor += random.randint(0,5)
                    i.playerHealth['hp'] += restor
                    print(f"You restored {restor} hp! You now have {i.playerHealth['hp']} hp!")
                i.playerPotions['restoration'] = int(potionChecker("Restoration Potion", i.playerPotions['restoration']))
                
            elif playerChoice == "4":
                dungeonCheckIn()

            else:
                print("Please enter a valid choice.\n")
                drinkPotions()
            
        # appears after each instance of attacking, options are to drink a potion or to attack
        def dungeonCheckIn():
            t.sleep(0.1)
            print("1. Attack\n2. Drink a potion\n3. Equip or unequip your weapon\n4. Check item\n5. Check armor\n6. Check player level\n7. Go to menu\n")
            playerChoice = input("Your choice: ")
            t.sleep(0.5)
            print()
            if playerChoice == "2": #wont allow u to attack
                drinkPotions()
            # attack just goes through both enemy and player attacks   
            elif playerChoice == "1":
                def attackStuff (x, y):
                    for _ in range(x):
                        playerAttack(i.playerBoosts["damage up"])
                        i.playerBoosts["damage up"] = 0
                    for _ in range(y):
                        enemyAttack(i.playerBoosts["dodge up"])
                        i.playerBoosts["dodge up"] = 0
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
                dungeonCheckIn()
            elif playerChoice == "4":
                readItemStats()
                dungeonCheckIn()
            elif playerChoice == "5":
                readItemStats(2)
                dungeonCheckIn()
            elif playerChoice == "6":
                print(printLevelStatus())
                dungeonCheckIn()
            elif playerChoice == "7":
                mainScreen()
            else:
                print("Please enter a valid choice.\n")
                dungeonCheckIn()
                    
        
        dungeonCheckIn()

                
# main menu function
def mainScreen():
    t.sleep(0.1)
    print()
    print("1. Load a save\n2. Create a new save\n3. Continue\n4. Open guide menu\n5. Exit\n\nNOTE: Making a new save will overwrite your old save. It will delete all progress made.")
    choice = input("Your choice: ")
    t.sleep(0.5)
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
