import pokemonClass as pk
import time


bulbasaur_pokemon = pk.Pokemon("bulbasaur", 45, 49, 49, 5, "grass")
charmander_pokemon = pk.Pokemon("charmander", 39, 52, 43, 5, "fire")
squirtle_pokemon = pk.Pokemon("squirtle", 44, 48, 65, 5, "water")
pidgey_pokemon = pk.Pokemon("pidgey", 40, 45, 40, 5, "flying")
pikachu_pokemon = pk.Pokemon("pikachu", 35, 55, 40, 5, "lightning")

pokemonList = []

pokemonList.append(bulbasaur_pokemon)
pokemonList.append(charmander_pokemon)
pokemonList.append(squirtle_pokemon)
pokemonList.append(pidgey_pokemon)
pokemonList.append(pikachu_pokemon)

loop = True
while(loop):
    print("2. Fight two pokemon")
    choice = input("Choose here: ")
    if choice == "2":
        print(charmander_pokemon.getName() + " Level : " + (str(charmander_pokemon.getCurrentLevel())))
        print(squirtle_pokemon.getName() + " Level : " + (str(squirtle_pokemon.getCurrentLevel())))
        battle_choice1 = input("Pick a number")
        if battle_choice1 == "1":
            for item in pokemonList():
                print(str(pokemonList().getAllAttacks.index(item)) + " " + item.attackName )
            battle_move = input("pick a move and prepare to battle")
            if battle_move == "0":
                print(charmander_pokemon.getName() + " used " + (str(charmander_pokemon.getAttack1().getAttackDamage())) + "!")
                if charmander_pokemon.getAttack1().getAttackDamage() - squirtle_pokemon.getAttack2().getAttackDamage() > 0:
                    print("successfully used " + charmander_pokemon.getAttack1().getAttackName() + " for " + (str(charmander_pokemon.getAttack1().getAttackDamage())) + " !")
                else:
                    print(charmander_pokemon.getName() + " missed!")
            if battle_move == "1":
                print("enemy " + (str(squirtle_pokemon.getName())) + " used " + (str(squirtle_pokemon.getAttack2().getAttackName())))
                time.sleep(1)
                print((str(charmander_pokemon.getName())) + " had is damage reduced!")
                time.sleep(1)
                print(charmander_pokemon.getName() + " used " + (str(charmander_pokemon.getAttack1().getAttackName())))
                time.sleep(1)
                charmander_pokemon.getAttack1().setAttackDamage(10)
                print("successfully used " + (str(charmander_pokemon.getAttack1().getAttackName())) + " for " + (str(charmander_pokemon.getAttack1().getAttackType())))

                time.sleep(1)

                print(squirtle_pokemon.getName() + " Fainted!")
                time.sleep(1)
                print(charmander_pokemon.getName() + " leveled up!")
                time.sleep(1)
                print(charmander_pokemon.getName()+" is now level "+(str(charmander_pokemon.getLevelUp())) + "!")

                break





