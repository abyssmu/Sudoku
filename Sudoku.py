import math
import random

def checkCol(b, colNum):
    c = getCol(b, colNum)
    n = len(c)
    col = [0] * n

    for i in range(0, n):
        col[i] = i + 1
    
    for i in range(0, n):
        pos = int(c[i]) - 1
        if(col[pos] != 0):
            col[pos] = 0
        else:
            return 0
        
    return 1

def checkSquare(b, sqNum):
    s = getSquare(b, sqNum)
    n = len(s)
    square = [0] * n

    for i in range(0, n):
        square[i] = i + 1
    
    for i in range(0, n):
        pos = int(s[i]) - 1
        if(square[pos] != 0):
            square[pos] = 0
        else:
            return 0
        
    return 1

def checkRow(b, rowNum):
    r = getRow(b, rowNum)
    n = len(r)
    row = [0] * n

    for i in range(0, n):
        row[i] = i + 1

    for i in range(0, n):
        pos = int(r[i]) - 1
        if(row[pos] != 0):
            row[pos] = 0
        else:
            return 0
        
    return 1

def countNums(b):
    size = len(b)
    n = math.trunc(math.sqrt(size))
    arr = [0] * n
    
    for i in range(0, size):
        val = int(b[i])
        if(val != 0):
            arr[val - 1] += 1
                
    return arr

def createRandArr(numCount):
    count = subN(numCount)
    numSum = int(sum(count))
    randArr = [0] * numSum
    pos = 0
    n = len(count)

    while numSum > 0:
        val = random.randint(1, n) #Between 1 and n

        if(count[val - 1] != 0):
            randArr[pos] = val

            count[val - 1] -= 1

            pos += 1
        
        numSum = sum(count)

    return randArr

def getCol(b, x):
    n = math.trunc(math.sqrt(len(b)))
    col = [0] * n

    for i in range(0, n):
        pos = i * n + x

        col[i] = b[pos]

    return col

def getSquare(b, sq):
    n = math.trunc(math.sqrt(len(b)))
    sqN = math.trunc(math.sqrt(n))
    square = [0] * n
    x = sq % sqN
    y = math.trunc(sq / sqN)
    start = (y * n * sqN) + (x * sqN)
    p = 0

    for i in range(0, sqN):
        for j in range(0, sqN):
            off = i * n + j
            pos = start + off

            square[p] = b[pos]

            p += 1

    return square

def getRow(b, y):
    n = math.trunc(math.sqrt(len(b)))
    row = [0] * n

    for i in range(0, n):
        pos = y * n + i

        row[i] = b[pos]

    return row

def insert(b, r):
    size = len(b)
    newBoard = [0] * size

    for i in range(0, size):
        newBoard[i] = b[i]

        rPos = 0

    for i in range(0, size):
        if(newBoard[i] == '0'):
            newBoard[i] = r[rPos]

            rPos += 1

    return newBoard

def isSolved(b):
    n = math.trunc(math.sqrt(len(b)))

    for i in range(0, n):
        col = bool(checkCol(b, i))
        square = bool(checkSquare(b, i))
        row = bool(checkRow(b, i))
        results = col and square and row

        if(not results):
            return 0

        i += 1

    return 1

def printBoard(b):
    i = 0
    size = len(b)
    enter = math.trunc(math.sqrt(size))
    tab = math.trunc(math.pow(size, 1 / 4))
    output = ""

    for i in range(0, size):
        output += str(b[i]) + " "

        if((i % tab) == (tab - 1)):
            output += '\t'

        if((i % enter) == (enter - 1)):
            output += '\n'

        # if((i % (enter * 3)) == ((enter * 3) - 1)):
        #     output += '\n'

    print(output)

    return

def readBoard():
    b = open("Sudoku.txt").read().strip('\n').replace(',', '').split()

    return b

def subN(intArr):
    n = len(intArr)
    newArr = [0] * n

    for i in range(0, n):
        newArr[i] = n - intArr[i]

    return newArr

def sum(intArr):
    n = len(intArr)
    total = 0

    for i in range(0, n):
        total += intArr[i]
    
    return total