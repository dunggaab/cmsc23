from abc import ABC, abstractmethod
from random import randint


class Lizalflos(ABC):
    @abstractmethod
    def throwBoomerang(self):
        pass
    @abstractmethod    
    def hide(self):
        pass
    
class Moblin(ABC):
    @abstractmethod
    def stab(self):
        pass
    @abstractmethod    
    def kick(self):
        pass

class Bokoblin(ABC):
    @abstractmethod
    def bludgeon(self):
        pass
    @abstractmethod    
    def defend(self):
        pass

class Dungeon(ABC):
    @abstractmethod
    def newLizalflos(self) -> Lizalflos: #builds a product A
        pass
    @abstractmethod
    def newMoblin(self) -> Moblin: #builds a product B
        pass
    @abstractmethod
    def newBokoblin(self) -> Bokoblin: #builds a product B
        pass

class Monster(ABC):
    @abstractmethod
    def announce(self):
        pass
    @abstractmethod    
    def move(self):
        pass

    ##DUNGEON

class EasyDungeon(Dungeon):
    def newBokoblin(self) -> Bokoblin:
        return NormalBokoblin()

    def newMoblin(self) -> Moblin:
        return NormalMoblin()
    
    def newLizalflos(self) -> Lizalflos:
        return NormalLizalflos()

class MediumDungeon(Dungeon):
    def newBokoblin(self) -> Bokoblin:
        return BlueBokoblin()

    def newMoblin(self) -> Moblin:
        return BlueMoblin()
    
    def newLizalflos(self) -> Lizalflos:
        return BlueLizalflos()

class HardDungeon(Dungeon):
    def newBokoblin(self) -> Bokoblin:
        return SilverBokoblin()

    def newMoblin(self) -> Moblin:
        return SilverMoblin()
    
    def newLizalflos(self) -> Lizalflos:
        return SilverLizalflos()

    ###Normal Monster

class NormalBokoblin(Bokoblin):
    def bludgeon(self):
        print("Normal Bokoblin bludgeons you with a boko club for 1 damage")
    def defend(self):
        print("Normal Bokoblin defends itself with a boko shield")
    def announce(self):
        print("A Normal Bokoblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()

class NormalMoblin(Moblin):
    def stab(self):
        print("Normal Moblin stabs you with a spear for 3 damage")
    def kick(self):
        print("Normal Moblin kicks you for 1 damage")
    def announce(self):
        print("A Normal Moblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class NormalLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Normal Lizalflos throws its lizal boomerang at you for 2 damage")
    def hide(self):
        print("Normal Lizalflos camouflages itself")
    def announce(self):
        print("A Normal Lizalflos appeared")
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

    ### Blue
class BlueBokoblin(Bokoblin):
    def bludgeon(self):
        print("Blue Bokoblin bludgeons you with a spiked boko club for 2 damage")
    def defend(self):
        print("Blue Bokoblin defends itself with a spiked boko shield")
    def announce(self):
        print("A Blue Bokoblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()

class BlueMoblin(Moblin):
    def stab(self):
        print("Blue Moblin stabs you with a rusty halberd for 5 damage")
    def kick(self):
        print("Blue Moblin kicks you for 2 damage")
    def announce(self):
        print("A Blue Moblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class BlueLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Blue Lizalflos throws its forked boomerang at you for 3 damage")
    def hide(self):
        print("Blue Lizalflos camouflages itself")
    def announce(self):
        print("A Blue Lizalflos appeared")
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

    ### Silver
class SilverBokoblin(Bokoblin):
    def bludgeon(self):
        print("Silver Bokoblin bludgeons you with a dragonbone boko club for 5 damage")
    def defend(self):
        print("Silver Bokoblin defends itself with a dragonbone boko shield")
    def announce(self):
        print("A Silver Bokoblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.bludgeon()
        else:
            self.defend()

class SilverMoblin(Moblin):
    def stab(self):
        print("Silver Moblin stabs you with a knight's halberd for 10 damage")
    def kick(self):
        print("Silver Moblin kicks you for 3 damage")
    def announce(self):
        print("A Silver Moblin appeared")
    def move(self):
        if randint(1,3) > 1:
            self.stab()
        else:
            self.kick()

class SilverLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Silver Lizalflos throws its tri-boomerang at you for 7 damage")
    def hide(self):
        print("Silver Lizalflos camouflages itself")
    def announce(self):
        print("A Silver Lizalflos appeared")
    def move(self):
        if randint(1,3) > 1:
            self.throwBoomerang()
        else:
            self.hide()

class Encounter:
    def __init__(self, dungeon:Dungeon):
        self.__enemies = []
        self.__dungeon = dungeon 
        for i in range(randint(0,8)):
            r = randint(1,3)
            if r == 1:
                self.__enemies.append(self.__dungeon.newBokoblin())
            elif r==2:
                self.__enemies.append(self.__dungeon.newMoblin())
            else:
                self.__enemies.append(self.__dungeon.newLizalflos())

    def announceEnemies(self):
        print("%d monsters appeared" % len(self.__enemies))
        for enemy in self.__enemies:
            enemy.announce()

    def moveEnemies(self):
        for enemy in self.__enemies:
            enemy.move()

easy=EasyDungeon()
round1= Encounter(easy)
round1.announceEnemies()
print()
round1.moveEnemies()
print()
medium=MediumDungeon()
round2= Encounter(medium)
round2.announceEnemies()
print()
round2.moveEnemies()
print()
hard=HardDungeon()
round3= Encounter(hard)
round3.announceEnemies()
print()
round3.moveEnemies()

