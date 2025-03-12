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
    "state": False,
    "modifier": None
}

#name just used for text

# list of items you can use in the game
Items = {
    1: {"charge": random.randint(5,20), "uses": random.randint(1,3), "name": "Dagger"}, #collect this first name, then use that name to find damage
    2: {"charge": random.randint(5,25), "uses": random.randint(2,5), "name": "Staff"},
    3: {"charge": random.randint(10,20), "uses": random.randint(1,3), "name": "Shortsword"},
    4: {"charge": random.randint(5,10), "uses": random.randint(3,5), "name": "Sickle"}
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

# resets boosts
playerBoosts["damage up"] = 0
playerBoosts["dodge up"] = 0
