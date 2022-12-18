import math
#coding based on formulae found in: https://www.calculatorsoup.com/calculators/technology/ppi-calculator.php

def pixelDensity(diagonalSize):
    w = 1920
    h = 1080
    
    diagonalPixels = math.sqrt((w*w) + (h*h))
    rounded_diagonalPixels = round(diagonalPixels, 2)
    
    PPI = round((rounded_diagonalPixels / diagonalSize), 2)
    print(PPI)
    
    return diagonalSize, rounded_diagonalPixels, PPI


diagonalSize = input("Diagonal size of monitor: ")


pixelDensity(float(diagonalSize))



#def callAll():
#    diagonalPixels(int(size))