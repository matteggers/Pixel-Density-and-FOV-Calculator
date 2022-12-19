import math



def pythagoras(w): #Diagonal screen size in inches
    global rounded_hypotenuse
    
    h = float(w / (16/9)) #assumes 16:9 aspect ratio
    
    hypotenuse = math.sqrt(((w*w) + (h*h)))
    rounded_hypotenuse = round(hypotenuse, 2)
    print(w)
    print(h)
    print(rounded_hypotenuse)
    print(type(rounded_hypotenuse))

    return rounded_hypotenuse, hypotenuse, h

def sizeCheck(rounded_hypotenuse):
    global pixelWidth
    global pixelHeight
    
    if rounded_hypotenuse in range (21,28): #RANGE DOESNT SUPPORT FLOAT
        pixelWidth = 1920
        pixelHeight = 1080
    elif rounded_hypotenuse in range (27,35):
        pixelWidth = 2560
        pixelHeight = 1440
    elif rounded_hypotenuse in range (50,76):
        pixelWidth = 3840
        pixelHeight = 2160
    elif rounded_hypotenuse > 75:
        pixelWidth = 7680
        pixelHeight = 4320
    else:
        print("Value not within range.")
        
    
    return pixelWidth, pixelHeight

w = float(input("How wide would you like the screen in inches?\n"))

pythagoras(w)

