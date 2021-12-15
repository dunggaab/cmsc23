from board import Board
from abc import ABC,abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass

class DashUpCommand (Command):
    def __init__(self,board:Board):
        self.__board = board
        self.__backupLocation = board.characterLocation()

    def execute(self):
        while self.__board.canMoveUp():
            self.__board.moveUp()

    def undo(self):
        self.__board.teleportCharacter(self.__backupLocation)

class DashRightCommand (Command):
    def __init__(self,board:Board):
        self.__board = board
        self.__backupLocation = board.characterLocation()

    def execute(self):
        while self.__board.canMoveRight():
            self.__board.moveRight()

    def undo(self):
        self.__board.teleportCharacter(self.__backupLocation)

class DashLeftCommand (Command):
    def __init__(self,board:Board):
        self.__board = board
        self.__backupLocation = board.characterLocation()

    def execute(self):
        while self.__board.canMoveLeft():
            self.__board.moveLeft() 

    def undo(self):
        self.__board.teleportCharacter(self.__backupLocation)

class DashDownCommand (Command):
    def __init__(self,board:Board):
        self.__board = board
        self.__backupLocation = board.characterLocation()

    def execute(self):
        while self.__board.canMoveDown():
            self.__board.moveDown()

    def undo(self):
        self.__board.teleportCharacter(self.__backupLocation)
