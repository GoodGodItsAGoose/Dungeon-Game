import Info as i

# loading the last save's info from saves.txt
def loadSave():
    subjects = ["damage-pot", "dodge", "restoration", "charge", "uses", "name", "state", "modifier"]
    results = {}
    with open('DungeonGame/saves.txt') as file:
        for line in file:
            if line != '\n':  # Skip empty lines
                name, *grades = line.strip().split(', ')
                results[name] = dict(zip(subjects, grades))
    i.playerPotions = results[str(len(results)-1)]
    i.playerItems["charge"] = results[str(len(results)-1)]["charge"]
    i.playerItems["uses"] = results[str(len(results)-1)]["uses"]
    i.playerItems["name"] = results[str(len(results)-1)]["name"]
    i.playerItemsState = results[str(len(results)-1)]["state"]
    i.playerItemModifier = results[str(len(results)-1)]["modifier"]

# updating the save's files
def updateSave():
    saveStats = i.playerPotions, i.playerItems, i.playerItemsState, i.playerItemModifier
    removes = ["damage-pot", "dodge", "restoration", "charge", "uses", "name", "state", "modifier", "damage", "{", "}", ": ", '"', "'", "(", ")"]
    subjects = ["damage-pot", "dodge", "restoration", "charge", "uses", "name", "state", "modifier"]
    num = 0
    results = {}
    with open('DungeonGame/saves.txt') as file:
        for line in file:
            if line != '\n':  # Skip empty lines
                name, *grades = line.strip().split(', ')
                results[name] = dict(zip(subjects, grades))
    number = len(results)
    for _ in range(16):
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
