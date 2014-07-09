#!/usr/bin/env python
####      Sudoku generator      ####

import random
import time
from collections import defaultdict

class Square(object):
    '''Main class holding the attributes for each square of the sudoku'''

    def __init__(self, x, y):
        self.value = None
        self.x = x
        self.y = y
        self.free = range(1, 10)
        self.region = None

    def addValue(self, value):
        self.value = value
    def addRegion(self, region):
        self.region = region
    def removeFromFreeValues(self, value):
        self.free.remove(value)
    def restoreFree(self):
        self.free = range(1,10)
    def removeValue(self):
        self.value = None

    def getValue(self):
        return self.value
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getFree(self):
        return self.free
    def getRegion(self):
        return self.region

def createBoard():
    board = [ Square(y, x) for x in range(9) for y in range(9) ]
    return board

def defineRegions(board):
    for square in board:
        if square.getX() < 3 and square.getY() < 3:
            square.addRegion(0)
        elif 3 <= square.getX() < 6 and square.getY() < 3:
            square.addRegion(1)
        elif 6 <= square.getX() < 9 and square.getY() < 3:
            square.addRegion(2)
        elif square.getX() < 3 and 3 <= square.getY() < 6:
            square.addRegion(3)
        elif 3 <= square.getX() < 6 and 3 <= square.getY() < 6:
            square.addRegion(4)
        elif 6 <= square.getX() < 9 and 3 <= square.getY() < 6:
            square.addRegion(5)
        elif square.getX() < 3 and 6 <= square.getY() < 9:
            square.addRegion(6)
        elif 3 <= square.getX() < 6 and 6 <= square.getY() < 9:
            square.addRegion(7)
        elif 6 <= square.getX() < 9 and 6 <= square.getY() < 9:
            square.addRegion(8)



def defineXs(board):
    Xdict = {}
    for i in range(9):
        x_squares = []
        for square in board:
            if square.getX() == i:
                x_squares.append(square)
            Xdict[i] = x_squares
    return Xdict


def defineYs(board):
    Ydict = {}
    for i in range(9):
        y_squares = []
        for square in board:
            if square.getY() == i:
                y_squares.append(square)
            Ydict[i] = y_squares
    return Ydict

def defineRegionslist(board):
    regions = {}
    for i in range(9):
        r_squares = []
        for square in board:
            if square.getRegion() == i:
                r_squares.append(square)
            regions[i] = r_squares
    return regions


def checkIfFree(board, current_square):
    free_values = current_square.getFree()
    if len(free_values) < 1:
        return False
    else:
        return True

def setValueOnce(value, current_square):
    current_square.addValue(value)
    current_square.removeFromFreeValues(value)


def checkXValidity(board, current_square):
    sameXlist = defineXs(board)[current_square.getX()]
    sameXlist.remove(current_square)
    x_values = []
    for square in sameXlist:
        x_values.append(square.getValue())
    if current_square.getValue() in x_values:
        return False
    else:
        return True

def checkYValidity(board, current_square):
    sameYlist = defineYs(board)[current_square.getY()]
    sameYlist.remove(current_square)
    y_values = []
    for square in sameYlist:
        y_values.append(square.getValue())
    if current_square.getValue() in y_values:
        return False
    else:
        return True

def checkRegionValidity(board, current_square):
    sameRegionlist = defineRegionslist(board)[current_square.getRegion()]
    sameRegionlist.remove(current_square)
    r_values = []
    for square in sameRegionlist:
        r_values.append(square.getValue())
    if current_square.getValue() in r_values:
        return False
    else:
        return True

def checkConditions(board, square):
    if checkXValidity(board, square) == checkYValidity(board, square) == checkRegionValidity(board, square) == True:
        return True
    else:
        return False


def CreateSudoku():
    board = createBoard()
    defineRegions(board)

    index = 0
    while index < 81:
        current_square = board[index]

        if checkIfFree(board, current_square) == False:
            current_square.restoreFree()
            current_square.removeValue()
            index -= 1
            continue

        value = random.choice(current_square.getFree())
        setValueOnce(value, current_square)

        if checkConditions(board, current_square) == False:
            continue
        else:
            index += 1

    return board


def printSudoku(board):

    line =        "#---+---+---#---+---+---#---+---+---#"
    line_thick =  "#####################################"
    print line

    for s in board:
        if (s.getX() ) % 3 == 0:
            print '#  ',
        elif random.random() > 0.3:
            print '|  ',
        else:
            print '| %d' %(s.getValue()),

        if (s.getX() +1) % 9 == 0:
            if (s.getY() + 1) % 3 == 0:
                print '#\n', line_thick
            else:
                print '#\n', line


if __name__ == "__main__":

    sudoku = CreateSudoku()
    printSudoku(sudoku)






