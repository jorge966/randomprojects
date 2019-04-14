class PokemonAttack:

    currentPP = None
    currentDmg = None
    currentAccuracy = None
    keywordTable = {}

    def __init__(self, dmg, pp, name, baseAccuracy, atkType, keywordTable=None):
        self.baseDmg = dmg
        self.basePP = pp
        self.atkName = name
        self.baseAccuracy = baseAccuracy
        self.atkType = atkType
        self.keywordTable = keywordTable

    # Current Attack, PP, and Accuracy Value Modifiers
    def getCurrentDamage(self):
        if self.currentDmg is None:
            self.currentDmg = self.baseDmg
        return self.currentDmg

    def setCurrentDamage(self, value=None, reduction=None, increase=None):
        if value is not None:
            self.currentDmg = value
        elif reduction is not None:
            self.currentDmg = self.currentDmg - reduction
        elif increase is not None:
            self.currentDmg = self.currentDmg + increase
        else:
            print("error")

    def getCurrentPP(self):
        if self.currentPP is None:
            self.currentPP = self.basePP
        return self.currentPP

    def setCurrentPP(self, value=None, reduction=None, increase=None):
        if value is not None:
            self.currentPP = value
        elif reduction is not None:
            self.currentPP = self.currentPP - reduction
        elif increase is not None:
            self.currentPP = self.currentPP + increase
        else:
            print("error")

    def getCurrentAccuracy(self):
        if self.currentAccuracy is None:
            self.currentAccuracy = self.baseAccuracy
        return self.currentAccuracy

    def setCurrentAccuracy(self, value=None, reduction=None, increase=None):
        if value is not None:
            self.currentAccuracy = value
        elif reduction is not None:
            self.currentAccuracy = self.currentAccuracy - reduction
        elif increase is not None:
            self.currentAccuracy = self.currentAccuracy + increase
        else:
            print("error")

    # Generic Functions
    def getBaseAttackDamage(self):
        return self.baseDmg

    def setBaseAttackDamage(self, value):
        self.baseDmg = value

    def getBaseAccuracy(self):
        return self.baseAccuracy

    def getBaseAttackPP(self):
        return self.basePP

    def setBaseAttackPP(self, value):
        self.basePP = value

    def getAttackType(self):
        return self.atkType

    def getAttackName(self):
        return self.atkName

