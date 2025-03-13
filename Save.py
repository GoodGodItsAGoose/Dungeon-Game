import Info as i

# loading the last save's info from saves.txt
def loadSave():
    subjects = ["damage-pot", "dodge", "restoration", "charge", "recharges", "name", "state", "modifier"]
    results = {}
    with open('DungeonGame/saves.txt') as file:
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
        i.playerItemsState = False
        i.playerItemModifier = None
    else:
        i.playerItems["charge"] = int(results[str(len(results)-1)]["charge"])
        i.playerItems["recharges"] = int(results[str(len(results)-1)]["recharges"])
        i.playerItems["name"] = results[str(len(results)-1)]["name"]
        i.playerItemsState = results[str(len(results)-1)]["state"]
        i.playerItemModifier = int(results[str(len(results)-1)]["modifier"])

# updating the save's files
def updateSave():
    saveStats = i.playerPotions, i.playerItems, i.playerItemsState, i.playerItemModifier
    saveStats = str(saveStats).replace("'charge': '', 'recharges': 'None', 'name': 'None', 'state': 'None', 'modifier': 'False'}, {", "")
    removes = ["damage-pot", "dodge", "restoration", "charge", "recharges", "name", "state", "modifier", "damage", "{", "}", ": ", '"', "'", "(", ")", "res"]
    subjects = ["damage-pot", "dodge", "restoration", "charge", "recharges", "name", "state", "modifier"]
    num = 0
    results = {}
    with open('DungeonGame/saves.txt') as file:
        for line in file:
            if line != '\n':  # Skip empty lines
                name, *grades = line.strip().split(', ')
                results[name] = dict(zip(subjects, grades))
    number = len(results)
    for _ in range(17):
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
