import random

def main():
    charecterClass = charecterClassGen()
    print(charecterClass)
    print(wepName)
    print(wepStats)

def charecterClassGen():

    char = random.randint(0, 8)

    charList = ["Scout", "Soldier", "Pyro", "Demoman", "Heavy", "Engineer", "Medic", "Sniper", "Spy"]

    charecterClassName = charList[char]

    return charecterClassName

def wepName():

    with open("TF2randomWeaponGenerator\main\wepNameAdj.txt", "r") as f:
        contentsAdj = f.readlines()
        f.close

    with open("TF2randomWeaponGenerator\main\wepNameNoun.txt", "r") as f:
        contentsNoun = f.readlines()
        f.close

    randAdj = contentsAdj[random.randint(0, len(contentsAdj))]
    randNoun = contentsNoun[random.randint(0, len(contentsNoun))]

    randAdj = str(randAdj.replace("\n", ""))
    randNoun = str(randNoun.replace("\n", ""))

    randWepName = randAdj + " " + randNoun
    
    return randWepName

def wepStats():

    itemSelection = ["w", "u", "m"]
    damageType = ["e", "b", "p", "m", "u"]
    
    wepType = [itemSelection[random.randint(0, len(itemSelection)-1)], damageType[random.randint(0, len(damageType)-1)]]

    if wepType[0] == "m":
        wepType[1] = "m"
    elif wepType[0] == "u":
        wepType[1] = "u"

    with open("TF2randomWeaponGenerator\main\statList", "r") as f:
        statsContent = f.readlines()
        
        randStat = statsContent[random.randint(0, len(statsContent)-1)]

        f.close
    
    randStat = randStat.strip("\n")

    randStat = randStat.split(" ")
    
    statOverType = randStat[-1]
    statOverType = list(statOverType)
    print(statOverType)
    
    statTier = statOverType[0]
    statWepType = statOverType[1]
    if len(statOverType) == 2:
        statTier = statOverType[0]
        statWepType = statOverType[1]
    elif len(statOverType) == 3:
        statTier = statOverType[:2]
        statWepType = statOverType[2]

    print(statTier)
    print(statWepType)
wepStats()