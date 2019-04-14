import pokemonAttack as pokemonAtk

class Pokemon:

    attackList = [pokemonAtk.pokemonAttack("Vinewhip", 30 , "grass" ), pokemonAtk.pokemonAttack("Growl", -20, "normal"),pokemonAtk.pokemonAttack("Bubbles", 40, "water")]

    def __init__(self, name , hp , atk , defense, currentLevel, type):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.currentLevel = currentLevel
        self.type = type

    def getName(self):
        return self.name

    def getHP(self):
        return self.hp

    def getAttack(self):
        return self.atk

    def getDef(self):
        return self.defense

    def getAttack1(self):
        return self.attackList[0]

    def getAttack2(self):
        return self.attackList[1]

    def getAttack3(self):
        return self.attackList[2]

    def getAllAttacks(self):
        return self.attackList

    def getAllStats(self):
        statDict = {
            "name": self.name,
            "hp": self.hp,
            "atk": self.atk,
            "def": self.defense
        }
        return statDict
    def getAllBattle(self):
        return self.atk

    def getCurrentLevel(self):
        return self.currentLevel

    def getLevelUp(self):
        self.currentLevel = self.currentLevel + 1
        return self.currentLevel

    def pokemonType(self):
        return self.type

























