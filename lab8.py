from abc import ABC, abstractmethod
from datetime import date,timedelta

class Order:
    def __init__(self,productName:str, productPrice:float):
        self.__productName = productName
        self.__productPrice = productPrice
    def orderString(self) -> str:
        return "%s P%.2f" % (self.__productName,self.__productPrice)
    def price(self) -> float:
        return self.__productPrice

class Delivery(ABC):
    @abstractmethod
    def estimatedDeliveryDate(self,processDate:date) -> float:
        pass
    @abstractmethod
    def deliveryFee(self) -> float:
        pass
    @abstractmethod
    def deliveryDetails(self) -> str:
        pass
    @abstractmethod
    def changeDeliveryStatus(self,newStatus:str):
        pass

class StandardDelivery(Delivery):
    def __init__(self,location:str):
        self.__location = location
        self.__deliveryStatus = "Processing"
    def estimatedDeliveryDate(self,processDate:date) -> float:
        return processDate + timedelta(days = 7)
    def deliveryFee(self) -> float:
        return 500
    def deliveryDetails(self) -> str:
        r = "STANDARD DELIVERY\nDELIVER TO:%s\nDELIVERY STATUS: %s\nDELIVERY FEE: P%.2f" % (self.__location,self.__deliveryStatus,self.deliveryFee())
        return r
    def changeDeliveryStatus(self,newStatus:str):
        self.__deliveryStatus = newStatus
        
class ExpressDelivery(Delivery):
    def __init__(self,location:str):
        self.__location = location
        self.__deliveryStatus = "Processing"
    def estimatedDeliveryDate(self,processDate:date) -> float:
        return processDate + timedelta(days = 1)
    def deliveryFee(self) -> float:
        return 1000
    def deliveryDetails(self) -> str:
        r = "EXPRESS DELIVERY\nDELIVER TO:%s\nDELIVERY STATUS: %s\nDELIVERY FEE: P%.2f" % (self.__location,self.__deliveryStatus,self.deliveryFee())
        return r
    def changeDeliveryStatus(self,newStatus:str):
        self.__deliveryStatus = newStatus

class Shipment:
    def __init__(self, orderList:[Order], processDate: date, location):
        self._orderList = orderList
        self._processDate = processDate
        self._delivery = self.newDelivery(location)

    def totalPrice(self) -> str:
        t = 0.0
        for order in self._orderList:
            t+=order.price()
        return t

    def shipmentDetails(self) -> str:

        r = "ORDERS:" + str(self._processDate) + "\n"
        for order in self._orderList:
            r += order.orderString() + "\n"
        r += "\n"
        r += "TOTAL PRICE OF ORDERS: P"  + str(self.totalPrice()) + "\n"
        r += self._delivery.deliveryDetails() + "\n\n"
        r += "PRICE WITH DELIVERY FEE : P" + str(self.totalPrice()+self._delivery.deliveryFee()) + "\n"
        r += "ESTIMATED DELIVERY DATE: " + str(self._delivery.estimatedDeliveryDate(self._processDate)) + "\n"
        return r    

    def newDelivery(self,location:str) -> Delivery:
        return StandardDelivery(location)

class ExpressShipment (Shipment):
    
    def newDelivery(self,location:str) -> Delivery:
        return ExpressDelivery(location)

o1 = [Order("Aespa Savage 1st Mini Album - P.O.S. Version",750),Order("NCT127 Favorite 3rd Repackage Album",900),Order("NCT Dream Hot Sauce 1st Album",600)]
o2 = [Order("Red Velvet Queendom",1000),Order("Twice Alcohol Free",950)]
## standard delivery
sd:Shipment = Shipment(o1,date(2021,12,1),"Lapu-Lapu City")
print(sd.shipmentDetails())

#express delivery
ed:Shipment = ExpressShipment(o2,date(2021,12,1),"Cebu City")
print(ed.shipmentDetails())
