from abc import abstractmethod

class Animal:
    def __init__(self):
        pass
    @abstractmethod
    def speed(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass

class Koala(Animal):
    def __init__(self):
        pass
    def speed(self):
        print('Koala moves with the speed 1.12 metres/second.')
    def weight(self):
        print('Koala\'s weight is between 4 and 15 kg')
    def eat(self):
        print('Koala eats about 1 kg eucalyptus leaves a day.')
    def sleep(self):
        print('Koala sleeps in average 14 hours a day.')

class Cheetah(Animal):
    def __init__(self):
        pass
    def speed(self):
        print('Cheetah moves with the speed 80-130 km/h.')
    def size(self):
        print('Cheetah is 1.1 - 1.5 metres long.')
    def eat(self):
        print('Cheetah eats about 2.8 - 3.5 kg of meat a day.')
    def sleep(self):
        print('Koala sleeps in average 12 hours a day.')

koala1 = Koala()
koala1.speed()
koala1.weight()
koala1.eat()
koala1.sleep()
print()
cheetah1 = Cheetah()
cheetah1.speed()
cheetah1.size()
cheetah1.eat()
cheetah1.sleep()