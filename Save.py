
import Info as i

# loading the last save's info from saves.txt
def loadSave():
    subjects = ["damage-pot", "dodge", "restoration", "charge", "recharges", "name", "max charges", "state", "modifier"]
    results = {}
    with open('PYTHON/DungeonGame/saves.txt') as file:
        for line in file:
            if line != '\n':  # Skip empty lines
                name, *grades = line.strip().split(', ')
                results[name] = dict(zip(subjects, grades))
    i.playerPotions["damage-pot"] = int(results[str(len(results)-1)]["damage-pot"])
    i.playerPotions["dodge"] = int(results[str(len(results)-1)]["dodge"])
    i.playerPotions["restoration"] = int(results[str(len(results)-1)]["restoration"])
    if results[str(len(results)-1)]["charge"] == "None":
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

# updating the save's files
def updateSave():
    saveStats = i.playerPotions, i.playerItems, i.playerItemsState, i.playerItemModifier
    removes = ["damage-pot", "dodge", "restoration", "max charges", "charge", "recharges", "name", "state", "modifier", "damage", "{", "}", ": ", '"', "'", "(", ")", "res"]
    subjects = ["damage-pot", "dodge", "restoration", "charge", "recharges", "name", "max charges", "state", "modifier"]
    num = 0
    results = {}
    with open('PYTHON/DungeonGame/saves.txt') as file:
        for line in file:
            if line != '\n':  # Skip empty lines
                name, *grades = line.strip().split(', ')
                results[name] = dict(zip(subjects, grades))
    number = len(results)
    for _ in range(18):
        saveStats = str(saveStats).replace(removes[num], "")
        num += 1
    with open("PYTHON/DungeonGame/saves.txt", "a") as f:
        f.write("\n")
        f.write(f"{number}, {saveStats}")
    
# making a new save
def newSave():
    with open("PYTHON/DungeonGame/saves.txt", "w") as f:
        f.write("\n")
    updateSave()
    print("Overwritten previous save.")

# clearing the save if you died, same as newSave but without the print argument
def died():
    with open("PYTHON/DungeonGame/saves.txt", "w") as f:
        f.write("\n")
    updateSave()
