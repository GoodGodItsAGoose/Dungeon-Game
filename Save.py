
import Info as i

armor = [
    "leggings", "armbands", "chestplate"
]
info = [
    "rating", "durability", "name"
]
def armorCheck(thing, a=1, collect=False):
    for _ in range(3):
        num1 = 1
        num = 0
        for _ in range(3):
            if collect == True:
                i.playerStats[armor[num]][info[num1-1]] = thing[info[num1-1]]
                num += 1
            elif i.playerStats[armor[num]][info[num1-1]] == "None" or i.playerStats[armor[num]][info[num1-1]] == None:
                i.playerStats[armor[num]][info[num1-1]] = None
                num1 += 1
            else:
                if a == 1:
                    try:
                        i.playerStats[armor[num]][info[num1-1]] = int(thing[info[num1-1]])
                    except TypeError:
                        i.playerStats[armor[num]][info[num1-1]] = thing[info[num1-1]]
                    num1 += 1
                else:
                    i.playerStats[armor[num]][info[num1-1]] = None
                    num1 += 1
            num += 1

# loading the last save's info from saves.txt
def loadSave():
    subjects = ["damage-pot", "dodge", "restoration", "charge", "recharges", "name", "max charges", "state", "modifier", "exp", "level", "rating", "durability", "name", "rating", "durability", "name", "rating", "durability", "name"]
    results = {}
    with open('DungeonGame/saves.txt') as file:
        for line in file:
            if line != '\n':  # Skip empty lines
                name, *grades = line.strip().split(', ')
                results[name] = dict(zip(subjects, grades))
    i.playerPotions["damage-pot"] = int(results[str(len(results)-1)]["damage-pot"])
    i.playerPotions["dodge"] = int(results[str(len(results)-1)]["dodge"])
    i.playerPotions["restoration"] = int(results[str(len(results)-1)]["restoration"])

    if results[str(len(results)-1)]["charge"] == "None" or results[str(len(results)-1)]["charge"] == None:
        i.playerItems["charge"] = None
        i.playerItems["recharges"] = None
        i.playerItems["name"] = None
        i.playerItems["max charges"] = None
        i.playerItemsState = False
        i.playerItemModifier = None
    else:
        i.playerItems["charge"] = int(results[str(len(results)-1)]["charge"])
        i.playerItems["recharges"] = int(results[str(len(results)-1)]["recharges"])
        i.playerItems["name"] = results[str(len(results)-1)]["name"]
        i.playerItems["max charges"] = int(results[str(len(results)-1)]["max charges"])
        if results[str(len(results)-1)]["state"] == "False":
            i.playerItemsState = False
        elif results[str(len(results)-1)]["state"] == "True":
            i.playerItemsState = True
        i.playerItemModifier = int(results[str(len(results)-1)]["modifier"])
    i.playerExp = int(results[str(len(results)-1)]["exp"])
    i.playerLevel = int(results[str(len(results)-1)]["level"])

# updating the save's files
def updateSave():
    saveStats = i.playerPotions, i.playerItems, i.playerItemsState, i.playerItemModifier, i.playerExp, i.playerLevel, i.playerStats["leggings"], i.playerStats["armbands"], i.playerStats["chestplate"]
    removes = ["damage-pot", "dodge", "restoration", "max charges", "charge", "recharges", "name", "state", "modifier", "damage", "exp", "level", "leggings", "rating", "durability", "name", "armbands", "chestplate", "{", "}", ": ", '"', "'", "(", ")", "res"]
    subjects = ["damage-pot", "dodge", "restoration", "charge", "recharges", "name", "max charges", "state", "modifier", "exp", "level"]
    num = 0
    results = {}
    with open('DungeonGame/saves.txt') as file:
        for line in file:
            if line != '\n':  # Skip empty lines
                name, *grades = line.strip().split(', ')
                results[name] = dict(zip(subjects, grades))
    number = len(results)
    for _ in range(26):
        saveStats = str(saveStats).replace(removes[num], "")
        num += 1
    with open("DungeonGame/saves.txt", "a") as f:
        f.write("\n")
        f.write(f"{number}, {saveStats}")
    
# making a new save
def newSave():
    with open("DungeonGame/saves.txt", "w") as f:
        f.write("\n")
    updateSave()
    print("Overwritten previous save.")

# clearing the save if you died, same as newSave but without the print argument
def died():
    with open("DungeonGame/saves.txt", "w") as f:
        f.write("\n")
    updateSave()
