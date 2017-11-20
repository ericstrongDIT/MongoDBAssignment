"""The following Class reads in the CSV File Pokemon.csv and places the data into a pokemon structure"""
from CSV_Entry import CSV_Entry
from pymongo import MongoClient

#db connection
con = MongoClient()
db = con.assignment

gen1 = []
gen2 = []
gen3 = []
gen4 = []
gen5 = []
gen6 = []


def getCSV(entry):
    lines = []
    f = open('Pokemon.csv', 'r')
    file_content = f.readlines()


    for row in file_content:
        # create objects of type CSV_Entry
        if(row.startswith('#')):
            continue
        row = str(row)
        lines = row.split(',')
        entry.append(CSV_Entry(lines))

    f.close()


def output(entry):
    # 1: Total count of pokemon
    print ("number of pokemon in the file: " + str(entry.__len__()))

    for pokemon in entry:
        print(pokemon)

def oneToFew(entry):
    """the following function iterates through the data set and creates a one:few cardinality for the pokemon characters"""
    characters = db.characters #create the document (table)

    characters.remove({}) #remove all from the set each time function is ran

    #foreach pokemon add them to the document in the onetofew cardinality
    for p in entry:
        """
        format for the one to few 
        pokemon.character{
                        number {},
                        pokemon_name: {...},
                        types:[type1: {...},type2: {...}],
                        attibutes:[attack{}etc...],
                         generation: {...},
                        legendary:{}
                        }
    
        """

        types = [{'type 1': p.type1},{'type 2': p.type2}]
        special = [{'special attack':p.spAtk},{'special defense':p.spDef}]
        attributes = [{'total' :p.total},{'hp':p.hp}, {'attack':p.attack},{'defense':p.defense},{'speed':p.speed}]

        characters.insert({'number':p.pokemonNumber,
                            'name': p.name,
                           'types': types,
                            'attributes': attributes,
                           'special': special,
                           'generation': p.generation,
                           'legendary': p.legendary })

    print('one to few: done')


def oneToMany(entry):
    """the following function iterates through the data set and creates a one:many cardinality for the pokemon characters"""
    poketypes = db.poketypes  # create the document (table)

    poketypes.remove({})  # remove all from the set each time function is ran



    # foreach pokemon add them to the document in the onetomany cardinality
    for p in entry:
        """
        format for the one to few 
        pokemon.poketypes{
                             bug:[ number:{},name:{}],
                            dark: [ number:{},name:{}],
                            dragon: [ number:{},name:{}],
                            electric: [ number:{},name:{}],
                            fairy: [ number:{},name:{}],
                            fighting:[ number:{},name:{}],
                            fire: [ number:{},name:{}],
                            flying: [ number:{},name:{}],
                            ghost: [ number:{},name:{}],
                            grass: [ number:{},name:{}],
                            ground: [ number:{},name:{}],
                            ice: [ number:{},name:{}],
                            normal: [ number:{},name:{}],
                            poison: [ number:{},name:{}],
                            psychic: [ number:{},name:{}],
                            rock: [ number:{},name:{}],
                            steel:[ number:{},name:{}],
                            water: [ number:{},name:{}],

                      
                        }

        """
        #group by type - fire
        if(p.type1 == 'Fire' or p.type2 == 'Fire'):
            fire = [{'number':p.pokemonNumber},{'name':p.name}]

            poketypes.insert({
                    'type':'fire',
                    'pokemon':fire
            })



        # #group by type - Water
        if(p.type1 == 'Water' or p.type2 == 'Water'):
            water = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'water',
                'pokemon': water
            })


        # # group by type - Pyschic
        if (p.type1 == 'Psychic' or p.type2 == 'Psychic'):
            psychic = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'psychic',
                'pokemon': psychic
            })

        # group by type - ice
        if (p.type1 == 'Ice' or p.type2 == 'Ice'):
            ice = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'ice',
                'pokemon': ice
            })


        # # group by type - grass
        if (p.type1 == 'Grass' or p.type2 == 'Grass'):
            grass = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'grass',
                'pokemon': grass
            })


        # group by type - rock
        if (p.type1 == 'Rock' or p.type2 == 'Rock'):

            rock = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'rock',
                'pokemon': rock
            })

        # group by type - bug
        if (p.type1 == 'Bug' or p.type2 == 'Bug'):

            bug = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'bug',
                'pokemon': bug
            })

        # group by type - dar
        if (p.type1 == 'Dark' or p.type2 == 'Dark'):

            dark = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'dark',
                'pokemon': dark
            })

        # group by type - dragon
        if (p.type1 == 'Dragon' or p.type2 == 'Dragon'):

            dragon = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'dragon',
                'pokemon': dragon
            })

        # group by type - electric
        if (p.type1 == 'Electric' or p.type2 == 'Electric'):
            electric = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'electric',
                'pokemon': electric
            })

        # group by type - electric
        if (p.type1 == 'Fighting' or p.type2 == 'Figthing'):
            fighting = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'fighting',
                'pokemon': fighting
            })

        # group by type - fairy
        if (p.type1 == 'Fairy' or p.type2 == 'Fairy'):
            fairy = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'fairy',
                'pokemon': fairy
            })

        # group by type - flying
        if (p.type1 == 'Flying' or p.type2 == 'Flying'):
            flying = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'flying',
                'pokemon': flying
            })

        # group by type - ghost
        if (p.type1 == 'Ghost' or p.type2 == 'Ghost'):
            ghost = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'ghost',
                'pokemon': ghost
            })

        # group by type - Ground
        if (p.type1 == 'Ground' or p.type2 == 'Ground'):
            ground = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'ground',
                'pokemon': ground
            })

        # group by type - normal
        if (p.type1 == 'Normal' or p.type2 == 'Normal'):
            normal = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'normal',
                'pokemon': normal
            })

        # group by type - poison
        if (p.type1 == 'Poison' or p.type2 == 'Poison'):
            poison = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'poison',
                'pokemon': poison
            })

        # group by type - steel
        if (p.type1 == 'Steel' or p.type2 == 'Steel'):
            steel = [{'number': p.pokemonNumber}, {'name': p.name}]
            poketypes.insert({
                'type': 'steel',
                'pokemon': steel
            })
    print('one to many: done')


