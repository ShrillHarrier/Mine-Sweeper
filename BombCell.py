from Cell import Cell

class BombCell(Cell):
   def __init__(self, x, y):
       super(BombCell, self).__init__(x, y)
    
   def onClick(self):
        self.clicked = True
        self.symbol = 'B'

   def endGame(self) -> bool:
       return True
