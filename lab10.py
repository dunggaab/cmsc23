from abc import ABC,abstractmethod

class Fraction:
    def __init__(self,num:int,denom:int):
        self.__num = num
        self.__denom = denom
    def num(self):
        return self.__num
    def denom(self):
        return self.__denom
    def __str__(self) -> str:
        return str(self.__num) + "/" + str(self.__denom)

class Operation(ABC):
    @abstractmethod
    def execute(self,left:Fraction, right:Fraction)->Fraction:
        pass
    @abstractmethod
    def __str__(self):
        pass
    
class Addition(Operation):
    def execute(self,left:Fraction, right:Fraction)->Fraction:
        if (left.denom()==right.denom()):
            num = left.num() + right.num()
            denom = left.denom()
        else:
            denom= left.denom() * right.denom()
            num= (((denom//left.denom())*left.num())+((denom//right.denom())*right.num()))
        return Fraction(num,denom)
    def __str__(self) -> str:
        return "+"

class Subtraction(Operation):
    def execute(self,left:Fraction, right:Fraction)->Fraction:
        if (left.denom()==right.denom()):
            num = left.num() - right.num()
            denom = left.denom()
        else:
            denom= left.denom() * right.denom()
            num= (((denom//left.denom())*left.num())-((denom//right.denom())*right.num()))
        return Fraction(num,denom)
    def __str__(self) -> str:
        return "-"

class Multiplication(Operation):
    def execute(self,left:Fraction, right:Fraction)->Fraction:
        num = left.num() * right.num()
        denom = left.denom() * right.denom()
        return Fraction(num,denom)
    def __str__(self) -> str:
        return "*" 

class Division(Operation):
    def execute(self,left:Fraction, right:Fraction)->Fraction:
        num = left.num() * right.denom() 
        denom = left.denom() *right.num() 
        return Fraction(num,denom)
    def __str__(self) -> str:
        return "/"
    
class Calculation:
    def __init__(self,left:Fraction,right:Fraction,operation:Operation): 
        self.__left = left
        self.__right = right
        self.__operation = operation 
        self.__answer = self.__operation.execute(self.__left,self.__right)

    def __str__(self):
        return str(self.__left) + " " + str(self.__operation) + " " + str(self.__right) + " = " + str(self.__answer)

###ADDITION
c0= Calculation (Fraction(1,3),Fraction(4,5),Addition())
print(c0)
###SUBTRACTION
c1= Calculation (Fraction(1,4),Fraction(1,5),Subtraction())
print(c1)
###MULTIPLICATION
c2= Calculation (Fraction(1,2),Fraction(2,3),Multiplication())
print(c2)
###DIVISION
c3= Calculation (Fraction(4,5),Fraction(2,6),Division())
print(c3)


