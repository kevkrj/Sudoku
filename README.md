# Sudoku

PuzzleCapture is the main file.

imgPath and datadrop will need to be updated to your own file structure.

This script will 
  take a screenshot of a Sudoku puzzle, 
  convert the screenshot into an image that is easy for OCR to read, 
  parse out images of the specific cells,
  read those parsed images,
  solve the sudoku puzzle using a backtracking algorithm,
  solve the puzzle in the online game.
 
Works with NYT puzzle and others but not all sudoku puzzles are easy for OCR to read and those won't work since they can't be read in with 100% accuracy (looking at you https://websudoku.com/)

Test.py is just a place where I was testing different OCR methods
Solver.py is the original version of the solver algorithm I took from someone else here on github.

Enjoy.
