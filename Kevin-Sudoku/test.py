
from numpy import empty
import pytesseract
import jellyfish
import difflib
import easyocr

datadrop = r'C:\Users\kevin\Code\Sudoku\Kevin-Sudoku\images\CurrentSudoku\\'
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
    data = (pytesseract.image_to_data(
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

    #print(data)
#print("puzzle:" + str(puzzle))
#print("string:" + string)

print("sPuzzle:" +sPuzzle)
rPuzzle = "050028790930651008840003010208000001300702500009106040093800006005300904086095000"
print("rPuzzle:" +rPuzzle)

ratio = difflib.SequenceMatcher(a=sPuzzle, b=rPuzzle).ratio()
print("ratio:" ,ratio)

print("mismatches:", jellyfish.damerau_levenshtein_distance(sPuzzle,rPuzzle))

number = 1
sresult = ''
reader = easyocr.Reader(['en'])
for number in range (1,82):
    result = reader.readtext(datadrop+ str(number)+'.png')
    if len(result) != 0:
        print (result[0][1][0])
        sresult = str(result[0][1][0]) +sresult
    else: 
        sresult = str(result) + '0'
    
print (sresult)