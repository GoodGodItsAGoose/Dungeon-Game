import random
import time as t
import Info as i
import Save as s

# change damage amount to vary each attack (+ random.randint(0,2)
"""
ideas:

magic items, certain amounts of uses, recharges or one time charge

rename potions to other things for more depth

add a longer description of fights
"""

def dungeonRun():
    
		# list of enemies, including its health, damage, dodge chance, double hit chance, double loot (will eventually use or remove) and chance of encountering
    enemy = {
        "undead": {"health": random.randint(23,30), "damage": random.randint(2,5), "dodge chance": 13, "double hit chance": 3, "double loot": random.randint(1,4), "chance": 16},
        "bandit": {"health": random.randint(17, 25), "damage": random.randint(4,7), "dodge chance": random.randint(10,23), "double hit chance": random.randint(12,17), "double loot": random.randint(1,3), "chance": 30}, 
        "snake": {"health": random.randint(7,15), "damage": random.randint(1,3), "dodge chance": 35, "double hit chance": 18, "double loot": random.randint(1,4), "chance": 45},
        "undead guard": {"health": random.randint(27,35), "damage": random.randint(6,11), "dodge chance": 17, "double hit chance": random.randint(11,15), "double loot": random.randint(1,2), "chance": 57},
        "giant spider": {"health": random.randint(13,20), "damage": random.randint(3,6), "dodge chance": random.randint(24,34), "double hit chance": random.randint(11,18), "double loot": random.randint(1,2), "chance": 68},
        "giant armored spider": {"health": random.randint(17,26), "damage": random.randint(3,7), "dodge chance": random.randint(19,31), "double hit chance": random.randint(11,16), "double loot": random.randint(1,1), "chance": 77},
        "goblin": {"health": random.randint(13,17), "damage": random.randint(2,5), "dodge chance": random.randint(13,23), "double hit chance": random.randint(13,16), "double loot": random.randint(1,4), "chance": 90},
        "wizard": {"health": random.randint(36,44), "damage": random.randint(7,14), "dodge chance": random.randint(13,16), "double hit chance": random.randint(11,15), "double loot": random.randint(1,1), "chance": 97},
        "King's Guard": {"health": random.randint(45,53), "damage": random.randint(13,17), "dodge chance": random.randint(3,7), "double hit chance": random.randint(11,15), "double loot": random.randint(1,1), "chance": 100},
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
    print(f"You came across a {baddieName}!")
    s.updateSave()
    # general dungeon function
    
    dungeonGoing = True
    while dungeonGoing == True:
        # checks if player has enough potions
        def potionChecker(ones, twos):
            if twos > 0:
                twos -=  1
                print(f"You drank 1 {ones}! You have {twos} {ones}s left!")
                return twos
            print(f"You're out of {ones}s!")

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
                print(f"The {baddieName} swung at you, but you dodged!")
            else:
                # if the player has 0 or less health and enemy has more than 0 health, the fight will end, player's health will be set to 0 if less than 0
                if i.playerHealth['hp'] > 0 and baddieOne['health'] > 0:
                    i.playerHealth["hp"] -= baddieOne["damage"]

                    if i.playerHealth['hp'] <= 0:
                        i.playerHealth['hp'] = 0
                        print(f"The {baddieName} hit you for {baddieOne['damage']} hp! You died!")
                        s.updateSave()
                        i.playerHealth['hp'] = 40
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
                    baddieOne['health'] -= i.playerDamage['damage'] + a
                    if baddieOne['health'] <= 0:
                        baddieOne['health'] = 0
                        drop = i.findAPotion(drops)
                        if baddieOne["double loot"] == 1:
                            drop2 = i.findAPotion(drops)
                            # stack potions if needed, if second part of message is the same, just add the two, seperate them into their seperate words, then do that
                            drop.split()
                            drop2.split()
                            if drop[1] is drop2[1]:
                                print("success!")
                                drop = check(drop[0])
                                drop1 = check(drop2[0])
                                drop = str(drop+drop1)+" "+drop2[2:]
                                print(f'You killed the {baddieName}! You got {drop}s!')
                            else:
                                print(f'You killed the {baddieName}! You got {drop} and {drop2}!')
                        else:
                            print(f'You killed the {baddieName}! You got {drop}!')
                        print()
                        i.playerHealth['hp'] = 40
                        dungeonRun()
                    else:
                        print(f"You hit the {baddieName} for {i.playerDamage['damage']} hp! It now has {baddieOne['health']} hp left!")
        
        # appears if player is at 10 or lower HP
        def restoreHealth():
            if i.playerHealth['hp'] <= 15:
                print("Would you like to drink a health potion?")
                playerChoice = input("")
                if "yes" or "y" in playerChoice.lower():
                    restor = random.randint(5,15)
                    if restor >= 13:
                        restor += random.randint(0,5)
                    i.playerHealth['hp'] += restor
                    
                    print(f"You restored {restor} hp! You now have {i.playerHealth['hp']} hp!")
                    i.playerPotions['restoration'] = potionChecker("Restoration Potion", i.playerPotions['restoration'])
                else:
                    print("Please enter a valid choice")
                    restoreHealth()
                    
        
        def drinkPotions():
            print()
            print(f"You have {i.playerPotions["damage-pot"]} Damage Up potions, {i.playerPotions["dodge"]} Dodge Chance Up potions, and {i.playerPotions["restoration"]} Restoration potions.\n1. Drink a Damage Up Potion\n2. Drink a Dodge Chance Up Potion\n3. Drink a Restoration Potion")   
            print("Note that boosting potions last for 1 attack.")
            playerChoice = input("")
            
            if playerChoice == "1":
                if potionOut(i.potionNamesReal[0]) == True:
                    i.playerBoosts["damage up"] = random.randint(3,6)
                    print("You boosted your damage by "+str(i.playerBoosts["damage up"])+" points!")
                i.playerPotions['damage-pot'] = int(potionChecker("Damage Potion", int(i.playerPotions['damage-pot'])))

            elif playerChoice == "2":
                if potionOut(i.potionNamesReal[1]) == True:
                    i.playerBoosts["dodge up"] = random.randint(5,9)
                    print("You boosted your dodge stat by "+str(i.playerBoosts["dodge up"])+" points!")
                i.playerPotions['dodge'] = int(potionChecker("Dodge Up Potion", int(i.playerPotions['dodge'])))

            elif playerChoice == "3": 
                if potionOut(i.potionNamesReal[2]) == True:
                    restor = random.randint(5,15)
                    if restor >= 13:
                        restor += random.randint(0,5)
                    i.playerHealth['hp'] += restor
                    print(f"You restored {restor} hp! You now have {i.playerHealth['hp']} hp!")
                i.playerPotions['restoration'] = int(potionChecker("Restoration Potion", int(i.playerPotions['restoration'])))
                print()
            else:
                print("Please enter a valid choice.")
                drinkPotions()
        
        # appears after each instance of attacking, options are to drink a potion or to attack
        def dungeonCheckIn():
            i.playerPotions["damage-pot"] = int(i.playerPotions["damage-pot"])
            i.playerPotions["dodge"] = int(i.playerPotions["dodge"])
            i.playerPotions["restoration"] = int(i.playerPotions["restoration"])
            print("1. Attack\n2. Drink a potion\n3. Go to menu")
            playerChoice = input("Your Choice: ")
            # resets boosts to 0
            i.playerBoosts["damage up"] = 0
            i.playerBoosts["dodge up"] = 0
            if playerChoice == "2": #wont allow u to attack
                drinkPotions()
            # attack just goes through both enemy and player attacks   
            elif playerChoice == "1":
                def attackStuff (x, y):
                    print()
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
                print()
                mainScreen()
            else:
                print("Please enter a valid choice.")
                dungeonCheckIn()
                    
        
        dungeonCheckIn()

                

def mainScreen():
    print("1. Load a save\n2. Create a new save\n3. Continue\n4. Exit\n\nNOTE: Making a new save will overwrite your old save. It will delete all progress made.")
    choice = input("Your choice: ")
    if choice == "1":
        s.loadSave()
        print(f"You loaded the previous save.")
        print()
        dungeonRun()
    elif choice == "2":
        s.newSave()
        print()
        dungeonRun()
    elif choice == "3":
        print()
        dungeonRun()
    elif choice == "4":
        exit()
    else:
        print("Please enter a valid choice.")
        mainScreen()

mainScreen()