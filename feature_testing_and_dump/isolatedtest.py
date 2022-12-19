import math
from itertools import chain
import numpy as np
#coding based on formulae found in: https://www.calculatorsoup.com/calculators/technology/ppi-calculator.php

def resolution(diagonalSize):
    try:
        global w
        global h
        global screenRes
        
        diagonalSize = round(diagonalSize * 2)/2 #rounds to nearest half inch
        print(diagonalSize)

        if diagonalSize in chain(np.arange(13, 28, 0.5), np.arange(41,50, 0.5)): 
            w = 1920
            h = 1080
            screenRes = "1080p"
        elif diagonalSize in np.arange(27, 41, 0.5):
            w = 2560
            h = 1440
            screenRes = "1440p"
        elif diagonalSize in list(np.arange(55, 76, 0.5)):
            w = 3840
            h = 2160
            screenRes = "4k"
        elif diagonalSize > 75:
            w = 7680
            h = 4320
            screenRes = "8k"
        elif diagonalSize in np.arange(12, 21, 0.5):
            w = 1280
            h = 720
            screenRes = "720p"
        else:
            print("Somehow, you entered a size beyond the program's control...")
        return w, h

    except TypeError or ValueError:
        print("This value was not among the list of dimensions.")
    
        
        
def pixelDensity(diagonalSize):
    diagonalPixels = math.sqrt(((w*w) + (h*h)))
    rounded_diagonalPixels = round(diagonalPixels, 2)
    
    
    PPI = round((rounded_diagonalPixels / diagonalSize), 2)
    print(f"The size of the screen is {diagonalSize} inches and contains {PPI} pixels per inch at {screenRes}")
    
    return diagonalSize, rounded_diagonalPixels, PPI

def availableSizes():
    a = list(chain(np.arange(21,28,0.5), np.arange(27,35,0.5), np.arange(35,50, 0.5),
                   np.arange(55,76,0.5)))
    print(f'{a}, and to infinity.')
#availableSizes()

diagonalSize = float(input("What is the diagonal size of the screen in inches? "))

resolution(diagonalSize)
pixelDensity(float(diagonalSize))



#find max pixel density of each resolution.
#create different categories for TV's and monitors because resolution differs depending on use.