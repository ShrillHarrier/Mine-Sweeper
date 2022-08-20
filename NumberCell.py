from Cell import Cell

class NumberCell(Cell):
   def __init__(self, x, y):
       super(NumberCell, self).__init__(x, y)
       self.symbolToBe = 1
    
   def onClick(self):
        self.clicked = True
        self.symbol = self.symbolToBe
    
   def increaseCount(self):
        self.symbolToBe += 1

   def endGame(self) -> bool:
       return False