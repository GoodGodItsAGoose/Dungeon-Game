
import random
import time as t

# staff has 20 when it should have at least 25

"""
OPTIMIZE THE HELL UP

issues:
- fails to start 2/3 times

to add:
- make fighting more immersive
    - Maybe add weapon / other attack messages
- balance enemies and drop rates
"""

ChargesGuide = "Charges: Charges on an item is how many times you can use that item to attack an enemy before it depletes its energy and must be recharged. If you let it drop to 0, the item will use a recharge when recharging."
RechargesGuide = "Recharges - Recharges on an item are how many times the item's charge can reach 0. After the last time, the item will be deleted from your character."
ItemsGuide = "Items: There are items in the game you can obtain through killing enemies. They all have different amounts of starting charges, recharges, and damage boosts. You can only have one item on your character at a time, and can replace the item you have. Replacing the item will delete your current item."

PotionsInfoGuide = "Potions:\n- Damage Up Potion: This boosts your damage for one attack.\n- Dodge Chance Up Potion: This boosts your chance to dodge an attack for one attack.\n- Restoration Potion: This restores your health."

GuideMenu = "Information Menu:\n1. Guide to item definitions\n2. Guide to types of potions\n3. Guide to menus\n4. Continue to game"

MenuGuide = "Guide Information:\n1. Main Menu Guide\n2. Battle Menu Guide\n3. Potion Menu Guide\n4. Item Recharging Menu Guide\n5. Obtaining an Item Menu Guide\n6. Low Health Menu Guide\n7. Go Back"
ItemsGuide = "Items Information:\n1. Charges Definition\n2. Recharges Definition\n3. What Are Items?\n4. Go Back"

BattleMenuGuide = "Battle Menu - This menu will pop up after every action.\n1. Attack: Continues to the fight.\n2. Drink a potion: Goes to the Potion Drinking Menu.\n3. Equip or unequip your weapon: Toggles whether your item will be used in a fight or not.\n4. Check item: Checks your current item's stats.\n5. Go to menu: Returns to the Main Menu."
ItemRechargeMenuGuide = "Item Recharged Menu - This menu will pop up once your item reaches its max charge.\n1. Re-equip: Re-equips the item.\n2. Continue the fight: Does not re-equip the item, continues to the fight."
LowHealthMenuGuide = "Low Health Menu - This menu shows up if you are at 15 hp or lower.\n1. Drink a restoration potion: Restores health via restoration potion.\n2.Continue the fight: Doesn't drink a restoration potion, continues to the fight."
ObtainingItemMenuGuide = "Obtaining an item - This menu shows up every time you find a new item.\n1. Take it: Replaces your current item with this item, or equips the item if you have no item. YOU WILL HAVE TO CHOOSE TO USE THE ITEM IN THE BATTLE MENU TO USE IT!!\n2. Leave it: Leaves the item, you continue to use your weapon.\n3. Check your current item's stats: Checks your current item's stats, returns to this menu."
MainMenuGuide = "Main Menu - The start menu.\n1. Load a save: Loads your last save, continues to the fight.\n2. Create a new save: Creates a new save, overwrites your previous saves, then continues to the fight.\n3. Continue: Continues to the fight, overwrites your last save.\n4. Exit: Exit the game."
PotionMenuGuide = "Potion Drinking Menu - This menu is an offshoot of the Battle Menu.\n1. Drink a Damage Up Potion - Drinks a Damage Up Potion then returns to the Battle Menu.\n2. Drink a Dodge Chance Up Potion - Drinks a Dodge Chance Up Potion then returns to the Battle Menu.\n3. Drink a Restoration Potion - Drinks a Restoration Potion then returns to the Battle Menu.\n4. Go back to the Attack Menu - Returns to the Battle Menu."

def itemsGuide():
    t.sleep(0.1)
    print("\n"+ItemsGuide)
    choice = input("Your Choice: ")
    if choice == "1":
        t.sleep(0.1)
        print("\n"+ChargesGuide+"\n")
        itemsGuide()
    elif choice == "2":
        t.sleep(0.1)
        print("\n"+RechargesGuide+"\n")
    elif choice == "3":
        t.sleep(0.1)
        print("\n"+ItemsGuide+"\n")
        itemsGuide()
    elif choice == "4":
        guideMenu()
    else:
        print("Please enter a valid choice.\n")
        itemsGuide()

