
import pyautogui as gui
import time
import cv2 as cv
import numpy

#Forming the Puzzle Grid
def form_grid(puzzle_string):
    global grid
    print('The Sudoku Problem')
    for i in range(0, len(puzzle_string), 9):
        row = puzzle_string[i:i+9]
        temp = []
        for block in row:
            temp.append(int(block))
        grid.append(temp)    
    printGrid()

#Function to print the grid
def printGrid():
    global grid
    for row in grid:
        print(row)

#Function to check if a digit can be placed in the given block
def possible(row,col,digit):
    global grid
    for i in range(0,9):
        if grid[row][i] == digit:
            return False
    for i in range(0,9):
        if grid[i][col] == digit:
            return False
    square_row = (row//3)*3
    square_col = (col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[square_row+i][square_col+j] == digit:
                return False    
    return True

#backtracking algorithm
def solve():
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for digit in range(1,10):
                    if possible(row,col,digit):
                        grid[row][col] = digit
                        solve()
                        grid[row][col] = 0  #Backtrack step
                return
    print('\nThe Solution')
    printGrid()

puzzle_string = "000082040000640582004005000065007800000204000002500960000400300249052000020820000"
grid = []
form_grid(puzzle_string)
solve()

