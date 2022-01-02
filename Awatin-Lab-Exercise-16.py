from abc import ABC,abstractmethod

class Sentence:
    def __init__(self,words:[str]):
        self.__words = words

    def __str__(self) -> str:
        sentenceString = ""
        for word in self.__words:
            sentenceString += word + " "
        return sentenceString[:-1]


class FormattedSentence(ABC,Sentence):
    def __init__(self, wrappedSentence: Sentence):
        self._wrappedSentence = wrappedSentence

    @abstractmethod
    def __str__(self) -> str:
        pass

class BorderedSentence (FormattedSentence):
    
    def __str__(self) -> str:
        borderline = "-" * (len(str(self._wrappedSentence))+2)
        return borderline + "\n|"+str(self._wrappedSentence)+"|\n" +borderline 

class FancySentence (FormattedSentence):
    
    def __str__(self) -> str:
        return "-+" + str(self._wrappedSentence) + "+-"

class UpperCaseSentence (FormattedSentence):
    
    def __str__(self) -> str:
        return str(self._wrappedSentence).upper()

s= Sentence (["hey", "there"])
print (s)
print (BorderedSentence(s))
print (FancySentence (UpperCaseSentence(s)))
print (UpperCaseSentence(BorderedSentence(s)))
print (BorderedSentence (FancySentence(s)))
print (FancySentence (BorderedSentence(s)))
print (FancySentence (UpperCaseSentence(s)))
