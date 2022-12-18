import math


def pythagoras(w): #Diagonal screen size in inches
    global rounded_hypotenuse
    
    h = float(w / (16/9)) #assumes 16:9 aspect ratio
    
    hypotenuse = math.sqrt(((w*w) + (h*h)))
    rounded_hypotenuse = round(hypotenuse)

    return rounded_hypotenuse, hypotenuse, h

def pythagoras(h): #Diagonal screen size in inches
    global rounded_hypotenuse
    
    w = float(h * (16/9))
    
    hypotenuse = math.sqrt(((w*w) + (h*h)))
    rounded_hypotenuse = round(hypotenuse)
    
    return rounded_hypotenuse, hypotenuse, w

def sizeCheck(rounded_hypotenuse):
    global pixelWidth
    global pixelHeight
    
    if 21 <= rounded_hypotenuse <= 27:
        pixelWidth = 1920
        pixelHeight = 1080
    elif 27 <= rounded_hypotenuse <= 34:
        pixelWidth = 2560
        pixelHeight = 1440
    elif 50 <= rounded_hypotenuse <= 75:
        pixelWidth = 3840
        pixelHeight = 2160
    elif 75 < rounded_hypotenuse:
        pixelWidth = 7680
        pixelHeight = 4320
    else:
        print("Value not within range.")
    return pixelWidth, pixelHeight
    
def pixelDensity(rounded_hypotenuse):
    diagonalPixels = math.sqrt(((pixelWidth*pixelWidth) + (pixelHeight*pixelHeight)))
    rounded_diagonalPixels = round(diagonalPixels, 2)
    
    
    PPI = round((rounded_diagonalPixels / rounded_hypotenuse), 2)
    print(f"There are {PPI} pixels per inch")
    
    return rounded_hypotenuse, rounded_diagonalPixels, PPI

def allFunc():
    question = input("Would you like to input the width or height?\n")
    
    if question in ("Width", "width", "with", "w"):
        w = float(input("How wide would you like the screen in inches?\n"))
        pythagoras(w)
    elif question in ("Height", "height", "h"):
        h = float(input("How tall would you like the screen in inches?\n"))
        pythagoras(h)
        
    sizeCheck(float(rounded_hypotenuse))
    pixelDensity(float(rounded_hypotenuse))
    
allFunc()