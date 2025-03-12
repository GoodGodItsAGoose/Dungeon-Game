import random

"""
OPTIMIZE THE HELL UP

issues:
- fails to start 2/3 times

to add:
- make fighting more immersive
    - Maybe add weapon / other attack messages
- balance enemies and drop rates
"""

#player statistics
playerStats = {
    "stats": {"hp": 40, "damage": random.randint(4,8), "dodge chance": 20, "double hit chance": 16},
    "ups": {"damage up": 0, "dodge up": 0},
    "potions": {"damage-pot": 0, "dodge": 0, "restoration": 5},
    "item": {"charge": None, "uses": None, "name": None},
    "state": {False},
    "modifier": {None},
}

#name just used for text

# save would be potions, (None, None or 20, 1), False, 1 (if results[saveNumber][item] == None)
#have to go through and save weapon name, or save as number
Items = {
    1: {"charge":random.randint(5,20), "uses": random.randint(1,3), "name": "dagger"}, #collect this first name, then use that name to find damage
    2: {"charge":random.randint(5,25), "uses": random.randint(2,5), "name": "staff"}
}
ItemPowers = {
    1: {"damage": 3},
    2: {"damage": 4},
    3: {"damage": 5},
    # have these be numbers, randomize easily that way, update modifier
    #damage be here, dodge up, yada yada, for easy collecting and usage, if playerItems = [run thru item names] take a certain modifier? or randomized modifiers?
}
# Items["dagger"]["power"]["damage"]
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

# have a new variable that changes depending on item name? ie, once function completes it updates a variable so you can directly access the item?
# save itemName in save file? including None?

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

playerBoosts["damage up"] = 0
playerBoosts["dodge up"] = 0
