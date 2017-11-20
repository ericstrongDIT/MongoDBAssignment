"""The following class is to store each line from the CSV file"""
class CSV_Entry(object):

    def __init__(self, lines):
        self.pokemonNumber = int(lines[0])
        self.name = lines[1]
        self.type1 = lines[2]
        self.type2 = lines[3]
        self.total = int(lines[4])
        self.hp = int(lines[5])
        self.attack = int(lines[6])
        self.defense = int(lines[7])
        self.spAtk = int(lines[8])
        self.spDef = int(lines[9])
        self.speed = int(lines[10])
        self.generation = int(lines[11])
        self.legendary = lines[12]
        size = len(self.legendary)
        self.legendary = self.legendary[:size-1]



    def __str__(self):
        return "\nnumber: {} \npokemon name: {} \ntype 1: {} \ntype 2: {} \ntotal: {} \nLegendary: {}".format(str(self.pokemonNumber),self.name, self.type1, self.type2, str(self.total), self.legendary)
        #return "\npokemon number: {}\nname: {} \ntype 1:{} \ntype 2: {}\n total: {}\n hp: {}\n attack: {}\ndefense:{} \nsp. Atk: {}\n sp.Def: {}\n Speed: {}\n Generation: {}\n Legendary: {}".format(self.pokemonNumber, self.type1,self.type2,self.total,self.attack, self.defense, self.spAtk, self.spDef,self.speed, self.generation, self.legendary)
