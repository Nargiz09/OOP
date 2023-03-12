class Animals:
    def __init__(self, animal_species, animal_color ):
        self.species = animal_species
        self.color = animal_color
    def description(self):
        print(self.species, self.color)
    def isEndemic(self):
        print(self.species, 'is endemic ')
    def isDomestic(self, YesNo):
        if YesNo == 'Yes':
            print(self.species, 'is a domestic animal')
        elif YesNo == 'No':
            print(self.species, 'is a wild animal')
    def max_speed(self, speed):
        print(self.species + ' moves with max speed: ' + str(speed) + ' km/h')

class Dogs(Animals):
    def __init__(self, species, color, name, age):
        super().__init__(species, color)
        self.name = name
        self.age = age
    def description(self):
        print('species: ' + self.species + '\ncolor: ' + self.color + '\nname: ' + self.name + '\nage: ' + str(
            self.age))
    def trainingCommands(self, YesNo):
        if YesNo == 'Yes':
            print(self.name, 'knows all training commands')
        elif YesNo == 'No':
            print(self.name, '''doesn't know training commands''')

class Cats(Animals):
    def __init__(self,species, color, name, breed, sex):
        super().__init__(species, color)
        self.name = name
        self.breed = breed
        self.sex = sex
    def description(self):
        print('species: ' + self.species + '\nbreed: ' + self.breed + '\ncolor: ' + self.color + '\nsex: ' + self.sex + '\nname: ' + self.name)

class Birds(Animals):
    def __init__(self, species, color, kind, size):
        super().__init__(species, color)
        self.kind = kind
        self.size = size
    def description(self):
        print('species: ' + self.species + '\nkind: ' + self.kind + '\ncolor: ' + self.color + '\nsize: ' + str(
            self.size) + ' sm')

dog1 = Dogs('dog','black', 'Tom', 7)
dog1.description()
dog1.isDomestic('Yes')
dog1.trainingCommands('Yes')
print()
cat1 = Cats('cat', 'white','Bob','British cat', 'boy')
cat1.description()
print()
bird1 = Birds('bird','black', 'eagle', 80)
bird1.description()
bird1.max_speed(320)