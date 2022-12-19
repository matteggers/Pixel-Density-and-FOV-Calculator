import math
from itertools import chain
#coding based on formulae found in: https://www.calculatorsoup.com/calculators/technology/ppi-calculator.php

def pixelDensity(diagonalSize):
    diagonalPixels = math.sqrt(((w*w) + (h*h)))
    rounded_diagonalPixels = round(diagonalPixels, 2)
    
    
    PPI = round((rounded_diagonalPixels / diagonalSize), 2)
    print(f"The size of the screen is {diagonalSize} inches and contains {PPI} pixels per inch at {screenRes}")
    
    return diagonalSize, rounded_diagonalPixels, PPI

def resolution(diagonalSize):
    try:
        global w
        global h
        global screenRes
        
        diagonalSize = int(round(diagonalSize))

        if diagonalSize in chain(range(21,28), range(36,50)): 
            w = 1920
            h = 1080
            screenRes = "1080p"
        elif diagonalSize in range(27, 35):
            w = 2560
            h = 1440
            screenRes = "1440p"
        elif diagonalSize in range(55, 76):
            w = 3840
            h = 2160
            screenRes = "4k"
        elif diagonalSize > 75:
            w = 7680
            h = 4320
            screenRes = "8k"
        else:
            print("Somehow, you entered a size beyond the program's control...")
        return w, h, screenRes, diagonalSize

    except TypeError or ValueError:
        print("This value was not among the list of dimensions.")


diagonalSize = float(input("What is the diagonal size of the screen in inches? "))

resolution(diagonalSize)
pixelDensity(float(diagonalSize))