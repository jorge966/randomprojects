class BasePokemon():

    attackList = {}

    def __init__(self, name , hp , atk , defense, currentLevel, type, attack1, attack2, attack3, attack4):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.currentLevel = currentLevel
        self.type = type
        self.attackList = {
            attack1.getAttackName() : attack1,
            attack2.getAttackName() : attack2,
            attack3.getAttackName() : attack3,
            attack4.getAttackName() : attack4
        }

    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def setHp(self, value):
        self.hp = value

    def getAtk(self):
        return self.atk

    def setAtk(self, value):
        self.atk = value

    def getDefence(self):
        return self.defense

    def setDefence(self, value):
        self.defense = value

    def getCurrentLevel(self):
        return self.currentLevel

    def setCurrentLevel(self, value):
        self.currentLevel = value

    def getType(self):
        return self.type

    def getAllAttacks(self):
        return self.attackList

