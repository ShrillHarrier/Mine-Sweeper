import math
import random
from BombCell import BombCell
from EmptyCell import EmptyCell
from NumberCell import NumberCell

class GameBoard:
    def __init__(self, cellCount, bombCount):
        self.endGame = 0
        self.cellArray = [[0 for x in range(int(math.sqrt(cellCount)))] for y in range(int(math.sqrt(cellCount)))] 
        self.cellCount = cellCount
        self.unClickedCells = cellCount
        self.bombCount = bombCount

        self.generateBombs()
        self.fillCells()

    def generateBombs(self):
       self.bombcellsx = []
       self.bombcellsy = []

       for i in range(0,self.bombCount):
            self.bombcellsx.append(random.randint(0,int(math.sqrt(self.cellCount))-1))
            self.bombcellsy.append(random.randint(0,int(math.sqrt(self.cellCount))-1))

       #print(bombcellsx)
       #print(bombcellsy)
       
       for i in range(0, self.bombCount):
           #print(int(bombcellsx[i]))
           self.cellArray[int(self.bombcellsx[i])][int(self.bombcellsy[i])] = BombCell(int(self.bombcellsx[i]),int(self.bombcellsy[i]))

    def fillCells(self):
        for i in range(0, int(math.sqrt(self.cellCount))):
            for j in range(0, int(math.sqrt(self.cellCount))):
                if(type(self.cellArray[j][i]) is BombCell):
                    self.fillAround(j,i)
                elif(not(type(self.cellArray[j][i]) is NumberCell)):
                    self.cellArray[j][i] = EmptyCell(j,i)

                #self.cellArray[i, j]
    
    def fillAround(self, x, y):
        new_x = (x-1 if x != 0 else x) 
        #print("new_x: ", new_x)
        new_y = (y-1 if y != 0 else y) 
        #print("new_y: ", new_y)

        bound_x = (new_x+2 if (x < math.sqrt(self.cellCount)-1) and (x != 0) else new_x+1)
        #print("bound_x: ", bound_x)
        bound_y = (new_y+2 if y < math.sqrt(self.cellCount)-1 and (y != 0) else new_y+1)
        #print("bound_y: ", bound_y)

        #print()

        for i in range(new_y,bound_y+1):
            for j in range(new_x,bound_x+1):
                if(not(type(self.cellArray[j][i]) is BombCell)):
                    if(type(self.cellArray[j][i]) is NumberCell):
                        self.cellArray[j][i].increaseCount()
                    else:
                        self.cellArray[j][i] = NumberCell(j,i)

    def Turn(self, x, y):
        x = int(x)
        y = int(y)

        if(self.cellArray[x][y].clicked == False):
            self.unClickedCells -= 1
            
        self.cellArray[x][y].onClick()

        if(self.unClickedCells == self.bombCount):
            print("\nYou Win!")
            self.endGame = 1

            for i in range(0,self.bombCount):
                self.cellArray[self.bombcellsx[i]][self.bombcellsy[i]].onClick()

        elif(self.cellArray[x][y].endGame() == True):
            print("\nYou Lose!")
            self.endGame = 1

            for i in range(0,self.bombCount):
                self.cellArray[self.bombcellsx[i]][self.bombcellsy[i]].onClick()

    def printCells(self):
        for i in range(0, int(math.sqrt(self.cellCount))):
            for j in range(0, int(math.sqrt(self.cellCount))):
                print(self.cellArray[j][i].symbol,end=" ")

            print()
    
    def getEndGame(self):
        return self.endGame
