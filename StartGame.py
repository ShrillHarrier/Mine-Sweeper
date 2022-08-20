from GameBoard import GameBoard

def start():
    boardLength = 6
    bombCount = 5
    _game = GameBoard(boardLength*boardLength, bombCount)
    
    while(_game.getEndGame() == 0):
        print()
        
        _game.printCells()

        x = int(input("Enter x-coord: \n"))
        y = int(input("Enter y-coord: \n"))

        if((x > boardLength-1) or (x < 0) or (y > boardLength-1) or (y < 0)):
            print("Out of range")
            continue

        _game.Turn(x,y)

    _game.printCells()

start()

