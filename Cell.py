from abc import ABCMeta, abstractmethod

class Cell:
    def __init__(self, x, y):
       self.x = x
       self.y = y
       self.clicked = False
       self.symbol = '?'

    @abstractmethod
    def onClick(self):
        pass

    @abstractmethod
    def gameOver(self) -> bool:
        pass
