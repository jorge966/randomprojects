

class pokemonAttack:

    attacking = {'fire': {'fire': 0.5, 'grass': 2.0, 'water': 0.5}, 'grass': {'fire': 0.5, 'grass': 0.5, 'water': 2.0}, 'water': {'fire': 2.0, 'grass': 0.5, 'water': 0.5}}



    def __init__(self, attackName, attackDamage, attackType):
        self.attackDamage = attackDamage
        self.attackName = attackName
        self.attackType = attackType

    def getAttackName(self):
        return self.attackName

    def getAttackDamage(self):
        return self.attackDamage

    def setAttackDamage(self, value):
        self.attackDamage = value

    def getAttackType(self):
        return self.attackType

    def setAttackType(self, value):
        self.attackType = value

    def attackType(self):
        attacktype = self.attackDamage * self.attacking[self.attackType()]
        if self.attackType() == self.attackType():
            print("its super effective!")
        return attacktype











