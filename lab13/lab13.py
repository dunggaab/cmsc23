from abc import ABC, abstractmethod

class Headline:
    def __init__(self, headline:str, details:str, source:str):
        self.__headline = headline
        self.__details = details
        self.__source = source

    def __str__(self) -> str:
        return "%s(%s)\n%s" % (self.__headline, self.__source, self.__source)

class Weather:
    def __init__(self, temp:float, humidity:float, outlook:str):
        self.__temp = temp
        self.__humidity = humidity
        self.__outlook = outlook

    def __str__(self) -> str:
        return "%s: %.1fC %.1f" % (self.__outlook, self.__temp, self.__humidity)


class Subscriber(ABC):
    @abstractmethod
    def update(self,newHeadline:Headline, newWeather:Weather):
        pass
    
class PushNotifier:
    def __init__(self,currentHeadline:Headline, currentWeather:Weather):
        self.__currentHeadline =currentHeadline
        self.__currentWeather =currentWeather        
        self.__subscribers = []

    def changeHeadline(self, newHeadline:Headline):
        self.__currentHeadline = newHeadline
        self.notifySubscribers()

    def changeWeather(self, newWeather:Headline):
        self.__currentWeather = newWeather
        self.notifySubscribers()

    def subscribe(self, newSubscriber):
        self.__subscribers.append(newSubscriber)
        newSubscriber.update(self.__currentHeadline,self.__currentWeather)

    def unsubscribe(self, exSubscriber):
        if exSubscriber in self.__subscribers:
            self.__subscribers.remove(exSubscriber)

    def notifySubscribers(self):
        for subsribers in self.__subscribers:
            subsribers.update(self.__currentHeadline,self.__currentWeather)

class EmailSubscriber(Subscriber):
    def __init__(self,emailAddress:str):
        self.__emailAddress = emailAddress

    def update(self,newHeadline:Headline,newWeather:Weather): 
        print("send email to: %s " % self.__emailAddress)
        print("new headline: %s" % newHeadline)
        print("new weather %s" % newWeather)

class FileLogger(Subscriber):
    def __init__(self,filename):
        self.__filename = filename

    def update(self,newHeadline:Headline,newWeather:Weather):
        with open (self.__filename, "a+") as f:
            f.write ("new headline %s\n" % newHeadline)
            f.write ("new weather %s\n" % newWeather)

w = Weather (29, 0.1, "Sunny")
h= Headline ("Today is Sunny", "mySource", "Detailssss....")
p= PushNotifier (h,w)
e= EmailSubscriber("raidenshogun@gmail.com")
f= FileLogger("log.in")

p.subscribe(e)
p.subscribe(f)


p.changeWeather(Weather(19, 0.1, "Very Cold"))
p.changeWeather(Weather(23, 0.1, "Cloudy"))
