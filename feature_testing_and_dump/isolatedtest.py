import math
from itertools import chain
import numpy as np
import time
import sys
import atexit

#coding based on formulae found in: https://www.calculatorsoup.com/calculators/technology/ppi-calculator.php

def availableSizes():
    a = list(chain(np.arange(21,28,0.5), np.arange(27,35,0.5), np.arange(35,50, 0.5),
                   np.arange(55,76,0.5)))
    print(f'{a}, and to infinity.')


def monitorSize(diagonalSize):
    global w
    global h
    global screenRes
    
    diagonalSize = round(diagonalSize * 2)/2 #rounds to nearest half inch
    try:
        if diagonalSize in chain(np.arange(13, 28, 0.5), np.arange(41,50, 0.5)): 
            w = 1920
            h = 1080
            screenRes = "1080p"
        elif diagonalSize in np.arange(27,45,0.5):
            while True:
                isUltrawide = input("Is this monitor ultrawide? (Y/N) \n")
                if isUltrawide in ("Yes", "yes", "Y", "y"): #***add functionality to loop again if input was not entered correctly 
                    w = 2560
                    h = 1440
                    screenRes = "1440p"
                    break
                elif isUltrawide in ("No", "no", "N","n"):
                    w = 1920
                    h = 1080
                    screenRes = 1080
                    break
                print("Invalid choice made, please try again.")
        elif diagonalSize > 45:
            print("You have entered a size above or below the available range for a monitor.\n")
            print("Are you sure this is a monitor? Please restart the program and select the TV option.")
            exit() 
    except TypeError or ValueError or NameError:
        time.sleep(5)
        sys.exit("This value was not among the list of available dimensions.")


def tvSize(diagonalSize):
    try:
        global w
        global h
        global screenRes
        
        diagonalSize = round(diagonalSize * 2)/2 #rounds to nearest half inch

        if diagonalSize in np.arange(13, 43, 0.5): 
            w = 1920
            h = 1080
            screenRes = "1080p"
        if diagonalSize in np.arange(43,51, 0.5):
            is4k = input("Is this TV 4k? (Y/N)\n")
            while True:
                if is4k in ("Yes", "yes", "Y", "y"):
                    w = 3840
                    h = 2160
                    screenRes = "4k"
                    break
                elif is4k in ("No", "no", "N", "n"):
                    w = 1920
                    h = 1080
                    break
                print("Invalid choice made, please try again")
        elif diagonalSize in list(np.arange(55, 76, 0.5)):
            w = 3840
            h = 2160
            screenRes = "4k"
        elif diagonalSize > 75:
            w = 7680
            h = 4320
            screenRes = "8k"
        else:
            print("Somehow, you entered a size beyond the program's control...")
            exit()
        return w, h, screenRes, diagonalSize

    except TypeError or ValueError or NameError:
        sys.exit("This value was not among the list of available dimensions.")

        
def pixelDensity(diagonalSize):
    diagonalPixels = math.sqrt(((w*w) + (h*h)))
    rounded_diagonalPixels = round(diagonalPixels, 2)
    global PPI
    
    PPI = round((rounded_diagonalPixels / diagonalSize), 2)
    print(f"The size of the screen is {diagonalSize} inches and contains {PPI} pixels per inch at {screenRes}")
    
    exit()
    
    return diagonalSize, rounded_diagonalPixels, PPI


def pixelJudge(PPI):
    PPI = round(PPI *5)/5 #rounds to nearest 1/5
    
    if PPI in np.arange(95,111,0.2): #well aware this could be done better by rounding PPI, but I am just testing for now.
        print("This is in an optimal pixel density range.")
    elif PPI < 80:
        print(f"With a pixel density of {PPI}, the screen may be unclear at closer viewing distances.")
    elif PPI in np.arange(80,96, 0.2):
        print("The pixel density of this screen could be better, but it is ok.")


def exit():
    atexit.register(lambda: input("Press Enter to exit.")) #found on S/O
   
   
def betterCallAll():
    global diagonalSize
    
    diagonalSize = float(input("What is the diagonal size of the screen in inches\n "))
    
    screenType = input("Is the screen a TV or monitor? (TV/M) \n")
    if screenType in ("TV", "tv", "t", "v", "T", "V"):
        tvSize(diagonalSize)
    elif screenType in ("Monitor", "monitor", "M", "m"):
        monitorSize(diagonalSize)

           
    pixelDensity(diagonalSize)
    pixelJudge(PPI)
    
betterCallAll()