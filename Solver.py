import os
import random
import Sudoku
import time

board = Sudoku.readBoard()
numCount = Sudoku.countNums(board)
randArr = Sudoku.createRandArr(numCount)

solved = 0
tempBoard = board

while(not bool(solved)):
    tempBoard = Sudoku.insert(board, randArr)
    #Sudoku.printBoard(tempBoard)
    results = bool(Sudoku.isSolved(tempBoard))

    print(results)

    if(results):
        solved = 1
    else:
        random.shuffle(randArr)

    #time.sleep(0.05)
    #os.system('cls')

Sudoku.printBoard(tempBoard)
print("Solved.")