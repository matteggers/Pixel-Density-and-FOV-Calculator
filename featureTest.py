import math
#coding based on formulae found in: https://www.calculatorsoup.com/calculators/technology/ppi-calculator.php

#commonDimensions = { #in inches, couldn't I have done this in excel?
#    "24": [20.918, 11.766],
#    "24.5": [21.354, 12.011],
#    "27": [23.533, 13.237],
#    "32": [27.89, 15.688],
#    "34": [29.634, 16.669],
#    "50": [43.579, 24.513],
#    "55": [47.937, 26.964],
#    "60": [52.295, 29.416],
#    "65": [56.652, 31.867],
#    "70": [61.01, 34.318],
#    "74.9": [65.281, 36.721],
#}

w = 0
h = 0

def pixelDensity(diagonalSize):
    #w = commonDimensions.get(diagonalSize[0])
    #h = commonDimensions.get(diagonalSize[1])

    
    
    diagonalPixels = math.sqrt((w*w) + (h*h))
    rounded_diagonalPixels = round(diagonalPixels, 2)
    
    PPI = round((rounded_diagonalPixels / diagonalSize), 2)
    print(PPI)
    
    return diagonalSize, rounded_diagonalPixels, PPI






#pixelDensity(float(diagonalSize))


def resolution():
    #try:
        global w
        global h
        if diagonalSize == "24" or "24.5" or "40":
            w = 1920
            h = 1080
        elif diagonalSize == "27" or "32" or "34":
            w = 2560
            h = 1440
        elif diagonalSize == "55" or "60" or "65" or "70" or "74.9":
            w = 3840
            h = 2160
        else:
            print("Sorry, this size is not available at this time.")
            
        
    #except


diagonalSize = input("Diagonal size of monitor: ")

resolution()
pixelDensity(float(diagonalSize))