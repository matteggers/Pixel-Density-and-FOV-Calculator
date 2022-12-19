import math

#coding based on formulae found in: https://www.calculatorsoup.com/calculators/technology/ppi-calculator.php


def pixelDensity(diagonalSize):
    diagonalPixels = math.sqrt(((w*w) + (h*h)))
    rounded_diagonalPixels = round(diagonalPixels, 2)
    
    print(diagonalPixels)
    
    PPI = round((rounded_diagonalPixels / diagonalSize), 2)
    print(PPI)
    
    return diagonalSize, rounded_diagonalPixels, PPI

def resolution(diagonalSize):
    try:
        global w
        global h

        if diagonalSize in (24, 24.5, 40): ## did a long list of or that did not work. Asked a user on learnpython discord and was informed of this way, which works. if you're still reading this long line... Hello!
            w = 1920
            h = 1080
        elif diagonalSize in (27, 32, 34):
            w = 2560
            h = 1440
        elif diagonalSize in (55, 60, 65, 70, 75):
            w = 3840
            h = 2160
        else:
            print("Sorry, this size is not available at this time.")
        return w, h

    except TypeError or ValueError:
        print("This value was not among the list of dimensions.")


diagonalSize = float(input("Diagonal size of screen: "))

resolution(diagonalSize)
pixelDensity(float(diagonalSize))