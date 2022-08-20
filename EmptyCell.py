from Cell import Cell

class EmptyCell(Cell):
   def __init__(self, x, y):
       super(EmptyCell, self).__init__(x, y)
    
   def onClick(self):
        self.clicked = True
        self.symbol = 'E'

   def endGame(self) -> bool:
       return False