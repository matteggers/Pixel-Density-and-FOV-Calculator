import math
from itertools import chain

def wTheorem(w): #Diagonal screen size in inches
    global hypotenuse
    global rounded_hypotenuse

    h = float(w / (16/9)) #assumes 16:9 aspect ratio

    hypotenuse = math.sqrt(((w*w) + (h*h)))
    rounded_hypotenuse = round(hypotenuse)

    return rounded_hypotenuse, hypotenuse, h

def hTheorem(h): #Diagonal screen size in inches
    global hypotenuse
    global rounded_hypotenuse
    
    w = float(h * (16/9))
 
    hypotenuse = math.sqrt(((w*w) + (h*h)))
    rounded_hypotenuse = round(hypotenuse)

    return rounded_hypotenuse, hypotenuse, h

def sizeCheck(rounded_hypotenuse):
    global pixelWidth
    global pixelHeight
    global resolution
    try:    
        if rounded_hypotenuse in chain(range(21,28), range(36,50)):
            pixelWidth = 1920
            pixelHeight = 1080
            resolution = "1080p"  
        elif rounded_hypotenuse in range(27,35):
            pixelWidth = 2560
            pixelHeight = 1440
            resolution = "1440p"
        elif rounded_hypotenuse in range(50,76):
            pixelWidth = 3840
            pixelHeight = 2160
            resolution = "4k"
        elif rounded_hypotenuse > 75:
            pixelWidth = 7680
            pixelHeight = 4320
            resolution = "8k"
        else:
            print(f"The diagonal length of the monitor is {rounded_hypotenuse}, which is out of range.")
    except NameError:
        print("NameError again!")
    return pixelWidth, pixelHeight
    
def pixelDensity(rounded_hypotenuse):
    diagonalPixels = math.sqrt(((pixelWidth*pixelWidth) + (pixelHeight*pixelHeight)))
    rounded_diagonalPixels = round(diagonalPixels, 2)
    
    
    PPI = round((rounded_diagonalPixels / rounded_hypotenuse), 2)
    print(f"There are {PPI} pixels per inch at {resolution}.")
    
    return rounded_hypotenuse, rounded_diagonalPixels, PPI

def allFunc():
    question = input("Would you like to input the width or height?\n")
    
    if question in ("Width", "width", "with", "w"):
        w = float(input("How wide would you like the screen in inches?\n"))
        wTheorem(w)
    if question in ("Height", "height", "h"):
        h = float(input("How tall would you like the screen in inches?\n"))
        hTheorem(h)

        
    sizeCheck(rounded_hypotenuse)
    pixelDensity(float(rounded_hypotenuse))
    
allFunc()