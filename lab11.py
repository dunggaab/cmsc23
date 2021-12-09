from abc import ABC,abstractmethod

class State(ABC):
    @abstractmethod
    def compress(self):
        pass
    @abstractmethod
    def release(self):
        pass
    @abstractmethod
    def heat(self):
        pass
    @abstractmethod
    def cool(self):
        pass
    @abstractmethod
    def __str__(self)->str:
        pass

class Matter:
    def __init__(self,name:str):
        self.__name = name
        self.__state = LiquidState(self)
    def changeState(self,newState:State):
        self.__state = newState
    def compress(self):
        self.__state.compress()
    def release(self):
        self.__state.release()
    def heat(self):
        self.__state.heat()
    def cool(self):
        self.__state.cool()
    def __str__(self)->str:
        return "%s is currently a %s" % (self.__name,self.__state)

class LiquidState(State):
    def __init__(self,matter:Matter):
        self.__matter = matter
    def compress(self):
        print ("compressing")
        self.__matter.changeState(SolidState(self.__matter))
    def release(self):
        print ("releasing")
        self.__matter.changeState(GaseousState(self.__matter))
    def heat(self):
        print ("vaporizing")
        self.__matter.changeState(GaseousState(self.__matter))
    def cool(self):
        print ("freezing")
        self.__matter.changeState(SolidState(self.__matter))
    def __str__(self):
        return "liquid"

class SolidState(State):
    def __init__(self,matter:Matter):
        self.__matter = matter
    def compress(self):
        print ("compressing")
    def release(self):
        print ("releasing")
        self.__matter.changeState(LiquidState(self.__matter))
    def heat(self):
        print ("melting")
        self.__matter.changeState(LiquidState(self.__matter))
    def cool(self):
        print ("cooling")
    def __str__(self):
        return "solid"

class GaseousState(State):
    def __init__(self,matter:Matter):
        self.__matter = matter
    def compress(self):
        print ("compressing")
        self.__matter.changeState(Liquid(self.__matter))
    def release(self):
        print ("releasing")
    def heat(self):
        print ("heating")
    def cool(self):
        print ("condensing")
        self.__matter.changeState(LiquidState(self.__matter))
    def __str__(self):
        return "gas"



water:Matter = Matter ("Water")
print(water)
water.compress()
print(water)
water.heat()
print(water)
water.release()
print(water)
water.heat()
print(water)
water.cool()
print(water)
