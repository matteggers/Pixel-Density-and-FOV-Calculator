import math
#from pixelDensity import pixelDensity, resolution
    #w = commonDimensions.get(diagonalSize[0])
    #h = commonDimensions.get(diagonalSize[1])
    
commonDimensions = { #in inches, couldn't I have done this in excel?
    "24": [20.918, 11.766],
    "24.5": [21.354, 12.011],
    "27": [23.533, 13.237],
    "32": [27.89, 15.688],
    "34": [29.634, 16.669],
    "50": [43.579, 24.513],
    "55": [47.937, 26.964],
    "60": [52.295, 29.416],
    "65": [56.652, 31.867],
    "70": [61.01, 34.318],
    "74.9": [65.281, 36.721],
}

#can find the horizontal width of any screen by dividing height / (16/9). inversly can do so by width x (16/9)


def pythagoras(w): #Diagonal screen size in inches
    global rounded_hypotenuse
    
    h = w / (16/9)
    
    hypotenuse = math.sqrt(((w*w) + (h*h)))
    rounded_hypotenuse = round(hypotenuse)
    return rounded_hypotenuse, hypotenuse, h

def pythagoras(h): #Diagonal screen size in inches
    global rounded_hypotenuse
    
    w = h * (16/9)
    
    hypotenuse = math.sqrt(((w*w) + (h*h)))
    rounded_hypotenuse = round(hypotenuse)
    return rounded_hypotenuse, hypotenuse, w

def sizeCheck(rounded_hypotenuse):
    global pixelWidth
    global pixelHeight
    
    
    if 27 > rounded_hypotenuse >= 21:
        pixelWidth = 1920
        pixelHeight = 1080
    elif 34 >= rounded_hypotenuse >= 27:
        pixelWidth = 2560
        pixelHeight = 1440
    elif 75 >= rounded_hypotenuse >= 50:
        pixelWidth = 3840
        pixelHeight = 2160
    elif 75 > rounded_hypotenuse:
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


#eventually want it to ask if we want width or height, then display proper question
#w = float(input("How wide would you like the screen in inches? "))
#h = float(input("How tall would you like the screen in inches? "))

#pythagoras(w)
#sizeCheck(rounded_hypotenuse)
#pixelDensity(rounded_hypotenuse)

def allFunc():
    question = input("Would you like to input the width or height?\n")
    
    if question in ("Width", "width", "with", "w"):
        w = float(input("How wide would you like the screen in inches? "))
        pythagoras(w)
    elif question in ("Height", "height", "h"):
        h = float(input("How tall would you like the screen in inches? "))
        pythagoras(h)
        
    sizeCheck(rounded_hypotenuse)
    pixelDensity(rounded_hypotenuse)
    
allFunc()