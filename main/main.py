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

    with open("python3Projects\TF2randomWeaponGen\main\wepNameAdj.txt", "r") as f:
        contentsAdj = f.readlines()
        f.close

    with open("python3Projects\TF2randomWeaponGen\main\wepNameNoun.txt", "r") as f:
        contentsNoun = f.readlines()
        f.close
    
    randAdj = contentsAdj[random.randint(0, len(contentsAdj))]
    randNoun = contentsNoun[random.randint(0, len(contentsNoun))]

    randWepName = str(randAdj) + str(randNoun)

    return randWepName

print(wepName())