from sys import path
import keyboard
import pyautogui
import cv2
import matplotlib.pyplot as plt
import pytesseract
import time

###################################################################
#              Capture screenshot of puzzle area                  #
###################################################################
imgPath = r'C:\Users\kevin\Code\Sudoku\Kevin-Sudoku\images\img.png'

# tell the user what to do
pyautogui.alert("Move the mouse to to top left and press enter, then the bottom right and press enter", "Instructions")

# gets the board region's coordinates
keyboard.wait('enter')
left, top = pyautogui.position()
keyboard.wait('enter')
right, bottom = pyautogui.position()
width = right - left
height = bottom - top

print("The image is ", width,"x" , height)

#save the screenshot, region = left, top, width, and height
img = pyautogui.screenshot(imgPath, region=(left, top, width, height))

###################################################################
#      Convert screenshot into image the computer can read        #
###################################################################

originalImg = cv2.imread(imgPath,1)
widthNew = 800
heightNew = 800
print("The resized image is ", widthNew,"x" , heightNew)

resizedImg = cv2.resize(originalImg,(heightNew,widthNew))
imgGray = cv2.cvtColor(resizedImg,cv2.COLOR_BGR2GRAY)
#imgBlur = cv2.GaussianBlur(imgBW,(5,5),1)
#imgCanny =cv2.Canny(imgGray,50,50)

###################################################################
#              Parse out images of each Soduku cell               #
###################################################################

datadrop = r'C:\Users\kevin\Code\Sudoku\Kevin-Sudoku\images\CurrentSudoku\\'
CropValue = widthNew//90
cellWidth = widthNew//9
cellHeight = heightNew//9
number = 0

for y in range (0,9):
    for x in range (0,9):
        col = x+1
        row = y+1
        number = number +1
        cell = imgGray[row*cellHeight-cellHeight+CropValue : row*cellHeight-CropValue , col*cellHeight-cellHeight+CropValue : col*cellHeight-CropValue]
        cv2.imwrite(datadrop + str(number) +'.png',cell)

###################################################################
#                 Read number from image 1 to 81                  #
###################################################################

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

number = 1
puzzle = []
sPuzzle = ''
for number in range (1,82):
    string = (pytesseract.image_to_string(
        datadrop + str(number)+'.png', config=("-c tessedit"
                  "_char_whitelist=0123456789"
                  " --psm 6"
                  #" -l osd"
                  " ")))
    string = string.replace("\n", "")
    if string == '':
        puzzle += "0"
        sPuzzle = sPuzzle + "0"
    else:
        puzzle += string
        sPuzzle = sPuzzle + string

###################################################################
#                       Solve the Puzzle                          #
###################################################################
grid = []
solution = []
puzzle_string = sPuzzle

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
    global solution
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
    global solution
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
    for row in grid:
        solution = solution +row
    # solution = solution +grid

form_grid(puzzle_string)
solve()

###################################################################
#                Solve the Puzzle in the Game                     #
###################################################################

if len(solution)>0:
    n=0
    for col in range(9):
        for row in range(9):
            if(int(solution[n]) != int(puzzle[n])):
                x = left + (width/9)*(row) + width/18
                y = top + (height/9)*(col) + height/18
                pyautogui.click(x,y)
                time.sleep(0.2)
                pyautogui.click(x,y)
                pyautogui.keyDown(str(solution[n]))
                pyautogui.keyUp(str(solution[n]))
                time.sleep(0.01)
            n=n+1
    n=n+1