def menuGuide():
    t.sleep(0.1)
    print("\n"+MenuGuide)
    choice = input("Your Choice: ")
    if choice == "1":
        t.sleep(0.1)
        print("\n"+MainMenuGuide+"\n")
        menuGuide()
    elif choice == "2":
        t.sleep(0.1)
        print("\n"+BattleMenuGuide+"\n")
        menuGuide()
    elif choice == "3":
        t.sleep(0.1)
        print("\n"+PotionMenuGuide+"\n")
        menuGuide()
    elif choice == "4":
        t.sleep(0.1)
        print("\n"+ItemRechargeMenuGuide+"\n")
        menuGuide()
    elif choice == "5":
        t.sleep(0.1)
        print("\n"+ObtainingItemMenuGuide+"\n")
        menuGuide()
    elif choice == "6":
        t.sleep(0.1)
        print("\n"+LowHealthMenuGuide+"\n")
        menuGuide()
    elif choice == "7":
        guideMenu()
    else:
        print("Please enter a valid choice.\n")
        menuGuide()

def guideMenu():
    t.sleep(0.1)
    print("\n"+GuideMenu)
    choice = input("Your Choice: ")
    if choice == "1":
        itemsGuide()
    elif choice == "2":
        t.sleep(0.1)
        print("\n"+PotionsInfoGuide+"\n")
        guideMenu()
    elif choice == "3":
        menuGuide()
    elif choice == "4":
        pass
    else:
        print("Please enter a valid choice.\n")
        guideMenu()

    

    


#player statistics
playerStats = {
    "stats": {"hp": 40, "damage": random.randint(4,8), "dodge chance": 20, "double hit chance": 16},
    "ups": {"damage up": 0, "dodge up": 0},
    "potions": {"damage-pot": 0, "dodge": 0, "restoration": 5},
    "item": {"charge": None, "recharges": None, "name": None, "max charges": None},
    "state": False,
    "modifier": None
}

#name just used for text

# list of items you can use in the game
Items = {
    1: {"charge": random.randint(5,20), "recharges": random.randint(1,3), "name": "Dagger", "max charges": random.randint(17,20)}, #collect this first name, then use that name to find damage
    2: {"charge": random.randint(5,25), "recharges": random.randint(2,5), "name": "Staff", "max charges": random.randint(25,30)},
    3: {"charge": random.randint(10,20), "recharges": random.randint(1,3), "name": "Shortsword", "max charges": random.randint(23,25)},
    4: {"charge": random.randint(5,10), "recharges": random.randint(3,5), "name": "Sickle", "max charges": random.randint(13,17)}
}

# item bonus damages
ItemPowers = {
    1: {"damage": 3},
    2: {"damage": 4},
    3: {"damage": 4},
    4: {"damage": 5}
}

# player stats for easy access
playerHealth = playerStats["stats"]
playerDamage = playerStats["stats"]
playerDodge = playerStats["stats"]
playerDoubleHitRate = playerStats["stats"]
playerPotions = playerStats["potions"]
playerBoosts = playerStats["ups"]
playerItems = playerStats["item"]
playerItemsState = playerStats["state"]
playerItemModifier = playerStats["modifier"]

# lists for potion-related code
potionNames = ["Damage Up Potion", "Dodge Up Potion", "Restoration Potion"]
potionNamesReal = ["damage-pot", "dodge", "restoration"]
potionChances = [35, 65, 90, 10]

# does something...
def chance(percentage):
    chanceNum = random.randint(1,100)
    if chanceNum < percentage:
        return False
    return True

# checks if total is between min or max
def between(total, min, max):
    if total <= max and total >= min:
        return True
    return False

# out of num of options, each have different percentages of probability of occurring

# rewards for beating the enemy
def findAPotion(chance=1):
    amount = random.randint(1,chance)
    potion_type = random.randint(0,2)
    num = 0
    for _ in range(4):
        if potion_type == num:
            playerPotions[potionNamesReal[potion_type]] += amount
            if amount == 1:
                return f"{amount} {potionNames[potion_type]}"
            elif amount != 1:
                return f"{amount} {potionNames[potion_type]}s"
        num += 1
