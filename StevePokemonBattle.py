import time
import StevePokemonAttack as pkmnA
import StevePokemon as pkmn
import random as rand

# Import Pokemon List
masterDict = {
    "grassList": {
        "vinewhip": [50, 25, "Vine Whip", 100, "Grass"],
        "absorb": [40, 20, "Absorb", 100, "Grass"],
        "razorleaf": [95, 15, "Razor Leaf", 95, "Grass"]
    },
    "waterList": {
        "bubble": [20, 35, "Bubble", 100, "Water"],
        "bubblebeam": [65, 20, "Bubble Beam", 100, "Water"],
        "surf": [95, 15, "Surf", 100, "Water"]
    },
    "fireList": {
        "ember": [20, 35, "Ember", 100, "Fire"],
        "firepunch": [35, 60, "Fire Punch", 100, "Fire"],
        "flameblast": [200, 5, "Flame Blast", 75, "Fire"]
    },
    "normalList": {
        "growl": [0, 50, "Growl", 100, "Normal"],
        "sandattack": [0, 30, "Sand-Attack", 85, "Normal"],
        "scratch": [30, 25, "Scratch", 100, "Normal"]
    }
}

# Generate Grass List
masterGrassDict = masterDict["grassList"]
grassAttackDict = {}
for key in masterGrassDict:
    values = masterGrassDict[key]
    atk = pkmnA.PokemonAttack(values[0], values[1], values[2], values[3], values[4])
    grassAttackDict[atk.getAttackName()] = atk

# Generate Water List
masterWaterList = masterDict["waterList"]
waterAttackDict = {}
for key in masterWaterList:
    values = masterWaterList[key]
    atk = pkmnA.PokemonAttack(values[0], values[1], values[2], values[3], values[4])
    waterAttackDict[atk.getAttackName()] = atk

# Generate Fire List
masterFireDict = masterDict["fireList"]
fireAttackDict = {}
for key in masterFireDict:
    values = masterFireDict[key]
    atk = pkmnA.PokemonAttack(values[0], values[1], values[2], values[3], values[4])
    fireAttackDict[atk.getAttackName()] = atk

# Generate Normal List
masterNormalDict = masterDict["normalList"]
normalAttackDict = {}
for key in masterNormalDict:
    values = masterNormalDict[key]
    atk = pkmnA.PokemonAttack(values[0], values[1], values[2], values[3], values[4])
    normalAttackDict[atk.getAttackName()] = atk

# Make Three Starter Pokemon
squirtle_pkmn = pkmn.BasePokemon("Squirtle", 50, 25, 60, 10, "Water",
                                 waterAttackDict["Bubble"],
                                 waterAttackDict["Bubble Beam"],
                                 waterAttackDict["Surf"],
                                 normalAttackDict["Sand-Attack"])
charmander_pkmn = pkmn.BasePokemon("Charmander", 60, 25, 30, 10, "Fire",
                                   fireAttackDict["Ember"],
                                   fireAttackDict["Fire Punch"],
                                   fireAttackDict["Flame Blast"],
                                   normalAttackDict["Scratch"])
bulbasaur_pkmn = pkmn.BasePokemon("Bulbasaur", 80, 15, 90, 10, "Grass",
                                  grassAttackDict["Vine Whip"],
                                  grassAttackDict["Absorb"],
                                  grassAttackDict["Razor Leaf"],
                                  normalAttackDict["Growl"])

masterPokemonDict = {
    charmander_pkmn.getName(): charmander_pkmn,
    bulbasaur_pkmn.getName(): bulbasaur_pkmn,
    squirtle_pkmn.getName(): squirtle_pkmn
}

def main():
    print("Select a Pokemon")
    tempDictIndex = {}
    user_selected_pokemon = None
    computer_selected_pokemon = None

    # Iterate through each Pokemon and display them as an option
    for index, key in enumerate(masterPokemonDict):
        currentPokemon = masterPokemonDict[key]
        tempDictIndex[index] = currentPokemon.getName()
        print("{}. {}".format(index + 1, currentPokemon.getName()))

    # Get user input
    user_pokemon = int(input(": ")) - 1

    # If the user selected a valid Pokemon, flag it as active
    if user_pokemon in tempDictIndex:
        selectedPokemonName = tempDictIndex[user_pokemon]
        user_selected_pokemon = masterPokemonDict[selectedPokemonName]
    else:
        print("You have made an invalid selection")

    # Have computer choose one of two remaining pokemon
    randomIndex = chooseRandomPokemon(tempDictIndex, user_pokemon)
    selectedComputerPokemonName = tempDictIndex[randomIndex]
    computer_selected_pokemon = masterPokemonDict[selectedComputerPokemonName]

    # Battle the two pokemon
    battle_arena(user_selected_pokemon, computer_selected_pokemon)

def chooseRandomPokemon(temporary_dict, user_selected_index):
    while(True):
        randomIndex = rand.randint(0, len(temporary_dict)-1)
        if randomIndex == user_selected_index:
            continue
        else:
            return randomIndex

def battle_arena(pokemon1, pokemon2):
    print("Go {}".format(pokemon1.getName()))
    time.sleep(1)
    print("Your opponent sends out {}".format(pokemon2.getName()))
    time.sleep(1)
    while(True):
        print("What will you do?")
        print("1. Attack")
        print("2. Run")
        userchoice = input(": ")
        if userchoice == "1":
            pokemonMoveset = pokemon1.getAllAttacks()
            for index, key in enumerate(pokemonMoveset):
                print("{}. {}".format(index, key))
            userattack = input("Select an attack")

        elif userchoice == "2":
            print("Got away safely bitch")
            return "Player Lost the Battle"
        else:
            print("Wrong choice bitch")
        break

## EXECUTION SPACE
main()

