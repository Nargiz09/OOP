class Animals:
    def __init__(self, animal_species, animal_color ):
        self.species = animal_species
        self.color = animal_color

    def description(self):
        print(self.species, self.color)

    def isEndemic(self):
        print(self.species, 'is endemic ')

    def _isDomestic(self, YesNo):
        if YesNo == 'Yes':
            print(self.species, 'is a domestic animal')
        elif YesNo == 'No':
            print(self.species, 'is a wild animal')

    def max_speed(self, speed):
        print(self.species + ' moves with max speed: ' + str(speed) + ' km/h')

animal2 = Animals('Kangaroo', 'Red')
animal2.description()
animal2.max_speed(70)
animal2._isDomestic('No')
animal2.isEndemic()
print()