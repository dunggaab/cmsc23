from abc import ABC, abstractmethod

class Date:
    def __init__(self, month:int, day:int, year:int):
        self.__month = month
        self.__day = day
        self.__year = year
    def mdyFormat(self) -> str:
        return str(self.__month) + "/" + str(self.__day) + "/" + str(self.__year)
    def countLeap(days):
        years = days.__year
        
        if (days.__month <= 2):
            years -= 1

        return int(years / 4) - int(years / 100) + int(years / 400)
    def daysCalculator (d1, d2):

        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


        n1 = d1.__year * 365 + d1.__day
 
        for i in range(0, d1.__month - 1):
            n1 += monthDays[i]
 
        n1 += Date.countLeap(d1)
 
        n2 = d2.__year * 365 + d2.__day
        
        for i in range(0, d2.__month - 1):
            n2 += monthDays[i]
            
        n2 += Date.countLeap(d2)

        return (n2 - n1)

       

class Page:
    def __init__(self, sectionHeader:str, body: str):
        self.__sectionHeader = sectionHeader
        self.__body = body

class BorrowableItem(ABC):
    @abstractmethod
    def uniqueItemId(self) -> int:
        pass
    @abstractmethod
    def commonName(self) -> str:
        pass



class Book(BorrowableItem):
    def __init__(self, bookId:int, title:str, author:str, publishDate:Date, pages: [Page]):
        self.__bookId = bookId
        self.__title = title
        self.__publishDate = publishDate
        self.__author = author
        self.__pages = pages
    def coverInfo(self) -> str:
        return "Title: " + self.__title + "\nAuthor: " + self.__author
    def uniqueItemId(self) -> int:
        return self.__bookId
    def commonName(self) -> str:
        return "Borrowed Item:" + self.__title + " by " + self.__author

class Periodical(BorrowableItem):
    def __init__(self, periodicalID:int, title:str, issue:Date, pages: [Page]):
        self.__periodicalID = periodicalID
        self.__title = title
        self.__issue = issue
        self.__pages = pages
    def uniqueItemId(self) -> int:
        return self.__periodicalID
    def commonName(self) -> str:
        return self.__title + ": " + self.__issue.mdyFormat()

class PC(BorrowableItem):
    def __init__(self, pcID:int):
        self.__pcID = pcID
    def uniqueItemId(self) -> int:
        return self.__pcID
    def commonName(self) -> str:
        return "PC" + str(self.__pcID)

class LibraryCard:
    def __init__(self, idNumber: int, name: str, borrowedItems: {BorrowableItem:Date}):
        self.__idNumber = idNumber
        self.__name = name
        self.__borrowedItems = borrowedItems
    def borrowItem(self,book:BorrowableItem, date:Date):
        self.__borrowedItems[book] = date
    def borrowerReport(self) -> str:
        r:str = self.__name + "\n"
        for borrowedItem in self.__borrowedItems:
            r = r + borrowedItem.commonName() + ", borrow date:" + self.__borrowedItems[borrowedItem].mdyFormat() + "\n"
        return r
    def returnItem(b:BorrowableItem):
        if b in self.__borrowedItems:
            del self.__borrowedItems[b]
    def penalty(self, b:BorrowableItem, today:Date)-> float:
        r:float
        if isinstance(b,Book) == True:
            r= Date.daysCalculator (self.__borrowedItems[b],today)
            if r>7:
                r=r-7
                return float(r*3.5)
            else:
                return float(0)
        elif isinstance(b,Periodical) == True:
            r= Date.daysCalculator (self.__borrowedItems[b],today)
            if r>1:
                r=r-1
                return float(r*3.5)
            else:
                return float(0)
        elif isinstance(b,PC) == True:
            r= Date.daysCalculator (self.__borrowedItems[b],today)
            if r>0:
                return float(r*3.5)
            else:
                return float(0)

    def itemsDue(self, today:Date)-> [BorrowableItem]:
        items=[]
        for borrowedItem in self.__borrowedItems:
            if isinstance(borrowedItem, Book) == True:
                days= Date.daysCalculator (self.__borrowedItems[borrowedItem],today)
                if days>7:
                    items.append(borrowedItem.commonName())
            elif isinstance(borrowedItem, Periodical) == True:
                days= Date.daysCalculator (self.__borrowedItems[borrowedItem],today)
                if days>1:
                    items.append(borrowedItem.commonName())
            elif isinstance(borrowedItem, PC) == True:
                days= Date.daysCalculator (self.__borrowedItems[borrowedItem],today)
                if days>0:
                    items.append(borrowedItem.commonName())
        return items
    
    def totalPenalty(self, today:Date)-> float:
        r:float
        r=0.0
        for borrowedItem in self.__borrowedItems:
            r+= LibraryCard.penalty(self, borrowedItem, today)
        return float(r)
            

l:LibraryCard = LibraryCard(9982,"John Ochea",{})

b:BorrowableItem = Book(10991,"Corpus Hermeticum", "Hermes Trismegistus", Date(9,1,1991), [])

pe1:BorrowableItem = Periodical(23, "I shall return!", Date(2,23,1879),[])

pc1:BorrowableItem = PC(1239)

l.borrowItem(b,Date(11,10,2021))

l.borrowItem(pe1,Date(11,10,2021))

l.borrowItem(pc1,Date(11,21,2021))

print(l.itemsDue(Date(11,23,2021)))

print(l.penalty(b,Date(11,23,2021)))

print(l.penalty(pe1,Date(11,23,2021)))

print(l.penalty(pc1,Date(11,23,2021)))

print(l.totalPenalty(Date(11,23,2021)))
            
            
