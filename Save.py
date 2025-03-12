import Info as i

# updating a nonexistent save makes a whole new save that is so fucked

def loadSave():
    subjects = ["damage-pot", "dodge", "restoration"]
    results = {}
    with open('DungeonGame/saves.txt') as file:
        next(file)
        for line in file:
            if line != '\n':  # Skip empty lines
                name, *grades = line.strip().split(', ')
                results[name] = dict(zip(subjects, grades))
    i.playerPotions = results[str(len(results)-1)]

def updateSave():
    saveStats = i.playerPotions
    removes = ["damage-pot", "dodge", "restoration", "{", "}", ": ", '"', "'"]
    subjects = ["damage-pot", "dodge", "restoration"]
    num = 0
    results = {}
    with open('DungeonGame/saves.txt') as file:
        next(file)
        for line in file:
            if line != '\n':  # Skip empty lines
                name, *grades = line.strip().split(', ')
                results[name] = dict(zip(subjects, grades))
    number = len(results)
    for _ in range(8):
        saveStats = str(saveStats).replace(removes[num], "")
        num += 1
    with open("DungeonGame\saves.txt", "a") as f:
        f.write("\n")
        f.write(f"{number}, {saveStats}")
    

def newSave():
    with open("DungeonGame\saves.txt", "w") as f:
        f.write("\n")
    updateSave()
    print("Overwritten previous save.")

