class Pokemon(object):
    attackingDict = {'fire': {'fire': 0.5, 'grass': 2.0, 'water': 0.5}, 'grass': {'fire': 0.5, 'grass': 0.5, 'water': 2.0}, 'water': {'fire': 2.0, 'grass': 0.5, 'water': 0.5}}
    def __init__(self, name, HP, Damage, type):
        self.name = name
        self.HP = HP
        self.Damage = Damage
        self.type = type

    def Battle(self, Opponent):
        attackDamage = self.Damage * self.attackingDict[self.type][Opponent.type]

        if(self.HP > 0):
            print("%s did %d Damage to %s"%(self.name, attackDamage, Opponent.name))
            print("%s has %d HP left"%(Opponent.name, Opponent.HP))
            Opponent.HP -= attackDamage
            return Opponent.Battle(self)
        else:
            print("%s wins! (%d HP left)" %(Opponent.name, Opponent.HP))
            return Opponent, self


Squirtle = Pokemon('Squirtle', 100, 5, 'water')
Bulbasaur = Pokemon('Bulbasaur', 100, 10, 'grass')
Winner, Loser = Bulbasaur.Battle(Squirtle)