def oneToSquillions(entry):
    """the following function iterates through the data set and creates a one:squillions cardinality for the pokemon characters"""
    generations = db.generations  # create the document (table)

    generations.remove({})  # remove all from the set each time function is ran

    # foreach pokemon add them to the document in the onetosquillions cardinality


    for p in entry:

        """
        format for the one to few 
        pokemon.generations{
                            generaton1:{generation:1},
                            pokemon:[
                                   number:{},
                                   name:{},
                                   legendary:{},
                                   
                                    
                                    
                            }
        
        """

        if (p.generation == 1):
            gen1.append({'pokemon number':p.pokemonNumber, 'name':p.name, 'legendary': p.legendary, 'power': p.total, 'types': [p.type1,p.type2]})

        if (p.generation == 2):
            gen2.append({'pokemon number':p.pokemonNumber, 'name':p.name, 'legendary': p.legendary, 'power': p.total, 'types': [p.type1,p.type2]})

        if (p.generation == 3):
            gen3.append({'pokemon number':p.pokemonNumber, 'name':p.name, 'legendary': p.legendary, 'power': p.total, 'types': [p.type1,p.type2]})

        if (p.generation == 4):
            gen4.append({'pokemon number':p.pokemonNumber, 'name':p.name, 'legendary': p.legendary, 'power': p.total, 'types': [p.type1,p.type2]})

        if (p.generation == 5):
            gen5.append({'pokemon number':p.pokemonNumber, 'name':p.name, 'legendary': p.legendary, 'power': p.total, 'types': [p.type1,p.type2]})

        if (p.generation == 6):
            gen6.append({'pokemon number':p.pokemonNumber, 'name':p.name, 'legendary': p.legendary, 'power': p.total, 'types': [p.type1,p.type2]})

    generations.insert({
        'generation':1,
        'pokemon':gen1
    })

    generations.insert({
        'generation': 2,
        'pokemon': gen2
    })

    generations.insert({
        'generation': 3,
        'pokemon': gen3
    })

    generations.insert({
        'generation': 4,
        'pokemon': gen4
    })

    generations.insert({
        'generation': 5,
        'pokemon': gen5
    })

    generations.insert({
        'generation': 6,
        'pokemon': gen6
    })

    print('one to squillions: done')





entry = []
getCSV(entry)
#entry = entry[1::] #remove the metadata from the dataset

#Question 2: one to few
oneToFew(entry)

#Question 2: one to many
oneToMany(entry)

#Question 2: one to squillions
oneToSquillions(entry)








